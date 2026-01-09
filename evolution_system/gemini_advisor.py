#!/usr/bin/env python3
"""
Enhanced AI Advisor with Gemini Integration

This module extends the AI Advisor with Google Gemini AI to generate
more sophisticated refinement suggestions based on error patterns.

The Gemini model is used to:
1. Analyze complex error patterns
2. Suggest novel topological modifications
3. Identify subtle correlations
4. Generate mathematical derivations
5. Rank suggestions by theoretical soundness

All suggestions must still follow Directive A (topological origin only).

Author: IRH Computational Research Team
Date: 2026-01-09
"""

import os
import json
from typing import Dict, List, Optional
from dataclasses import dataclass

try:
    from google import genai
    from google.genai import types
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    print("Warning: Google GenAI SDK not available. Gemini features disabled.")


@dataclass
class GeminiConfig:
    """Configuration for Gemini AI integration."""
    model_name: str = "gemini-2.0-flash-exp"
    temperature: float = 0.3  # Lower for more deterministic physics
    top_p: float = 0.95
    max_output_tokens: int = 8192
    
    # Physics-specific configuration
    enforce_topological_origin: bool = True
    require_mathematical_derivation: bool = True
    filter_phenomenological: bool = True


class GeminiAIAdvisor:
    """
    Enhanced AI Advisor using Google Gemini for sophisticated error analysis
    and refinement suggestions.
    
    This advisor wraps the existing AIAdvisor with additional Gemini-powered
    capabilities for deeper analysis and novel suggestion generation.
    """
    
    def __init__(self, config: Optional[GeminiConfig] = None):
        """
        Initialize Gemini AI Advisor.
        
        Args:
            config: GeminiConfig object (uses defaults if None)
        """
        self.config = config or GeminiConfig()
        self.gemini_available = GEMINI_AVAILABLE
        self.client = None
        
        # Initialize Gemini client if API key available
        api_key = os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')
        if api_key and self.gemini_available:
            try:
                self.client = genai.Client(api_key=api_key)
                print(f"✓ Gemini AI initialized: {self.config.model_name}")
            except Exception as e:
                print(f"Warning: Failed to initialize Gemini: {e}")
                self.client = None
        elif not api_key:
            print("ℹ GEMINI_API_KEY or GOOGLE_API_KEY not found in environment.")
            print("  Gemini features disabled - using template-based suggestions.")
            print("  To enable Gemini: export GEMINI_API_KEY='your-api-key'")
        
        # Load IRH theory context for Gemini prompts
        self.theory_context = self._load_theory_context()
    
    def _load_theory_context(self) -> str:
        """
        Load IRH theory context for Gemini prompts.
        
        This provides the AI with essential background about the IRH framework,
        ensuring suggestions are theory-consistent.
        """
        context = """
        IRH (Intrinsic Resonance Holography) Theoretical Framework:
        
        Core Principles:
        1. 4-strand resonance network substrate (N=4 topologically protected)
        2. Metric mismatch η = 4/π from 4D→3D projection
        3. All physical constants derived from topological invariants
        4. No free parameters (Directive A: NO phenomenological tuning)
        
        Key Topological Structures:
        - Hopf fibrations: S³→S², S⁷→S⁴, S¹⁵→S⁸
        - 24-cell polytope (F₄ root system)
        - Artin braid group B₃ (SU(3) color charge)
        - Chern classes and characteristic classes
        - Weyl anomaly from conformal breaking
        
        Validated Predictions:
        - Fine-structure constant α⁻¹ ≈ 137.036 (from Hopf volumes + 24-cell)
        - Koide ratio Q = 2/3 (exact, from circulant eigenvalues)
        - Metric mismatch η = 4/π (exact, from dimensional reduction)
        - Gauge couplings α₁, α₂, α₃ (from Braid group representations)
        - Cosmological constant Λ (from instanton suppression)
        
        Available Topological Corrections:
        1. Chern class corrections (C₁, C₂, C₃)
        2. Berry phase corrections (geometric phases)
        3. Instanton corrections (topological vacua)
        4. Hopf fibration hierarchy (higher spheres)
        5. Braid group corrections (higher strands)
        6. Euler characteristic corrections (χ(M))
        7. Weyl anomaly corrections (conformal breaking)
        8. Holonomy corrections (parallel transport)
        9. Volume ratio corrections (sphere volumes)
        10. Winding number corrections (homotopy groups)
        
        CRITICAL CONSTRAINT (Directive A):
        All suggestions MUST have clear topological/geometric origin.
        NO phenomenological fitting, NO adjustable parameters.
        Every constant must trace to Hopf fibrations, Chern classes,
        Braid groups, or other topological invariants.
        """
        return context
    
    def analyze_error_patterns_with_gemini(self, error_analysis: Dict) -> Dict:
        """
        Use Gemini to perform deep analysis of error patterns.
        
        Args:
            error_analysis: Output from ErrorAnalyzer
            
        Returns:
            Enhanced analysis with Gemini insights
        """
        if not self.client:
            return {
                "gemini_available": False,
                "analysis": "Gemini not available - using template-based analysis"
            }
        
        # Build prompt for Gemini
        prompt = self._build_error_analysis_prompt(error_analysis)
        
        try:
            # Call Gemini API
            response = self.client.models.generate_content(
                model=self.config.model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=self.config.temperature,
                    top_p=self.config.top_p,
                    max_output_tokens=self.config.max_output_tokens,
                )
            )
            
            # Parse response
            analysis_text = response.text
            
            return {
                "gemini_available": True,
                "model": self.config.model_name,
                "analysis": analysis_text,
                "insights": self._extract_insights(analysis_text)
            }
            
        except Exception as e:
            return {
                "gemini_available": False,
                "error": str(e),
                "analysis": "Gemini call failed - falling back to templates"
            }
    
    def generate_refinement_suggestions_with_gemini(self, 
                                                     error_analysis: Dict,
                                                     n_suggestions: int = 5) -> List[Dict]:
        """
        Use Gemini to generate novel refinement suggestions.
        
        Args:
            error_analysis: Output from ErrorAnalyzer
            n_suggestions: Number of suggestions to generate
            
        Returns:
            List of refinement suggestions with full mathematical details
        """
        if not self.client:
            return []
        
        # Build prompt for suggestion generation
        prompt = self._build_suggestion_prompt(error_analysis, n_suggestions)
        
        try:
            # Call Gemini API
            response = self.client.models.generate_content(
                model=self.config.model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=self.config.temperature,
                    top_p=self.config.top_p,
                    max_output_tokens=self.config.max_output_tokens,
                )
            )
            
            # Parse suggestions from response
            suggestions_text = response.text
            suggestions = self._parse_suggestions(suggestions_text)
            
            return suggestions
            
        except Exception as e:
            print(f"Warning: Gemini suggestion generation failed: {e}")
            return []
    
    def _build_error_analysis_prompt(self, error_analysis: Dict) -> str:
        """Build prompt for Gemini error pattern analysis."""
        
        patterns_summary = json.dumps(error_analysis.get('patterns', []), indent=2)
        summary = error_analysis.get('summary', {})
        
        prompt = f"""
{self.theory_context}

TASK: Analyze error patterns in IRH theoretical predictions

ERROR ANALYSIS DATA:
{json.dumps(summary, indent=2)}

DETECTED PATTERNS:
{patterns_summary}

INSTRUCTIONS:
1. Identify the root causes of discrepancies
2. Look for correlations between error patterns
3. Suggest which topological structures might be missing
4. Prioritize by theoretical naturalness
5. Consider systematic vs random errors
6. Check if errors suggest higher-order corrections

Provide your analysis in clear, structured format focusing on:
- Most critical discrepancies
- Likely topological origins of errors
- Suggested correction types (Chern, Berry, Instanton, etc.)
- Expected improvement magnitude

Remember: All suggestions must have topological origin (Directive A).
NO phenomenological fitting allowed.
"""
        return prompt
    
    def _build_suggestion_prompt(self, error_analysis: Dict, n: int) -> str:
        """Build prompt for Gemini refinement suggestion generation."""
        
        patterns_summary = json.dumps(error_analysis.get('patterns', [])[:5], indent=2)
        
        prompt = f"""
{self.theory_context}

TASK: Generate {n} topologically-motivated refinement suggestions

ERROR PATTERNS TO ADDRESS:
{patterns_summary}

INSTRUCTIONS:
Generate {n} refinement suggestions following this EXACT JSON format:

[
  {{
    "name": "Descriptive name of refinement",
    "refinement_type": "chern_class|berry_phase|instanton|hopf_fibration|braid_group|other",
    "mathematical_formula": "Precise mathematical expression",
    "topological_basis": "Detailed explanation of topological origin",
    "affected_observables": ["list", "of", "affected", "observables"],
    "expected_improvement": "Quantitative description of expected improvement",
    "derivation_steps": ["Step 1", "Step 2", "Step 3", ...],
    "symmetries_preserved": ["Gauge invariance", "Lorentz symmetry", ...],
    "confidence": "high|medium|low",
    "priority_score": 0-100
  }},
  ...
]

CRITICAL REQUIREMENTS (Directive A):
1. Every refinement MUST have clear topological/geometric origin
2. NO phenomenological parameters (no fitting to data)
3. All constants from Hopf fibrations, Chern classes, Braid groups, etc.
4. Must preserve fundamental symmetries
5. Must have testable predictions

Focus on:
- Gauge sector errors → Chern class corrections
- Mass predictions → Berry phase, Hopf fibration corrections  
- Cosmological errors → Instanton corrections
- Fine-structure constant → Higher-order Hopf volumes

Output ONLY valid JSON, no additional text.
"""
        return prompt
    
    def _extract_insights(self, analysis_text: str) -> List[str]:
        """Extract key insights from Gemini analysis."""
        insights = []
        
        # Simple extraction - look for bullet points or numbered lists
        lines = analysis_text.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('-') or line.startswith('•') or line[0:2].replace('.', '').isdigit():
                insights.append(line.lstrip('-•0123456789. '))
        
        return insights[:10]  # Return top 10 insights
    
    def _parse_suggestions(self, suggestions_text: str) -> List[Dict]:
        """Parse JSON suggestions from Gemini response."""
        try:
            # Try to extract JSON from response
            # Handle cases where Gemini adds markdown code blocks
            text = suggestions_text.strip()
            
            # Remove markdown code blocks if present
            if text.startswith('```'):
                lines = text.split('\n')
                text = '\n'.join(lines[1:-1] if lines[-1].strip() == '```' else lines[1:])
                text = text.replace('```json', '').replace('```', '')
            
            # Parse JSON
            suggestions = json.loads(text)
            
            # Validate that it's a list
            if not isinstance(suggestions, list):
                suggestions = [suggestions]
            
            return suggestions
            
        except json.JSONDecodeError as e:
            print(f"Warning: Failed to parse Gemini suggestions as JSON: {e}")
            print(f"Response text: {suggestions_text[:200]}...")
            return []


