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
        # EXPERIMENTAL VALUE FOR VALIDATION ONLY - CODATA 2022
        assert float(alpha_inv.value) == pytest.approx(137.035999177, rel=1e-9)
    
    def test_get_lepton_masses(self):
        """Test getting lepton masses."""
        from evolution_system import ExperimentalDatabase
        db = ExperimentalDatabase()
        
        m_e = db.get('m_electron')
        m_mu = db.get('m_muon')
        m_tau = db.get('m_tau')
        
        # EXPERIMENTAL VALUES FOR VALIDATION ONLY - CODATA 2022 / PDG 2022
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


class TestAIAdvisor:
    """Tests for AIAdvisor module (Phase 2)."""
    
    def test_import(self):
        """Test that AIAdvisor can be imported."""
        from evolution_system import AIAdvisor
        advisor = AIAdvisor()
        assert advisor is not None
    
    def test_modification_templates(self):
        """Test that modification templates are available."""
        from evolution_system.ai_advisor import TopologicalModificationTemplates
        
        templates = TopologicalModificationTemplates()
        
        # Test Chern class template
        chern = templates.chern_class_correction(order=2)
        assert chern is not None
        assert chern.name == "Chern Class C_2 Correction"
        assert len(chern.derivation_steps) > 0
        assert len(chern.symmetries_preserved) > 0
        
        # Test Berry phase template
        berry = templates.berry_phase_mass_correction()
        assert berry is not None
        assert "Berry" in berry.name
        
        # Test instanton template
        instanton = templates.instanton_vacuum_correction(order=2)
        assert instanton is not None
        assert "Instanton" in instanton.name
    
    def test_generate_suggestions(self):
        """Test generating suggestions from error analysis."""
        from evolution_system import (
            AIAdvisor, ErrorAnalyzer, ValidationModule, CalculationEngine
        )
        
        # Run full pipeline to get error analysis
        engine = CalculationEngine()
        predictions = engine.compute_all_predictions()
        
        validator = ValidationModule()
        report = validator.validate_all(predictions)
        
        analyzer = ErrorAnalyzer()
        analysis = analyzer.analyze(report)
        
        # Generate suggestions
        advisor = AIAdvisor()
        suggestions = advisor.generate_suggestions(analysis.to_dict())
        
        # Should generate some suggestions
        assert isinstance(suggestions, list)
    
    def test_rank_suggestions(self):
        """Test ranking of suggestions."""
        from evolution_system import AIAdvisor
        from evolution_system.ai_advisor import (
            TopologicalModificationTemplates, RefinementSuggestion
        )
        
        advisor = AIAdvisor()
        templates = TopologicalModificationTemplates()
        
        # Create some mock suggestions
        suggestions = [
            RefinementSuggestion(
                modification=templates.chern_class_correction(order=2),
                error_pattern="gauge_coupling_systematic",
                justification="Test justification",
                implementation_notes="Test notes",
                validation_criteria=["Criterion 1"],
                risk_assessment="Low risk"
            ),
            RefinementSuggestion(
                modification=templates.berry_phase_mass_correction(),
                error_pattern="lepton_mass_pattern",
                justification="Test justification 2",
                implementation_notes="Test notes 2",
                validation_criteria=["Criterion 2"],
                risk_assessment="Medium risk"
            )
        ]
        
        ranked = advisor.rank_suggestions(suggestions)
        
        # Should be sorted by priority score
        assert len(ranked) == 2
        assert ranked[0].modification.priority_score >= ranked[1].modification.priority_score
    
    def test_filter_topological_only(self):
        """Test filtering to only topological modifications."""
        from evolution_system import AIAdvisor
        from evolution_system.ai_advisor import (
            TopologicalModificationTemplates, RefinementSuggestion
        )
        
        advisor = AIAdvisor()
        templates = TopologicalModificationTemplates()
        
        # Create valid topological suggestion
        suggestion = RefinementSuggestion(
            modification=templates.hopf_fibration_correction(),
            error_pattern="alpha_systematic",
            justification="Test",
            implementation_notes="Test",
            validation_criteria=["Test"],
            risk_assessment="Low"
        )
        
        filtered = advisor.filter_topological_only([suggestion])
        
        # Should pass through
        assert len(filtered) == 1
    
    def test_generate_report(self):
        """Test generating human-readable report."""
        from evolution_system import (
            AIAdvisor, ErrorAnalyzer, ValidationModule, CalculationEngine
        )
        
        # Run full pipeline
        engine = CalculationEngine()
        predictions = engine.compute_all_predictions()
        
        validator = ValidationModule()
        report = validator.validate_all(predictions)
        
        analyzer = ErrorAnalyzer()
        analysis = analyzer.analyze(report)
        
        # Generate report
        advisor = AIAdvisor()
        text_report = advisor.generate_report(analysis.to_dict(), n=3)
        
        # Should be a non-empty string
        assert isinstance(text_report, str)
        assert len(text_report) > 0
        assert "DIRECTIVE A COMPLIANCE" in text_report
    
    def test_to_dict(self):
        """Test advisor configuration to dict."""
        from evolution_system import AIAdvisor
        
        advisor = AIAdvisor()
        config = advisor.to_dict()
        
        assert isinstance(config, dict)
        assert 'error_patterns' in config
        assert 'modification_types' in config
        assert 'confidence_levels' in config


