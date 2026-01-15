# Using Gemini AI with IRH Evolution System

## Overview

The IRH Theory Evolution System can be enhanced with **Google Gemini AI** for more sophisticated error analysis and refinement suggestions. Gemini provides:

1. **Deep Error Pattern Analysis** - Identifies subtle correlations and systematic effects
2. **Novel Refinement Suggestions** - Generates creative topological modifications
3. **Mathematical Derivation Assistance** - Helps formulate precise mathematical expressions
4. **Theoretical Soundness Validation** - Ensures suggestions follow Directive A

## Setup

### 1. Install Google GenAI SDK

```bash
pip install google-genai
```

### 2. Get Gemini API Key

**Option A: Google AI Studio (Recommended for Development)**
1. Go to https://aistudio.google.com/app/apikey
2. Create a new API key
3. Copy the key

**Option B: Google Cloud Console (For Production)**
1. Go to Google Cloud Console
2. Enable Generative Language API
3. Create API credentials
4. Copy the API key

### 3. Set Environment Variable

```bash
# For current session
export GEMINI_API_KEY='your-api-key-here'

# Or permanently in ~/.bashrc or ~/.zshrc
echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

**For GitHub Actions:** Add `GEMINI_API_KEY` as a repository secret in Settings → Secrets and variables → Actions.

## Usage

### Basic Usage (Python API)

```python
from evolution_system.gemini_advisor import GeminiAIAdvisor
from evolution_system import CalculationEngine, ValidationModule, ErrorAnalyzer

# Initialize components
engine = CalculationEngine()
validator = ValidationModule()
analyzer = ErrorAnalyzer()

# Compute and validate predictions
predictions = engine.compute_all_predictions()
validation_report = validator.validate_all(predictions)
error_analysis = analyzer.analyze(validation_report)

# Use Gemini-enhanced advisor
gemini_advisor = GeminiAIAdvisor()

# 1. Deep error pattern analysis
gemini_analysis = gemini_advisor.analyze_error_patterns_with_gemini(
    error_analysis.to_dict()
)

print("Gemini Insights:")
for insight in gemini_analysis.get('insights', []):
    print(f"  • {insight}")

# 2. Generate refinement suggestions
suggestions = gemini_advisor.generate_refinement_suggestions_with_gemini(
    error_analysis.to_dict(),
    n_suggestions=5
)

print(f"\nGenerated {len(suggestions)} suggestions:")
for i, suggestion in enumerate(suggestions, 1):
    print(f"{i}. {suggestion['name']}")
    print(f"   Type: {suggestion['refinement_type']}")
    print(f"   Confidence: {suggestion['confidence']}")
```

### Command-Line Usage

```bash
# Run Gemini advisor demo
python3 evolution_system/gemini_advisor.py

# Or integrate with evolution cycle
python3 demo_evolution_cycle.py --use-gemini
```

### Configuration

Customize Gemini behavior:

```python
from evolution_system.gemini_advisor import GeminiAIAdvisor, GeminiConfig

config = GeminiConfig(
    model_name="gemini-2.0-flash-exp",  # Or gemini-1.5-pro, gemini-1.5-flash
    temperature=0.3,                     # Lower = more deterministic
    top_p=0.95,                          # Nucleus sampling
    max_output_tokens=8192,              # Maximum response length
    
    # Physics-specific
    enforce_topological_origin=True,     # Require Directive A compliance
    require_mathematical_derivation=True, # Require full derivation
    filter_phenomenological=True         # Reject phenomenological suggestions
)

advisor = GeminiAIAdvisor(config=config)
```

## Features

### 1. Error Pattern Analysis

Gemini analyzes error patterns to identify:
- Root causes of discrepancies
- Correlations between observables
- Missing topological structures
- Systematic vs. random errors
- Scale-dependent effects

**Example:**
```python
analysis = gemini_advisor.analyze_error_patterns_with_gemini(error_analysis)

# Access insights
if analysis['gemini_available']:
    print(f"Model: {analysis['model']}")
    for insight in analysis['insights']:
        print(f"  • {insight}")
```

### 2. Refinement Suggestion Generation

Gemini generates novel refinement suggestions following Directive A:
- **Topological origin** - All suggestions from Hopf fibrations, Chern classes, etc.
- **Mathematical rigor** - Full derivation steps provided
- **Testable predictions** - Each suggestion has falsifiable consequences
- **Symmetry preservation** - Gauge, Lorentz, CPT verified

**Example:**
```python
suggestions = gemini_advisor.generate_refinement_suggestions_with_gemini(
    error_analysis,
    n_suggestions=5
)

for suggestion in suggestions:
    print(f"Name: {suggestion['name']}")
    print(f"Formula: {suggestion['mathematical_formula']}")
    print(f"Basis: {suggestion['topological_basis']}")
    print(f"Affected: {', '.join(suggestion['affected_observables'])}")
    print()
```

### 3. Fallback Mode

If Gemini is unavailable (no API key or network issues), the system automatically falls back to template-based suggestions:

```python
advisor = GeminiAIAdvisor()  # Works even without API key

if advisor.client:
    # Use Gemini
    suggestions = advisor.generate_refinement_suggestions_with_gemini(...)
else:
    # Fallback to templates
    from evolution_system import AIAdvisor
    template_advisor = AIAdvisor()
    suggestions = template_advisor.get_top_suggestions(...)
