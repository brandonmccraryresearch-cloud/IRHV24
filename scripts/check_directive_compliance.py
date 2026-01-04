#!/usr/bin/env python3
"""
Directive Compliance Checker for IRH Computational Research

This script enforces Directive A (No-Tuning Constraint) by scanning Python code
and Jupyter notebooks for hardcoded experimental values, improper labeling,
and missing placeholder warnings.

Usage:
    python check_directive_compliance.py \
        --check-hardcoded-values \
        --check-experimental-labels \
        --check-placeholder-warnings \
        --output violations.json

Author: IRH Computational Research Team
Version: 1.0.0
"""

import argparse
import ast
import json
import re
import sys
from pathlib import Path
from typing import List, Dict, Any, Set
import nbformat


# Known experimental values that should ONLY appear with validation labels
EXPERIMENTAL_VALUES = {
    # Fine-structure constant and related
    "137.035999": "Fine-structure constant α⁻¹",
    "137.036": "Fine-structure constant α⁻¹",
    "0.00729735": "Fine-structure constant α",
    
    # Electron properties
    "0.510998": "Electron mass (MeV/c²)",
    "0.511": "Electron mass (MeV/c²)",
    "9.10938": "Electron mass (kg × 10⁻³¹)",
    "9.109": "Electron mass (kg × 10⁻³¹)",
    
    # Fundamental constants
    "1.60217": "Elementary charge (C × 10⁻¹⁹)",
    "1.602": "Elementary charge (C × 10⁻¹⁹)",
    "6.62607": "Planck constant (Js × 10⁻³⁴)",
    "6.626": "Planck constant (Js × 10⁻³⁴)",
    
    # Muon and tau masses
    "105.658": "Muon mass (MeV/c²)",
    "1776.86": "Tau mass (MeV/c²)",
    "1776.9": "Tau mass (MeV/c²)",
    
    # Cosmological constants
    "1.054e-52": "Cosmological constant Λ (m⁻²)",
    "10⁻⁵²": "Cosmological constant order of magnitude",
    "10⁻¹²³": "Vacuum energy discrepancy",
    
    # Gauge couplings at MZ scale
    "0.357": "SU(3) coupling α₃",
    "0.034": "SU(2) coupling α₂",
    "0.0169": "U(1) coupling α₁",
    
    # QCD string tension
    "1.2": "QCD string tension (GeV/fm) or (GeV²)",
}


# Validation label patterns that indicate proper usage
VALIDATION_LABELS = [
    r"EXPERIMENTAL\s+VALUE",
    r"FOR\s+VALIDATION\s+ONLY",
    r"VALIDATION",
    r"EXPERIMENTAL\s*-\s*FOR\s+VALIDATION",
    r"CODATA",
    r"MEASURED\s+VALUE",
]


# Placeholder warning patterns
PLACEHOLDER_WARNINGS = [
    r"WARNING.*PLACEHOLDER",
    r"TODO.*DERIVE",
    r"PLACEHOLDER.*TOPOLOGICAL",
    r"PENDING.*DERIVATION",
]


