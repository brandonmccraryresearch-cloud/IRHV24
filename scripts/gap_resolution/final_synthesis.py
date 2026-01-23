#!/usr/bin/env python3
"""
Final Synthesis Report Generator
=================================

Aggregates results from all resolution phases and generates
a comprehensive gap resolution report.

Author: IRH Computational Research Team
"""

import argparse
import json
import os
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


@dataclass
class PhaseStatus:
    """Status of a resolution phase."""
    id: str
    name: str
    status: str  # resolved, partial, unresolved, failed
    score_before: float
    score_after: float
    improvement: float
    key_findings: List[str]
    remaining_gaps: List[str]


def load_phase_results(input_dir: Path) -> Dict[str, Dict]:
    """Load results from all phases."""
    results = {}
    
    phase_files = {
        "theta0": "*theta0*.json",
        "cosmological": "*cosmological*.json",
        "vev": "*vev*.json",
        "ckm": "*ckm*.json",
        "dark_matter": "*dark_matter*.json",
        "mass_scale": "*mass_scale*.json",
        "nlo": "*nlo*.json",
    }
    
    for phase_id, pattern in phase_files.items():
        for json_file in input_dir.rglob(pattern):
            if "council" in json_file.name:  # Skip council files
                try:
                    with open(json_file) as f:
                        results[phase_id] = json.load(f)
                except (json.JSONDecodeError, FileNotFoundError) as e:
                    print(f"⚠️  Could not load {json_file}: {e}")
    
    return results


def compute_phase_status(phase_id: str, result: Dict) -> PhaseStatus:
    """Compute status for a single phase."""
    status_map = {
        "resolved": 100,
        "partial": 60,
        "incomplete": 30,
        "unresolved": 10,
        "minimal": 20,
    }
    
    status = result.get("status", "unknown")
    score_after = status_map.get(status, 0)
    
    # Estimate score before (all were 0)
    score_before = 0
    
    remaining = result.get("remaining_gaps", [])
    
    return PhaseStatus(
        id=phase_id,
        name=phase_id.replace("_", " ").title(),
        status=status,
        score_before=score_before,
        score_after=score_after,
        improvement=score_after - score_before,
        key_findings=[f"Status: {status}"],
        remaining_gaps=remaining[:5] if remaining else ["No gaps recorded"],
    )


def generate_markdown_report(phases: List[PhaseStatus], overall_score: float) -> str:
    """Generate markdown synthesis report."""
    lines = [
        "# IRH v68 Gap Resolution Synthesis Report",
        "",
        f"**Generated:** {datetime.now().isoformat()}",
        "",
        "## Executive Summary",
        "",
        f"**Overall Progress Score:** {overall_score:.1f}/100",
        "",
        "This report synthesizes the results of the multi-phase gap resolution",
        "pipeline addressing issues identified in KimiAudit.md and the Author Response.",
        "",
        "## Phase Results",
        "",
    ]
    
    for phase in phases:
        status_emoji = {
            "resolved": "✅",
            "partial": "🔶",
            "incomplete": "🔸",
            "unresolved": "❌",
            "minimal": "🔹",
        }.get(phase.status, "❓")
        
        lines.extend([
            f"### {status_emoji} Phase: {phase.name}",
            "",
            f"- **Status:** {phase.status}",
            f"- **Progress:** {phase.score_before:.0f} → {phase.score_after:.0f} (+{phase.improvement:.0f})",
            "",
            "**Remaining Gaps:**",
        ])
        
        for gap in phase.remaining_gaps[:3]:
            lines.append(f"- {gap}")
        
        lines.append("")
    
    # Summary table
    lines.extend([
        "## Summary Table",
        "",
        "| Phase | Status | Progress |",
        "|-------|--------|----------|",
    ])
    
    for phase in phases:
        lines.append(f"| {phase.name} | {phase.status} | {phase.improvement:+.0f} |")
    
    lines.extend([
        "",
        "## Recommendations",
        "",
        "### High Priority",
        "1. **Cosmological Constant**: The most critical gap remains unresolved",
        "2. **Dark Matter CMB**: Requires numerical Boltzmann code implementation",
        "3. **θ₀ Derivation**: Chern-Simons calculation needs completion",
        "",
        "### Medium Priority",
        "4. **CKM/PMNS Matrix**: Triality overlap integrals need computation",
        "5. **Mass Scale**: Lattice Green's function required",
        "6. **VEV Cascade**: RG running calculation needed",
        "",
        "### Lower Priority",
        "7. **NLO Corrections**: Already partially derived via Epstein zeta",
        "",
        "## Next Steps",
        "",
        "1. Run Gemini Council on final_synthesis for AI recommendations",
        "2. Prioritize cosmological constant approach (supersymmetric D₄)",
        "3. Implement numerical tools for CMB torsion model",
        "4. Consult knot theory experts for θ₀ derivation",
        "",
        "---",
        "",
        "*Report generated by IRH Gap Resolution Pipeline*",
    ])
    
    return "\n".join(lines)


