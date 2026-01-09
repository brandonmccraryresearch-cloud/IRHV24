#!/usr/bin/env python3
"""
Test the Integration System with a refinement suggestion.

This script demonstrates:
1. Getting a refinement suggestion from AI Advisor
2. Testing the refinement in isolation
3. Running regression tests
4. Checking symmetry preservation
5. Generating integration report

Author: IRH Computational Research Team
Date: 2026-01-09
"""

import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from evolution_system import (
    CalculationEngine,
    ValidationModule,
    ErrorAnalyzer,
    AIAdvisor,
    IntegrationSystem,
    ExperimentalDatabase
)


def print_section(title: str):
    """Print a section title."""
    print(f"\n{'=' * 70}")
    print(f"  {title}")
    print(f"{'=' * 70}\n")


def main():
    """Test integration system with a refinement suggestion."""
    
    print_section("INTEGRATION SYSTEM TEST")
    
    # Step 1: Get baseline predictions and errors
    print("Step 1: Computing baseline predictions...")
    engine = CalculationEngine()
    db = ExperimentalDatabase()
    validator = ValidationModule(db)
    analyzer = ErrorAnalyzer()
    
    predictions = engine.compute_all_predictions()
    validation_report = validator.validate_all(predictions)
    error_analysis = analyzer.analyze(validation_report)
    
    print(f"  ✓ Baseline: {validation_report.compared_predictions} predictions")
    print(f"  ✓ Mean σ-deviation: {validation_report.mean_sigma_deviation:.2f}")
    print(f"  ✓ Pass rate: {validation_report.overall_pass_rate * 100:.1f}%")
    
    # Step 2: Get refinement suggestions
    print_section("Step 2: Getting refinement suggestions...")
    advisor = AIAdvisor()
    suggestions = advisor.get_top_suggestions(error_analysis.to_dict(), n=3)
    
    if not suggestions:
        print("  ✗ No refinement suggestions generated")
        return 1
    
    print(f"  ✓ Generated {len(suggestions)} suggestions")
    print()
    
    # Select top suggestion
    top_suggestion = suggestions[0]
    mod = top_suggestion.modification
    
    print(f"Testing: {mod.name}")
    print(f"  Type: {mod.refinement_type.value}")
    print(f"  Confidence: {mod.confidence.value}")
    print(f"  Priority: {mod.priority_score:.2f}")
    print()
    
    # Step 3: Test refinement
    print_section("Step 3: Testing refinement in isolation...")
    integrator = IntegrationSystem()
    
    print("  Running integration tests...")
    print("  This includes:")
    print("    • Baseline computation")
    print("    • Refined computation (with modification)")
    print("    • Regression testing (check no predictions worsen)")
    print("    • Symmetry preservation checks")
    print("    • Topological origin verification")
    print()
    
    # The test_refinement method does all the validation
    result = integrator.test_refinement(top_suggestion)
    
    print(f"  Integration Status: {result.status.value}")
    print()
    
    # Step 4: Display results
    print_section("Step 4: Integration Test Results")
    
    print(f"Target Improved: {'YES' if result.target_improved else 'NO'}")
    if result.target_improved:
        print(f"  Improvement: {result.target_improvement_pct:.2f}%")
    print()
    
    print(f"Regression Tests:")
    print(f"  Total tests: {len(result.regression_tests)}")
    print(f"  Passed: {len([t for t in result.regression_tests if t.passed])}")
    print(f"  Failed: {result.regressions_found}")
    print()
    
    if result.regressions_found > 0:
        print("  Failed Tests:")
        for test in result.regression_tests:
            if not test.passed:
                print(f"    • {test.observable}: {test.baseline_sigma:.2f}σ → "
                      f"{test.refined_sigma:.2f}σ (worse by {-test.improvement:.2f}σ)")
        print()
    
    print(f"Symmetry Checks:")
    print(f"  Total checks: {len(result.symmetry_checks)}")
    print(f"  Preserved: {'YES' if result.symmetries_preserved else 'NO'}")
    if not result.symmetries_preserved:
        print("  Violations:")
        for check in result.symmetry_checks:
            if not check.preserved:
                print(f"    • {check.symmetry_name}: {check.details}")
    print()
    
    print(f"Topological Origin Verified: {'YES' if result.topological_origin_verified else 'NO'}")
    if result.topological_origin_verified:
        print(f"  Derivation: {result.topological_derivation[:60]}...")
    print()
    
    # Step 5: Decision
    print_section("Step 5: Integration Decision")
    
    if result.is_valid:
        print("✅ REFINEMENT VALIDATED")
        print()
        print("This refinement:")
        print(f"  • Improves target predictions by {result.target_improvement_pct:.2f}%")
        print(f"  • Passes all {len(result.regression_tests)} regression tests")
        print(f"  • Preserves all symmetries")
        print(f"  • Has clear topological origin (Directive A)")
        print()
        print("Recommendation: INTEGRATE into theory")
        print()
        print("Next steps:")
        print("  1. Create refinement notebook implementing the modification")
        print("  2. Update CalculationEngine with refined formulas")
        print("  3. Re-run full validation suite")
        print("  4. Update theory documentation (README.md)")
        print("  5. Document rationale in changelog")
    else:
        print("❌ REFINEMENT REJECTED")
        print()
        if result.rejection_reason:
            print(f"Reason: {result.rejection_reason.value}")
        print()
        print("Issues:")
        if not result.target_improved:
            print("  • Does not improve target predictions")
        if result.regressions_found > 0:
            print(f"  • Causes {result.regressions_found} regressions")
        if not result.symmetries_preserved:
            print("  • Violates fundamental symmetries")
        if not result.topological_origin_verified:
            print("  • Lacks clear topological derivation")
        print()
        print("Recommendation: DO NOT INTEGRATE")
        print()
        print("Next steps:")
        print("  1. Review refinement mathematical derivation")
        print("  2. Consider alternative topological modifications")
        print("  3. Analyze why this approach failed")
        print("  4. Generate new suggestions from AI Advisor")
    
    # Step 6: Export results
    print_section("Step 6: Export Results")
    
    output_dir = Path("outputs/evolution_system")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = output_dir / f"integration_test_{timestamp}.json"
    
    test_results = {
        "timestamp": timestamp,
        "suggestion": top_suggestion.to_dict(),
        "integration_result": result.to_dict(),
        "recommendation": "INTEGRATE" if result.is_valid else "REJECT"
    }
    
    with open(output_file, 'w') as f:
        json.dump(test_results, f, indent=2)
    
    print(f"✓ Results exported to: {output_file}")
    print()
    
    return 0 if result.is_valid else 1


if __name__ == "__main__":
    sys.exit(main())
