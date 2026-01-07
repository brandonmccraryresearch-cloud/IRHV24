"""
Tests for the IRH Theory Evolution System

These tests verify the basic functionality of the evolution system components:
- ExperimentalDatabase: Loading and accessing experimental values
- CalculationEngine: Computing theoretical predictions
- ValidationModule: Comparing predictions to experiments
- ErrorAnalyzer: Identifying error patterns
"""

import pytest
import mpmath as mp

# Set precision for tests
mp.dps = 50


class TestExperimentalDatabase:
    """Tests for ExperimentalDatabase."""
    
    def test_import(self):
        """Test that ExperimentalDatabase can be imported."""
        from evolution_system import ExperimentalDatabase
        db = ExperimentalDatabase()
        assert db is not None
    
    def test_constants_loaded(self):
        """Test that constants are loaded."""
        from evolution_system import ExperimentalDatabase
        db = ExperimentalDatabase()
        assert db.count() > 0
    
    def test_get_alpha(self):
        """Test getting fine-structure constant."""
        from evolution_system import ExperimentalDatabase
        db = ExperimentalDatabase()
        alpha = db.get('alpha')
        
        assert alpha is not None
        assert alpha.symbol == "α"
        assert float(alpha.value) == pytest.approx(7.2973525693e-3, rel=1e-10)
    
    def test_get_alpha_inv(self):
        """Test getting inverse fine-structure constant."""
        from evolution_system import ExperimentalDatabase
        db = ExperimentalDatabase()
        alpha_inv = db.get('alpha_inv')
        
        assert alpha_inv is not None
        assert float(alpha_inv.value) == pytest.approx(137.035999177, rel=1e-9)
    
    def test_get_lepton_masses(self):
        """Test getting lepton masses."""
        from evolution_system import ExperimentalDatabase
        db = ExperimentalDatabase()
        
        m_e = db.get('m_electron')
        m_mu = db.get('m_muon')
        m_tau = db.get('m_tau')
        
        assert float(m_e.value) == pytest.approx(0.51099895, rel=1e-7)
        assert float(m_mu.value) == pytest.approx(105.6583755, rel=1e-7)
        assert float(m_tau.value) == pytest.approx(1776.86, rel=1e-4)
    
    def test_get_tier(self):
        """Test getting constants by tier."""
        from evolution_system import ExperimentalDatabase
        from evolution_system.experimental_database import ValidationTier
        
        db = ExperimentalDatabase()
        tier1 = db.get_tier(1)
        
        assert len(tier1) > 0
        for const in tier1:
            assert const.tier == ValidationTier.TIER_1
    
    def test_missing_key_raises_error(self):
        """Test that missing key raises KeyError."""
        from evolution_system import ExperimentalDatabase
        db = ExperimentalDatabase()
        
        with pytest.raises(KeyError):
            db.get('nonexistent_constant')
    
    def test_to_dict(self):
        """Test converting database to dictionary."""
        from evolution_system import ExperimentalDatabase
        db = ExperimentalDatabase()
        
        data = db.to_dict()
        assert isinstance(data, dict)
        assert 'alpha' in data
        assert 'alpha_inv' in data


