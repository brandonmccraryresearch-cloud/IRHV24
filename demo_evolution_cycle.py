#!/usr/bin/env python3
"""
Demonstration: IRH Theory Evolution System - First Production Run

This script demonstrates the complete evolution cycle:
1. Compute baseline predictions from topological invariants
2. Validate against experimental measurements (CODATA, PDG, Planck)
3. Analyze error patterns
4. Generate AI-powered refinement suggestions
5. Test and (optionally) integrate successful refinements

All operations follow Directive A: NO hardcoded experimental values as inputs.
Experimental values are used ONLY for validation comparison.

Author: IRH Computational Research Team
Date: 2026-01-09
"""

import sys
import json
from datetime import datetime
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

from evolution_system import (
    CalculationEngine,
    ValidationModule,
    ErrorAnalyzer,
    ExperimentalDatabase
)


def print_header(title: str, char: str = "=", width: int = 70):
    """Print a formatted section header."""
    print()
    print(char * width)
    print(title.center(width))
    print(char * width)
    print()


def print_section(title: str):
    """Print a section title."""
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print(f"{'=' * 60}\n")


def main():
    """Run demonstration evolution cycle."""
    
    print_header("IRH THEORY EVOLUTION SYSTEM", "=")
    print_header("First Production Evolution Cycle", "-")
    
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Initialize components
    print_section("1. INITIALIZING COMPONENTS")
    
    db = ExperimentalDatabase()
    print(f"✓ Experimental Database: {db.count()} constants loaded")
    
    engine = CalculationEngine()
    print(f"✓ Calculation Engine: Ready")
    
    validator = ValidationModule(db)
    print(f"✓ Validation Module: Ready")
    
    analyzer = ErrorAnalyzer()
    print(f"✓ Error Analyzer: Ready")
    
    # Compute baseline predictions
    print_section("2. COMPUTING BASELINE PREDICTIONS")
    print("Deriving all predictions from topological invariants...")
    print("(No experimental values used as inputs - Directive A)")
    print()
    
    predictions = engine.compute_all_predictions()
    
    # Convert dict to list for easier handling
    pred_list = list(predictions.values()) if isinstance(predictions, dict) else predictions
    
    print(f"✓ Computed {len(pred_list)} predictions:")
    print()
    
    for i, pred in enumerate(pred_list[:5], 1):
        print(f"  {i}. {pred.symbol:10s} = {float(pred.value):12.6g}  ({pred.name})")
    
    if len(pred_list) > 5:
        print(f"  ... and {len(pred_list) - 5} more")
    
    # Validate against experiments
    print_section("3. VALIDATING AGAINST EXPERIMENTS")
    print("Comparing predictions to CODATA 2022 / PDG 2022 / Planck 2018...")
    print("(Experimental values used ONLY for validation - Directive A)")
    print()
    
    validation_report = validator.validate_all(predictions)
    
    print(f"Validation Results:")
    print(f"  Excellent (<1σ):  {validation_report.excellent_count:3d}")
    print(f"  Good (1-3σ):      {validation_report.good_count:3d}")
    print(f"  Fair (3-5σ):      {validation_report.fair_count:3d}")
    print(f"  Poor (>5σ):       {validation_report.poor_count:3d}")
    print(f"  ---")
    print(f"  Total compared:   {validation_report.compared_predictions:3d}")
    print(f"  Mean σ-deviation: {validation_report.mean_sigma_deviation:.2f}")
    print(f"  Pass rate (≤3σ):  {validation_report.overall_pass_rate * 100:.1f}%")
    
    # Analyze error patterns
    print_section("4. ANALYZING ERROR PATTERNS")
    print("Identifying systematic discrepancies...")
    print()
    
    error_analysis = analyzer.analyze(validation_report)
    
    print(f"Error Patterns Detected: {len(error_analysis.patterns)}")
    print()
    
    # Group patterns by severity
    critical = [p for p in error_analysis.patterns if p.severity.value == "critical"]
    high = [p for p in error_analysis.patterns if p.severity.value == "high"]
    medium = [p for p in error_analysis.patterns if p.severity.value == "medium"]
    
    if critical:
        print(f"  Critical ({len(critical)}):")
        for p in critical[:3]:
            print(f"    • {p.description}")
        if len(critical) > 3:
            print(f"    ... and {len(critical) - 3} more")
    
    if high:
        print(f"  High ({len(high)}):")
        for p in high[:3]:
            print(f"    • {p.description}")
        if len(high) > 3:
            print(f"    ... and {len(high) - 3} more")
    
    if medium:
        print(f"  Medium ({len(medium)}):")
        for p in medium[:2]:
            print(f"    • {p.description}")
        if len(medium) > 2:
            print(f"    ... and {len(medium) - 2} more")
    
    # Generate refinement suggestions
    print_section("5. GENERATING REFINEMENT SUGGESTIONS")
    print("AI Advisor analyzing error patterns...")
    print("(All suggestions must have topological origin - Directive A)")
    print()
    
    from evolution_system import AIAdvisor
    advisor = AIAdvisor()
    
    # Get top suggestions
    suggestions = advisor.get_top_suggestions(error_analysis.to_dict(), n=5)
    
    print(f"Generated {len(suggestions)} refinement suggestions")
    print()
    
    if suggestions:
        for i, suggestion in enumerate(suggestions, 1):
            mod = suggestion.modification
            print(f"  Suggestion {i}: {mod.name}")
            print(f"    Type: {mod.refinement_type.value}")
            print(f"    Topological Basis: {mod.topological_basis[:60]}...")
            print(f"    Confidence: {mod.confidence.value}")
            print(f"    Priority: {mod.priority_score:.2f}")
            print()
    else:
        print("  ℹ No refinement suggestions generated in this cycle.")
        print("  This may occur when:")
        print("    • All predictions already within acceptable bounds")
        print("    • Error patterns too complex for current templates")
        print("    • System needs additional topological modification templates")
        print()
    
    # Summary
    print_section("6. SUMMARY")
    
    print(f"Evolution Cycle Status: COMPLETED")
    print()
    print(f"Baseline Performance:")
    print(f"  • Predictions computed: {len(pred_list)}")
    print(f"  • Predictions validated: {validation_report.compared_predictions}")
    print(f"  • Mean σ-deviation: {validation_report.mean_sigma_deviation:.2f}")
    print(f"  • Pass rate (≤3σ): {validation_report.overall_pass_rate * 100:.1f}%")
    print()
    
    if suggestions:
        print(f"Next Steps:")
        print(f"  • Test top {min(len(suggestions), 3)} refinement suggestions")
        print(f"  • Validate that improvements don't cause regressions")
        print(f"  • Integrate successful refinements into theory")
        print(f"  • Update documentation with theoretical rationale")
    else:
        print(f"Next Steps:")
        print(f"  • Review error patterns to identify missing topological structures")
        print(f"  • Expand AI Advisor templates with new topological modifications")
        print(f"  • Consider higher-order corrections (Chern classes, Berry phases)")
        print(f"  • Investigate RG flow effects on discrepant predictions")
    
    print()
    print_header("DEMONSTRATION COMPLETE", "=")
    print()
    
    # Export results
    output_dir = Path("outputs/evolution_system")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = output_dir / f"evolution_cycle_{timestamp}.json"
    
    results = {
        "timestamp": timestamp,
        "predictions": [p.to_dict() for p in pred_list],
        "validation": validation_report.to_dict(),
        "error_analysis": error_analysis.to_dict(),
        "suggestions": [s.to_dict() for s in suggestions],
        "summary": {
            "predictions_count": len(pred_list),
            "mean_sigma": validation_report.mean_sigma_deviation,
            "pass_rate": validation_report.overall_pass_rate,
            "suggestions_count": len(suggestions)
        }
    }
    
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"✓ Full results exported to: {output_file}")
    print()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
