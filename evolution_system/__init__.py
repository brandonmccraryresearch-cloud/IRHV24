"""
IRH Theory Evolution System
===========================

An AI-guided framework for continuously improving the Intrinsic Resonance Holography (IRH)
theoretical predictions through systematic error analysis and synoptic refinement.

**Status:** Phase 1 Infrastructure - Development

**Goal:** Enable the IRH framework to self-improve by learning from prediction errors and
automatically suggesting theoretical refinements based on topological and geometric principles.

Modules:
--------
- calculation_engine: Execute all IRH predictions with high precision
- experimental_database: Comprehensive database of CODATA, PDG, and Planck values
- validation_module: Compare theoretical predictions to experimental measurements
- error_analyzer: Identify systematic patterns in prediction errors

**Key Principle:** The system does NOT tune parameters to fit data. Instead, it suggests
*deeper topological structures* that could explain observed deviations.

Usage:
------
```python
from evolution_system import CalculationEngine, ValidationModule, ErrorAnalyzer

# Initialize components
engine = CalculationEngine()
validator = ValidationModule()
analyzer = ErrorAnalyzer()

# Run evolution cycle
predictions = engine.compute_all_predictions()
validation_report = validator.validate_all(predictions)
error_patterns = analyzer.analyze(validation_report)

# Get improvement suggestions (future: AI Advisor)
suggestions = analyzer.suggest_refinements(error_patterns)
```

References:
-----------
- docs/THEORY_EVOLUTION_SYSTEM.md: Full design document
- notebooks/06_validation_suite.ipynb: Validation implementation
- verification/precision/constants.py: High-precision constant calculations
"""

__version__ = "0.1.0"
__author__ = "IRH Computational Research Team"
__all__ = [
    'CalculationEngine',
    'ExperimentalDatabase', 
    'ValidationModule',
    'ErrorAnalyzer',
    'PredictionResult',
    'ValidationResult',
    'ErrorPattern',
]

from .calculation_engine import CalculationEngine, PredictionResult
from .experimental_database import ExperimentalDatabase
from .validation_module import ValidationModule, ValidationResult
from .error_analyzer import ErrorAnalyzer, ErrorPattern