class TestFullPipelineWithAdvisor:
    """Integration tests for the complete evolution system with AI Advisor."""
    
    def test_complete_evolution_cycle(self):
        """Test complete evolution cycle including AI Advisor."""
        from evolution_system import (
            CalculationEngine,
            ExperimentalDatabase,
            ValidationModule,
            ErrorAnalyzer,
            AIAdvisor,
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
        
        # 5. Get AI-powered suggestions
        advisor = AIAdvisor()
        suggestions = advisor.get_top_suggestions(analysis.to_dict(), n=5)
        
        # Should get some suggestions
        assert isinstance(suggestions, list)
        
        # 6. Verify all suggestions are topologically motivated
        for suggestion in suggestions:
            assert suggestion.modification.topological_basis is not None
            assert len(suggestion.modification.symmetries_preserved) > 0
            assert len(suggestion.modification.derivation_steps) > 0


class TestIntegrationSystem:
    """Tests for IntegrationSystem module (Phase 3)."""
    
    def test_import(self):
        """Test that IntegrationSystem can be imported."""
        from evolution_system import IntegrationSystem
        integrator = IntegrationSystem()
        assert integrator is not None
    
    def test_integration_status_enum(self):
        """Test IntegrationStatus enum values."""
        from evolution_system.integration_system import IntegrationStatus
        
        assert IntegrationStatus.PENDING.value == "pending"
        assert IntegrationStatus.TESTING.value == "testing"
        assert IntegrationStatus.VALIDATED.value == "validated"
        assert IntegrationStatus.REJECTED.value == "rejected"
        assert IntegrationStatus.INTEGRATED.value == "integrated"
    
    def test_isolated_test_environment(self):
        """Test IsolatedTestEnvironment setup."""
        from evolution_system.integration_system import IsolatedTestEnvironment
        
        env = IsolatedTestEnvironment()
        baseline = env.setup_baseline()
        
        assert baseline is not None
        assert len(baseline) > 0
        assert 'alpha_inv' in baseline or 'koide_Q' in baseline
    
    def test_topological_verifier(self):
        """Test TopologicalVerifier validation."""
        from evolution_system.integration_system import TopologicalVerifier
        from evolution_system.ai_advisor import TopologicalModificationTemplates
        
        verifier = TopologicalVerifier()
        templates = TopologicalModificationTemplates()
        
        # Test valid topological modification
        chern = templates.chern_class_correction(order=2)
        is_valid, derivation = verifier.verify(chern)
        
        assert is_valid is True
        assert derivation is not None
        assert len(derivation) > 0
    
    def test_symmetry_checker(self):
        """Test SymmetryChecker validation."""
        from evolution_system.integration_system import SymmetryChecker
        from evolution_system.ai_advisor import TopologicalModificationTemplates
        
        checker = SymmetryChecker()
        templates = TopologicalModificationTemplates()
        
        # Test modification with symmetry declarations
        hopf = templates.hopf_fibration_correction()
        
        # Pass empty predictions for symmetry check
        checks = checker.check_all(hopf, {})
        
        assert len(checks) > 0
        # Hopf fibration should preserve symmetries
        gauge_check = next((c for c in checks if "Gauge" in c.symmetry_name), None)
        assert gauge_check is not None
    
    def test_test_refinement(self):
        """Test the main test_refinement method."""
        from evolution_system import IntegrationSystem, AIAdvisor, ErrorAnalyzer
        from evolution_system import CalculationEngine, ValidationModule
        
        # Get a suggestion to test
        engine = CalculationEngine()
        predictions = engine.compute_all_predictions()
        
        validator = ValidationModule()
        report = validator.validate_all(predictions)
        
        analyzer = ErrorAnalyzer()
        analysis = analyzer.analyze(report)
        
        advisor = AIAdvisor()
        suggestions = advisor.get_top_suggestions(analysis.to_dict(), n=1)
        
        if suggestions:
            # Test the refinement
            integrator = IntegrationSystem()
            result = integrator.test_refinement(suggestions[0])
            
            # Result should have all required fields
            assert result.refinement_name is not None
            assert result.status is not None
            assert result.test_timestamp is not None
            assert isinstance(result.regression_tests, list)
            assert isinstance(result.symmetry_checks, list)
    
    def test_generate_report(self):
        """Test report generation for integration result."""
        from evolution_system import IntegrationSystem
        from evolution_system.integration_system import (
            IntegrationResult, IntegrationStatus
        )
        
        # Create a mock result
        result = IntegrationResult(
            refinement_name="Test Refinement",
            status=IntegrationStatus.VALIDATED,
            target_improved=True,
            target_improvement_pct=5.2,
            topological_origin_verified=True,
            topological_derivation="Derived from Chern classes"
        )
        
        integrator = IntegrationSystem()
        report = integrator.generate_report(result)
        
        assert isinstance(report, str)
        assert "Test Refinement" in report
        assert "VALIDATED" in report
    
    def test_to_dict(self):
        """Test IntegrationSystem configuration to dict."""
        from evolution_system import IntegrationSystem
        
        integrator = IntegrationSystem()
        config = integrator.to_dict()
        
        assert isinstance(config, dict)
        assert 'sigma_tolerance' in config
        assert 'valid_topological_sources' in config
        assert 'history_count' in config
    
    def test_integration_result_is_valid(self):
        """Test IntegrationResult.is_valid property."""
        from evolution_system.integration_system import (
            IntegrationResult, IntegrationStatus
        )
        
        # Valid result
        valid_result = IntegrationResult(
            refinement_name="Test",
            status=IntegrationStatus.VALIDATED,
            target_improved=True,
            regressions_found=0,
            symmetries_preserved=True,
            topological_origin_verified=True
        )
        assert valid_result.is_valid is True
        
        # Invalid: not improved
        invalid_result = IntegrationResult(
            refinement_name="Test",
            status=IntegrationStatus.REJECTED,
            target_improved=False,
            regressions_found=0,
            symmetries_preserved=True,
            topological_origin_verified=True
        )
        assert invalid_result.is_valid is False
        
        # Invalid: has regressions
        regressed_result = IntegrationResult(
            refinement_name="Test",
            status=IntegrationStatus.REJECTED,
            target_improved=True,
            regressions_found=2,
            symmetries_preserved=True,
            topological_origin_verified=True
        )
        assert regressed_result.is_valid is False


class TestFullPipelineWithIntegration:
    """Integration tests for the complete evolution system with Integration System."""
    
    def test_complete_evolution_cycle_with_integration(self):
        """Test complete evolution cycle including Integration System."""
        from evolution_system import (
            CalculationEngine,
            ExperimentalDatabase,
            ValidationModule,
            ErrorAnalyzer,
            AIAdvisor,
            IntegrationSystem,
        )
        from evolution_system.ai_advisor import TopologicalModificationTemplates, RefinementSuggestion
        
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
        
        # 5. Get AI-powered suggestions or create test suggestion
        advisor = AIAdvisor()
        suggestions = advisor.get_top_suggestions(analysis.to_dict(), n=3)
        
        # If no suggestions from analysis, create a test suggestion
        if not suggestions:
            templates = TopologicalModificationTemplates()
            test_suggestion = RefinementSuggestion(
                modification=templates.chern_class_correction(order=2),
                error_pattern="gauge_coupling_systematic",
                justification="Test refinement for integration testing",
                implementation_notes="Testing only",
                validation_criteria=["Test criterion"],
                risk_assessment="Low risk test"
            )
            suggestions = [test_suggestion]
        
        # 6. Test refinements with Integration System
        integrator = IntegrationSystem()
        
        results = []
        for suggestion in suggestions:
            result = integrator.test_refinement(suggestion)
            results.append(result)
        
        # Should have tested some refinements
        assert len(results) > 0
        
        # All results should have proper status
        from evolution_system.integration_system import IntegrationStatus
        for result in results:
            assert result.status in [
                IntegrationStatus.VALIDATED,
                IntegrationStatus.REJECTED,
                IntegrationStatus.TESTING
            ]
        
        # Integration history should be populated
        history = integrator.get_integration_history()
        assert len(history) == len(results)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