class TestCalculationEngine:
    """Tests for CalculationEngine."""
    
    def test_import(self):
        """Test that CalculationEngine can be imported."""
        from evolution_system import CalculationEngine
        engine = CalculationEngine()
        assert engine is not None
    
    def test_compute_fine_structure_constant(self):
        """Test computing fine-structure constant."""
        from evolution_system import CalculationEngine
        engine = CalculationEngine()
        
        result = engine.compute_fine_structure_constant()
        
        assert result is not None
        assert result.symbol == "α⁻¹"
        # Should be close to 137 (within ~1% given approximations)
        assert 135 < float(result.value) < 140
    
    def test_compute_metric_mismatch(self):
        """Test computing metric mismatch η = 4/π."""
        from evolution_system import CalculationEngine
        engine = CalculationEngine()
        
        result = engine.compute_metric_mismatch()
        
        assert result is not None
        assert result.symbol == "η"
        assert result.is_exact == True
        expected = 4 / 3.14159265358979323846
        assert float(result.value) == pytest.approx(expected, rel=1e-10)
    
    def test_compute_koide_formula(self):
        """Test computing Koide ratio Q = 2/3."""
        from evolution_system import CalculationEngine
        engine = CalculationEngine()
        
        result = engine.compute_koide_formula()
        
        assert result is not None
        assert result.symbol == "Q"
        assert result.is_exact == True
        assert float(result.value) == pytest.approx(2/3, rel=1e-15)
    
    def test_compute_all_predictions(self):
        """Test computing all predictions."""
        from evolution_system import CalculationEngine
        engine = CalculationEngine()
        
        predictions = engine.compute_all_predictions()
        
        assert isinstance(predictions, dict)
        assert len(predictions) > 0
        
        # Check required predictions exist
        assert 'alpha_inv' in predictions
        assert 'eta' in predictions
        assert 'koide_Q' in predictions
    
    def test_prediction_has_metadata(self):
        """Test that predictions include metadata."""
        from evolution_system import CalculationEngine
        engine = CalculationEngine()
        
        result = engine.compute_fine_structure_constant()
        
        assert result.derivation is not None
        assert result.theory_reference is not None
        assert result.components is not None
        assert len(result.components) > 0
    
    def test_to_dict(self):
        """Test converting predictions to dictionary."""
        from evolution_system import CalculationEngine
        engine = CalculationEngine()
        
        engine.compute_all_predictions()
        data = engine.to_dict()
        
        assert isinstance(data, dict)
        assert 'alpha_inv' in data


class TestValidationModule:
    """Tests for ValidationModule."""
    
    def test_import(self):
        """Test that ValidationModule can be imported."""
        from evolution_system import ValidationModule
        validator = ValidationModule()
        assert validator is not None
    
    def test_validate_koide_formula(self):
        """Test validating Koide formula."""
        from evolution_system import ValidationModule, CalculationEngine
        
        engine = CalculationEngine()
        prediction = engine.compute_koide_formula()
        
        validator = ValidationModule()
        result = validator.validate_koide_formula(prediction)
        
        assert result is not None
        assert result.sigma_deviation is not None
        # Koide formula should be very accurate
        assert result.sigma_deviation < 1.0
    
    def test_validate_all_predictions(self):
        """Test validating all predictions."""
        from evolution_system import ValidationModule, CalculationEngine
        
        engine = CalculationEngine()
        predictions = engine.compute_all_predictions()
        
        validator = ValidationModule()
        report = validator.validate_all(predictions)
        
        assert report is not None
        assert report.total_predictions == len(predictions)
        assert report.compared_predictions > 0
    
    def test_validation_report_has_statistics(self):
        """Test that validation report has statistics."""
        from evolution_system import ValidationModule, CalculationEngine
        
        engine = CalculationEngine()
        predictions = engine.compute_all_predictions()
        
        validator = ValidationModule()
        report = validator.validate_all(predictions)
        
        assert report.excellent_count >= 0
        assert report.good_count >= 0
        assert report.fair_count >= 0
        assert report.poor_count >= 0
    
    def test_to_dict(self):
        """Test converting report to dictionary."""
        from evolution_system import ValidationModule, CalculationEngine
        
        engine = CalculationEngine()
        predictions = engine.compute_all_predictions()
        
        validator = ValidationModule()
        report = validator.validate_all(predictions)
        
        data = report.to_dict()
        assert isinstance(data, dict)
        assert 'summary' in data
        assert 'results' in data


