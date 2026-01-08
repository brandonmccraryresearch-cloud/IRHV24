"""
IRH Theory Evolution System
===========================

An AI-guided framework for continuously improving the Intrinsic Resonance Holography (IRH)
theoretical predictions through systematic error analysis and synoptic refinement.

**Status:** Phase 2 Infrastructure - AI Advisor Development

**Goal:** Enable the IRH framework to self-improve by learning from prediction errors and
automatically suggesting theoretical refinements based on topological and geometric principles.

Modules:
--------
- calculation_engine: Execute all IRH predictions with high precision
- experimental_database: Comprehensive database of CODATA, PDG, and Planck values
- validation_module: Compare theoretical predictions to experimental measurements
- error_analyzer: Identify systematic patterns in prediction errors
- ai_advisor: Generate topologically-motivated refinement suggestions

**Key Principle:** The system does NOT tune parameters to fit data. Instead, it suggests
*deeper topological structures* that could explain observed deviations.

Usage:
------
```python
from evolution_system import CalculationEngine, ValidationModule, ErrorAnalyzer, AIAdvisor

# Initialize components
engine = CalculationEngine()
validator = ValidationModule()
analyzer = ErrorAnalyzer()
advisor = AIAdvisor()

# Run evolution cycle
predictions = engine.compute_all_predictions()
validation_report = validator.validate_all(predictions)
error_analysis = analyzer.analyze(validation_report)

# Get AI-powered improvement suggestions
suggestions = advisor.get_top_suggestions(error_analysis, n=5)
report = advisor.generate_report(error_analysis)
print(report)
```

References:
-----------
- docs/THEORY_EVOLUTION_SYSTEM.md: Full design document
- notebooks/06_validation_suite.ipynb: Validation implementation
- verification/precision/constants.py: High-precision constant calculations
"""

__version__ = "0.2.0"
__author__ = "IRH Computational Research Team"
__all__ = [
    'CalculationEngine',
    'ExperimentalDatabase', 
    'ValidationModule',
    'ErrorAnalyzer',
    'AIAdvisor',
    'PredictionResult',
    'ValidationResult',
    'ErrorPattern',
    'RefinementSuggestion',
    'TopologicalModification',
]

from .calculation_engine import CalculationEngine, PredictionResult
from .experimental_database import ExperimentalDatabase
from .validation_module import ValidationModule, ValidationResult
from .error_analyzer import ErrorAnalyzer, ErrorPattern
from .ai_advisor import AIAdvisor, RefinementSuggestion, TopologicalModification