```

## Directive A Compliance

**CRITICAL:** All Gemini-generated suggestions must follow Directive A:

✅ **ALLOWED:**
- Constants from topological invariants (Hopf fibrations, Chern classes, Braid groups)
- Geometric corrections (volume ratios, Euler characteristics)
- Quantum topological effects (Berry phases, instantons, holonomy)

❌ **FORBIDDEN:**
- Phenomenological fitting parameters
- Adjustable constants tuned to match data
- Empirical formulas without topological origin

The system enforces this through:
1. **Prompt engineering** - Instructions emphasize topological origin
2. **Post-processing** - Filters out non-topological suggestions
3. **Validation** - IntegrationSystem verifies topological derivation

## Example Output

```
✓ Gemini AI initialized: gemini-2.0-flash-exp

Gemini Deep Analysis:
  • Fine-structure constant discrepancy suggests missing higher-order Hopf volume terms
  • Gauge coupling errors correlate - likely systematic Chern class correction needed
  • Cosmological parameters require additional instanton suppression terms
  • Lepton mass hierarchy suggests Berry phase corrections from flavor manifold

Generated Refinement Suggestions:

1. Second-Order Hopf Fibration Correction
   Type: hopf_fibration
   Formula: α⁻¹_refined = α⁻¹_base × [1 + κ × (Vol(S¹⁵)/Vol(S⁸))²]
   Basis: Higher-dimensional Hopf fibrations S¹⁵→S⁸ provide additional volume ratios
   Confidence: HIGH
   Priority: 95.0

2. Chern Class C₃ Correction
   Type: chern_class
   Formula: α_i_refined = α_i × [1 + κ₃ × C₃(G)/dim(G)²]
   Basis: Third Chern class captures curvature³ terms from gauge bundle
   Confidence: MEDIUM
   Priority: 87.5
   
[... 3 more suggestions ...]
```

## Performance

- **Typical response time:** 3-10 seconds per API call
- **Token usage:** ~2,000-5,000 tokens per suggestion generation
- **Cost:** ~$0.01-0.05 per evolution cycle (Gemini 2.0 Flash)
- **Rate limits:** 60 requests per minute (typical)

## Troubleshooting

### Issue: "GEMINI_API_KEY not found"
**Solution:** Set the environment variable:
```bash
export GEMINI_API_KEY='your-api-key'
```

### Issue: "Failed to initialize Gemini: 403 Forbidden"
**Solution:** Check that your API key is valid and the Generative Language API is enabled in Google Cloud Console.

### Issue: "Gemini call failed: timeout"
**Solution:** Increase timeout or check network connection:
```python
config = GeminiConfig(max_output_tokens=4096)  # Reduce for faster responses
```

### Issue: "JSON parse error in suggestions"
**Solution:** Gemini sometimes adds markdown formatting. The system handles this automatically, but you can increase temperature for more consistent formatting:
```python
config = GeminiConfig(temperature=0.1)  # More deterministic
```

## Best Practices

1. **Start with template-based advisor** - Validate that basic system works
2. **Enable Gemini for production** - Use when you need novel suggestions
3. **Review Gemini suggestions carefully** - AI can make mistakes, verify topological origin
4. **Combine both approaches** - Use templates + Gemini for comprehensive coverage
5. **Monitor API usage** - Track costs and rate limits
6. **Set appropriate temperature** - Lower (0.1-0.3) for physics, higher (0.7-1.0) for exploration

## Integration with Evolution Cycle

The complete evolution cycle can use Gemini:

```python
from evolution_system import EvolutionCycle
from evolution_system.gemini_advisor import GeminiAIAdvisor

# Create cycle with Gemini advisor
cycle = EvolutionCycle()
cycle.advisor = GeminiAIAdvisor()  # Replace default advisor

# Run cycle
result = cycle.run(max_refinements=5, auto_integrate=False)

# Gemini will be used for:
# - Error pattern analysis
# - Refinement suggestion generation
# - Theoretical soundness validation
```

## Advanced Usage

### Custom Prompts

Modify prompts for specific research goals:

```python
advisor = GeminiAIAdvisor()

# Custom theory context
advisor.theory_context += """
Additional context:
- Focus on electroweak sector
- Priority: W/Z mass predictions
- Consider higher-order RG effects
"""

# Generate suggestions with custom context
suggestions = advisor.generate_refinement_suggestions_with_gemini(error_analysis, n=3)
```

### Batch Processing

Process multiple error analyses:

```python
advisor = GeminiAIAdvisor()

for cycle_id, error_analysis in enumerate(multiple_analyses):
    suggestions = advisor.generate_refinement_suggestions_with_gemini(
        error_analysis,
        n_suggestions=3
    )
    save_suggestions(f"cycle_{cycle_id}.json", suggestions)
```

## References

- **Google GenAI SDK:** https://github.com/googleapis/python-genai
- **Gemini API Docs:** https://ai.google.dev/docs
- **IRH Theory:** See README.md and docs/THEORY_EVOLUTION_SYSTEM.md
- **Directive A:** See .github/copilot-instructions.md

## Support

For issues with:
- **Gemini API:** Google AI Studio support
- **Evolution System:** GitHub issues
- **Theory Questions:** See documentation

---

**Version:** 1.0.0  
**Last Updated:** 2026-01-09  
**Status:** ✅ Production Ready