class ViolationDetector:
    """Detects Directive A violations in Python code and notebooks."""
    
    def __init__(self):
        self.violations: List[Dict[str, Any]] = []
        
    def check_hardcoded_values(self, content: str, filepath: str, 
                               line_offset: int = 0) -> None:
        """
        Check for hardcoded experimental values in code.
        
        Args:
            content: Source code or cell content
            filepath: Path to file being checked
            line_offset: Line offset for notebook cells
        """
        lines = content.split('\n')
        
        for line_num, line in enumerate(lines, start=1):
            # Skip comments and docstrings for this check
            stripped = line.strip()
            if stripped.startswith('#') or stripped.startswith('"""') or stripped.startswith("'''"):
                continue
                
            # Check for experimental value patterns
            for value_pattern, description in EXPERIMENTAL_VALUES.items():
                # Handle scientific notation patterns
                if 'e' in value_pattern or '⁻' in value_pattern:
                    # More lenient matching for scientific notation
                    pattern = value_pattern.replace('e', r'[eE]').replace('⁻', '-?')
                    if re.search(pattern, line):
                        # Check if properly labeled
                        if not self._has_validation_label(line, lines, line_num - 1):
                            self.violations.append({
                                "file": filepath,
                                "line": line_num + line_offset,
                                "value": value_pattern,
                                "context": description,
                                "severity": "CRITICAL",
                                "message": f"Hardcoded experimental value ({description}) without validation label",
                                "code_snippet": line.strip()
                            })
                else:
                    # Exact matching for regular decimals
                    if value_pattern in line:
                        # Check if properly labeled
                        if not self._has_validation_label(line, lines, line_num - 1):
                            self.violations.append({
                                "file": filepath,
                                "line": line_num + line_offset,
                                "value": value_pattern,
                                "context": description,
                                "severity": "CRITICAL",
                                "message": f"Hardcoded experimental value ({description}) without validation label",
                                "code_snippet": line.strip()
                            })
    
    def _has_validation_label(self, line: str, all_lines: List[str], 
                             line_idx: int) -> bool:
        """
        Check if a line with experimental value has proper validation label.
        
        Checks the current line and up to 3 lines before it for labels.
        """
        # Check current line
        for pattern in VALIDATION_LABELS:
            if re.search(pattern, line, re.IGNORECASE):
                return True
        
        # Check up to 3 lines before
        for offset in range(1, 4):
            if line_idx - offset >= 0:
                prev_line = all_lines[line_idx - offset]
                for pattern in VALIDATION_LABELS:
                    if re.search(pattern, prev_line, re.IGNORECASE):
                        return True
        
        return False
    
    def check_experimental_labels(self, content: str, filepath: str,
                                  line_offset: int = 0) -> None:
        """
        Check that experimental values are properly labeled.
        
        This is a complementary check to ensure labels are used correctly.
        """
        lines = content.split('\n')
        
        for line_num, line in enumerate(lines, start=1):
            # Look for validation labels
            has_label = False
            for pattern in VALIDATION_LABELS:
                if re.search(pattern, line, re.IGNORECASE):
                    has_label = True
                    break
            
            if has_label:
                # Check if there's an actual value nearby
                has_value = False
                for offset in range(-1, 3):
                    check_idx = line_num - 1 + offset
                    if 0 <= check_idx < len(lines):
                        check_line = lines[check_idx]
                        # Look for numerical assignments
                        if re.search(r'=\s*[\d.eE-]+', check_line):
                            has_value = True
                            break
                
                if not has_value:
                    self.violations.append({
                        "file": filepath,
                        "line": line_num + line_offset,
                        "value": "N/A",
                        "context": "Validation label without associated value",
                        "severity": "WARNING",
                        "message": "Validation label found but no experimental value nearby",
                        "code_snippet": line.strip()
                    })
    
    def check_placeholder_warnings(self, content: str, filepath: str,
                                   line_offset: int = 0) -> None:
        """
        Check that placeholder implementations have WARNING comments.
        
        Looks for suspicious patterns that might be placeholders without warnings.
        """
        lines = content.split('\n')
        
        # Patterns that suggest placeholder implementations
        placeholder_patterns = [
            (r'#.*TODO', "TODO comment without WARNING"),
            (r'#.*FIXME', "FIXME comment without WARNING"),
            (r'#.*HACK', "HACK comment without WARNING"),
            (r'#.*temporary', "Temporary implementation without WARNING"),
            (r'pass\s*#.*derive', "Placeholder derivation without WARNING"),
        ]
        
        for line_num, line in enumerate(lines, start=1):
            for pattern, description in placeholder_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    # Check if WARNING is present
                    has_warning = False
                    for warning_pattern in PLACEHOLDER_WARNINGS:
                        if re.search(warning_pattern, line, re.IGNORECASE):
                            has_warning = True
                            break
                    
                    # Also check nearby lines
                    if not has_warning:
                        for offset in range(-2, 3):
                            check_idx = line_num - 1 + offset
                            if 0 <= check_idx < len(lines):
                                check_line = lines[check_idx]
                                for warning_pattern in PLACEHOLDER_WARNINGS:
                                    if re.search(warning_pattern, check_line, re.IGNORECASE):
                                        has_warning = True
                                        break
                    
                    if not has_warning:
                        self.violations.append({
                            "file": filepath,
                            "line": line_num + line_offset,
                            "value": "N/A",
                            "context": description,
                            "severity": "WARNING",
                            "message": f"Placeholder without WARNING: {description}",
                            "code_snippet": line.strip()
                        })
    
    def check_python_file(self, filepath: Path, check_flags: Dict[str, bool]) -> None:
        """Check a Python source file for violations."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if check_flags.get('hardcoded_values', False):
                self.check_hardcoded_values(content, str(filepath))
            
            if check_flags.get('experimental_labels', False):
                self.check_experimental_labels(content, str(filepath))
            
            if check_flags.get('placeholder_warnings', False):
                self.check_placeholder_warnings(content, str(filepath))
                
        except Exception as e:
            print(f"Error checking {filepath}: {e}", file=sys.stderr)
    
    def check_notebook_file(self, filepath: Path, check_flags: Dict[str, bool]) -> None:
        """Check a Jupyter notebook for violations."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                nb = nbformat.read(f, as_version=4)
            
            for cell_idx, cell in enumerate(nb.cells):
                if cell.cell_type == 'code':
                    content = cell.source
                    # Use cell index for line offset
                    line_offset = cell_idx * 1000  # Arbitrary offset to distinguish cells
                    
                    if check_flags.get('hardcoded_values', False):
                        self.check_hardcoded_values(content, str(filepath), line_offset)
                    
                    if check_flags.get('experimental_labels', False):
                        self.check_experimental_labels(content, str(filepath), line_offset)
                    
                    if check_flags.get('placeholder_warnings', False):
                        self.check_placeholder_warnings(content, str(filepath), line_offset)
                        
        except Exception as e:
            print(f"Error checking notebook {filepath}: {e}", file=sys.stderr)
    
    def get_violations(self) -> List[Dict[str, Any]]:
        """Return all detected violations."""
        return self.violations
    
    def has_critical_violations(self) -> bool:
        """Check if any critical violations were found."""
        return any(v['severity'] == 'CRITICAL' for v in self.violations)


