# IRH Theory Evolution System

An AI-guided framework for continuously improving the Intrinsic Resonance Holography (IRH) theoretical predictions through systematic error analysis and synoptic refinement.

## Overview

The Theory Evolution System enables the IRH framework to self-improve by:
1. Computing all theoretical predictions from topological invariants
2. Validating predictions against experimental measurements
3. Analyzing error patterns to identify systematic discrepancies
4. Suggesting topologically-motivated refinements (no phenomenological fitting)

## Installation

```bash
# From repository root
pip install -e .

# Or install dependencies manually
pip install mpmath numpy
```

## Quick Start

```python
from evolution_system import (
    CalculationEngine,
    ExperimentalDatabase,
    ValidationModule,
    ErrorAnalyzer
)

# 1. Load experimental database
db = ExperimentalDatabase()
print(f"Loaded {db.count()} experimental constants")

# 2. Compute all theoretical predictions
engine = CalculationEngine()
predictions = engine.compute_all_predictions()
engine.print_summary()

# 3. Validate against experiments
validator = ValidationModule(db)
report = validator.validate_all(predictions)
validator.print_validation_report(report)

# 4. Analyze error patterns
analyzer = ErrorAnalyzer()
analysis = analyzer.analyze(report)
analyzer.print_analysis(analysis)

# 5. Get refinement suggestions
suggestions = analysis.get_high_priority_suggestions(n=5)
for s in suggestions:
    print(f"Suggestion: {s.title}")
    print(f"  {s.description}")
```

## Modules

### ExperimentalDatabase

Comprehensive database of experimental values from:
- **CODATA 2022**: Fundamental physical constants
- **PDG 2022**: Particle physics properties
- **Planck 2018**: Cosmological parameters

```python
from evolution_system import ExperimentalDatabase

db = ExperimentalDatabase()

# Get specific constant
alpha = db.get('alpha_inv')
print(f"α⁻¹ = {alpha.value} ± {alpha.uncertainty}")

# Get by tier
tier1 = db.get_tier(1)  # Core parameters

# Get by category
leptons = db.get_category('lepton_masses')
```

**Important:** All experimental values are marked "FOR VALIDATION ONLY" per Directive A.

### CalculationEngine

Computes theoretical predictions from topological invariants.

```python
from evolution_system import CalculationEngine

engine = CalculationEngine()

# Compute individual predictions
alpha = engine.compute_fine_structure_constant()
eta = engine.compute_metric_mismatch()
koide = engine.compute_koide_formula()

# Compute all predictions
predictions = engine.compute_all_predictions()
```

**Current Predictions:**
- α⁻¹ (fine-structure constant)
- η (metric mismatch = 4/π)
- Q (Koide ratio = 2/3)
- α_s, α₁, α₂ (gauge couplings)
- sin²θ_W (weak mixing angle)
- M_X (GUT scale)
- ΩΛ, ΩDM, Ωb (cosmological ratios)

### ValidationModule

Compares theoretical predictions to experimental measurements.

```python
from evolution_system import ValidationModule, CalculationEngine

engine = CalculationEngine()
predictions = engine.compute_all_predictions()

validator = ValidationModule()
report = validator.validate_all(predictions)

# Check results
print(f"Excellent: {report.excellent_count}")  # Within 1σ
print(f"Good: {report.good_count}")            # 1-3σ
print(f"Fair: {report.fair_count}")            # 3-5σ
print(f"Poor: {report.poor_count}")            # >5σ

# Get discrepant predictions
discrepant = report.get_discrepant(sigma_threshold=3.0)
```

### ErrorAnalyzer

Identifies systematic error patterns and suggests refinements.

```python
from evolution_system import ErrorAnalyzer

analyzer = ErrorAnalyzer()
analysis = analyzer.analyze(report)

# View patterns
for pattern in analysis.patterns:
    print(f"{pattern.severity.value}: {pattern.description}")

# Get suggestions
for suggestion in analysis.suggestions:
    print(f"Suggestion: {suggestion.title}")
    print(f"  Topological origin: {suggestion.topological_origin}")
```

**Pattern Types:**
- Systematic offset (predictions all too high/low)
- Scale-dependent (errors vary with energy)
- Sector-specific (e.g., gauge sector issues)
- Individual outliers (>3σ discrepancies)

## Directive Compliance

This system strictly adheres to IRH Directives:

### Directive A: No-Tuning Constraint
- All constants derived from topological invariants
- Experimental values ONLY for validation, never as inputs
- No phenomenological fitting or parameter adjustment

### Directive B: CODATA Precision
- All calculations use arbitrary precision (mpmath)
- Comparisons include σ-deviations and relative errors
- Results compared to latest CODATA 2022 values

### Directive C: Rigorous Formalism
- Forces described as "curvature in connections"
- Particles as "B₃ resonant modes"
- Standard gauge theory terminology

## Tests

Run the test suite:

```bash
cd /path/to/IRHV24
python -m pytest tests/test_evolution_system.py -v
```

## Design Document

See [docs/THEORY_EVOLUTION_SYSTEM.md](../docs/THEORY_EVOLUTION_SYSTEM.md) for the full design specification.

## Status

**Phase 1: Infrastructure** - In Development
- [x] Experimental database
- [x] Calculation engine
- [x] Validation module
- [x] Error analyzer
- [ ] Full Standard Model coverage

**Future Phases:**
- Phase 2: AI Advisor Development
- Phase 3: Integration System
- Phase 4: Full System Operation