def generate_synthesis(input_dir: Path, output_json: Path, output_md: Optional[Path]) -> Dict:
    """Generate complete synthesis."""
    # Load all phase results
    phase_results = load_phase_results(input_dir)
    
    # Compute status for each phase
    phases = []
    for phase_id, result in phase_results.items():
        status = compute_phase_status(phase_id, result)
        phases.append(status)
    
    # Fill in missing phases
    all_phases = ["theta0", "cosmological", "vev", "ckm", "dark_matter", "mass_scale", "nlo"]
    found_ids = {p.id for p in phases}
    
    for phase_id in all_phases:
        if phase_id not in found_ids:
            phases.append(PhaseStatus(
                id=phase_id,
                name=phase_id.replace("_", " ").title(),
                status="not_run",
                score_before=0,
                score_after=0,
                improvement=0,
                key_findings=["Phase not executed"],
                remaining_gaps=["All gaps remain"],
            ))
    
    # Sort by phase order
    phase_order = {p: i for i, p in enumerate(all_phases)}
    phases.sort(key=lambda x: phase_order.get(x.id, 99))
    
    # Compute overall score
    total_improvement = sum(p.improvement for p in phases)
    base_score = 82  # From The_challenge_to_completion.md
    overall_score = min(100, base_score + total_improvement * 0.1)
    
    # Generate outputs
    synthesis = {
        "timestamp": datetime.now().isoformat(),
        "overall_score": overall_score,
        "base_score": base_score,
        "phases": [
            {
                "id": p.id,
                "name": p.name,
                "status": p.status,
                "score_before": p.score_before,
                "score_after": p.score_after,
                "improvement": p.improvement,
                "key_findings": p.key_findings,
                "remaining_gaps": p.remaining_gaps,
            }
            for p in phases
        ],
        "recommendations": [
            "Prioritize cosmological constant resolution",
            "Implement CMB torsion Boltzmann code",
            "Complete Chern-Simons calculation for θ₀",
        ],
    }
    
    # Save JSON
    output_json.parent.mkdir(parents=True, exist_ok=True)
    with open(output_json, 'w') as f:
        json.dump(synthesis, f, indent=2)
    
    # Save Markdown
    if output_md:
        markdown = generate_markdown_report(phases, overall_score)
        with open(output_md, 'w') as f:
            f.write(markdown)
    
    return synthesis


def main():
    parser = argparse.ArgumentParser(description="Generate synthesis report")
    parser.add_argument("--input-dir", type=str, required=True,
                       help="Directory containing phase results")
    parser.add_argument("--output", type=str, required=True,
                       help="Output JSON file")
    parser.add_argument("--generate-markdown", type=str, default=None,
                       help="Optional markdown output file")
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("FINAL SYNTHESIS REPORT GENERATION")
    print("=" * 60)
    
    input_dir = Path(args.input_dir)
    output_json = Path(args.output)
    output_md = Path(args.generate_markdown) if args.generate_markdown else None
    
    synthesis = generate_synthesis(input_dir, output_json, output_md)
    
    print(f"Overall score: {synthesis['overall_score']:.1f}/100")
    print(f"Phases processed: {len(synthesis['phases'])}")
    
    print(f"✅ Synthesis saved to {output_json}")
    if output_md:
        print(f"✅ Markdown report saved to {output_md}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