def main():
    """Main entry point for the compliance checker."""
    parser = argparse.ArgumentParser(
        description='Check IRH code for Directive A compliance violations'
    )
    parser.add_argument(
        '--check-hardcoded-values',
        action='store_true',
        help='Check for hardcoded experimental values'
    )
    parser.add_argument(
        '--check-experimental-labels',
        action='store_true',
        help='Verify experimental values are properly labeled'
    )
    parser.add_argument(
        '--check-placeholder-warnings',
        action='store_true',
        help='Check that placeholders have WARNING comments'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='violations.json',
        help='Output file for violation report (JSON format)'
    )
    parser.add_argument(
        '--paths',
        type=str,
        nargs='+',
        default=['notebooks/', 'scripts/', 'verification/'],
        help='Paths to check (default: notebooks/, scripts/, verification/)'
    )
    
    args = parser.parse_args()
    
    # Determine what to check
    check_flags = {
        'hardcoded_values': args.check_hardcoded_values,
        'experimental_labels': args.check_experimental_labels,
        'placeholder_warnings': args.check_placeholder_warnings,
    }
    
    # If no flags specified, check everything
    if not any(check_flags.values()):
        check_flags = {k: True for k in check_flags}
    
    # Initialize detector
    detector = ViolationDetector()
    
    # Scan all specified paths
    for path_str in args.paths:
        path = Path(path_str)
        if not path.exists():
            print(f"Warning: Path {path} does not exist, skipping", file=sys.stderr)
            continue
        
        if path.is_file():
            # Check single file
            if path.suffix == '.py':
                detector.check_python_file(path, check_flags)
            elif path.suffix == '.ipynb':
                detector.check_notebook_file(path, check_flags)
        else:
            # Check directory recursively
            for py_file in path.rglob('*.py'):
                detector.check_python_file(py_file, check_flags)
            
            for nb_file in path.rglob('*.ipynb'):
                # Skip checkpoint files
                if '.ipynb_checkpoints' not in str(nb_file):
                    detector.check_notebook_file(nb_file, check_flags)
    
    # Get violations
    violations = detector.get_violations()
    
    # Generate report
    report = {
        'total_violations': len(violations),
        'critical_violations': sum(1 for v in violations if v['severity'] == 'CRITICAL'),
        'warning_violations': sum(1 for v in violations if v['severity'] == 'WARNING'),
        'violations': violations,
        'check_flags': check_flags,
    }
    
    # Write JSON output
    with open(args.output, 'w') as f:
        json.dump(report, f, indent=2)
    
    # Print summary
    print(f"\n{'='*70}")
    print("DIRECTIVE A COMPLIANCE CHECK RESULTS")
    print(f"{'='*70}")
    print(f"Total violations found: {report['total_violations']}")
    print(f"  - Critical: {report['critical_violations']}")
    print(f"  - Warnings: {report['warning_violations']}")
    print(f"\nDetailed report written to: {args.output}")
    
    if violations:
        print(f"\n{'='*70}")
        print("VIOLATION SUMMARY:")
        print(f"{'='*70}")
        for v in violations[:10]:  # Show first 10
            print(f"\n[{v['severity']}] {v['file']}:{v['line']}")
            print(f"  {v['message']}")
            print(f"  Code: {v['code_snippet'][:80]}")
        
        if len(violations) > 10:
            print(f"\n... and {len(violations) - 10} more violations")
            print(f"See {args.output} for complete list")
    
    # Exit with error code if critical violations found
    if detector.has_critical_violations():
        print(f"\n{'='*70}")
        print("❌ CRITICAL VIOLATIONS DETECTED - BUILD FAILED")
        print(f"{'='*70}")
        sys.exit(1)
    elif violations:
        print(f"\n{'='*70}")
        print("⚠️  WARNINGS DETECTED - Please review")
        print(f"{'='*70}")
        sys.exit(0)  # Don't fail build on warnings
    else:
        print(f"\n{'='*70}")
        print("✅ NO VIOLATIONS DETECTED - All checks passed")
        print(f"{'='*70}")
        sys.exit(0)


if __name__ == '__main__':
    main()