def main():
    """Demonstration of Gemini-enhanced AI Advisor."""
    print("=" * 70)
    print("  GEMINI-ENHANCED AI ADVISOR DEMONSTRATION")
    print("=" * 70)
    print()
    
    # Initialize
    advisor = GeminiAIAdvisor()
    
    if not advisor.client:
        print("❌ Gemini not available - cannot run demonstration")
        print("   Set GEMINI_API_KEY environment variable to enable Gemini")
        return 1
    
    # Load sample error analysis
    from evolution_system import CalculationEngine, ValidationModule, ErrorAnalyzer
    
    print("Step 1: Computing baseline predictions...")
    engine = CalculationEngine()
    validator = ValidationModule()
    analyzer = ErrorAnalyzer()
    
    predictions = engine.compute_all_predictions()
    validation_report = validator.validate_all(predictions)
    error_analysis = analyzer.analyze(validation_report)
    
    print(f"  ✓ Error patterns: {len(error_analysis.patterns)}")
    print()
    
    # Gemini analysis
    print("Step 2: Running Gemini deep analysis...")
    gemini_analysis = advisor.analyze_error_patterns_with_gemini(
        error_analysis.to_dict()
    )
    
    if gemini_analysis['gemini_available']:
        print(f"  ✓ Model: {gemini_analysis['model']}")
        print(f"  ✓ Insights generated: {len(gemini_analysis.get('insights', []))}")
        print()
        print("Key Insights:")
        for i, insight in enumerate(gemini_analysis.get('insights', [])[:5], 1):
            print(f"  {i}. {insight}")
        print()
    
    # Gemini suggestions
    print("Step 3: Generating refinement suggestions with Gemini...")
    gemini_suggestions = advisor.generate_refinement_suggestions_with_gemini(
        error_analysis.to_dict(),
        n_suggestions=3
    )
    
    print(f"  ✓ Suggestions generated: {len(gemini_suggestions)}")
    print()
    
    if gemini_suggestions:
        for i, suggestion in enumerate(gemini_suggestions, 1):
            print(f"Suggestion {i}: {suggestion.get('name', 'Unnamed')}")
            print(f"  Type: {suggestion.get('refinement_type', 'unknown')}")
            print(f"  Confidence: {suggestion.get('confidence', 'unknown')}")
            print(f"  Priority: {suggestion.get('priority_score', 0)}")
            print()
    
    print("=" * 70)
    print("  DEMONSTRATION COMPLETE")
    print("=" * 70)
    
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