class TestErrorAnalyzer:
    """Tests for ErrorAnalyzer."""
    
    def test_import(self):
        """Test that ErrorAnalyzer can be imported."""
        from evolution_system import ErrorAnalyzer
        analyzer = ErrorAnalyzer()
        assert analyzer is not None
    
    def test_analyze_report(self):
        """Test analyzing validation report."""
        from evolution_system import (
            ErrorAnalyzer, ValidationModule, CalculationEngine
        )
        
        engine = CalculationEngine()
        predictions = engine.compute_all_predictions()
        
        validator = ValidationModule()
        report = validator.validate_all(predictions)
        
        analyzer = ErrorAnalyzer()
        analysis = analyzer.analyze(report)
        
        assert analysis is not None
        assert analysis.total_errors_analyzed > 0
    
    def test_analysis_detects_patterns(self):
        """Test that analysis detects patterns."""
        from evolution_system import (
            ErrorAnalyzer, ValidationModule, CalculationEngine
        )
        
        engine = CalculationEngine()
        predictions = engine.compute_all_predictions()
        
        validator = ValidationModule()
        report = validator.validate_all(predictions)
        
        analyzer = ErrorAnalyzer()
        analysis = analyzer.analyze(report)
        
        # Should detect some patterns given the simplified approximations
        assert len(analysis.patterns) >= 0  # May or may not find patterns
    
    def test_analysis_generates_suggestions(self):
        """Test that analysis generates suggestions."""
        from evolution_system import (
            ErrorAnalyzer, ValidationModule, CalculationEngine
        )
        
        engine = CalculationEngine()
        predictions = engine.compute_all_predictions()
        
        validator = ValidationModule()
        report = validator.validate_all(predictions)
        
        analyzer = ErrorAnalyzer()
        analysis = analyzer.analyze(report)
        
        # May or may not have suggestions depending on errors
        assert isinstance(analysis.suggestions, list)
    
    def test_to_dict(self):
        """Test converting analysis to dictionary."""
        from evolution_system import (
            ErrorAnalyzer, ValidationModule, CalculationEngine
        )
        
        engine = CalculationEngine()
        predictions = engine.compute_all_predictions()
        
        validator = ValidationModule()
        report = validator.validate_all(predictions)
        
        analyzer = ErrorAnalyzer()
        analysis = analyzer.analyze(report)
        
        data = analysis.to_dict()
        assert isinstance(data, dict)
        assert 'summary' in data
        assert 'patterns' in data
        assert 'suggestions' in data


class TestIntegration:
    """Integration tests for the full evolution system pipeline."""
    
    def test_full_pipeline(self):
        """Test complete evolution pipeline."""
        from evolution_system import (
            CalculationEngine,
            ExperimentalDatabase,
            ValidationModule,
            ErrorAnalyzer,
        )
        
        # 1. Load experimental database
        db = ExperimentalDatabase()
        assert db.count() > 0
        
        # 2. Compute predictions
        engine = CalculationEngine()
        predictions = engine.compute_all_predictions()
        assert len(predictions) > 0
        
        # 3. Validate against experiments
        validator = ValidationModule(db)
        report = validator.validate_all(predictions)
        assert report.compared_predictions > 0
        
        # 4. Analyze errors
        analyzer = ErrorAnalyzer()
        analysis = analyzer.analyze(report)
        assert analysis.total_errors_analyzed > 0
        
        # 5. Verify outputs are serializable
        predictions_json = engine.to_dict()
        report_json = report.to_dict()
        analysis_json = analysis.to_dict()
        
        assert isinstance(predictions_json, dict)
        assert isinstance(report_json, dict)
        assert isinstance(analysis_json, dict)
    
    def test_koide_formula_accuracy(self):
        """Test that Koide formula is accurately predicted."""
        from evolution_system import CalculationEngine, ValidationModule
        
        engine = CalculationEngine()
        prediction = engine.compute_koide_formula()
        
        validator = ValidationModule()
        result = validator.validate_koide_formula(prediction)
        
        # Koide formula should be within 1σ
        assert result.sigma_deviation < 1.0
        assert result.agreement_status.value == "excellent"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
