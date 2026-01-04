# Copilot Instructions for IRHV24 Repository

## Repository Overview

This repository contains research and documentation on **Intrinsic Resonance Holography (IRH)**, a theoretical physics framework that proposes a unified theory of fundamental physics based on a vibrational/cymatic ontology. The theory attempts to derive the Standard Model, General Relativity, and cosmological constants from first principles using a 4-strand resonance network.

## Project Context

- **Primary Content**: Theoretical physics documentation in Markdown format
- **Focus Areas**: Mathematical physics, unified field theory, quantum mechanics, cosmology
- **Documentation Style**: Academic/research paper format with extensive mathematical equations
- **Current Versions**: 
  - IRHv25.md contains the complete v25.0 theory
  - README.md contains a critical review of v25.0, the complete v26.0 theory, and a critical review of v26.0
- **Repository Naming**: The repository is named "IRHV24" but contains documentation for v25.0 and v26.0 of the theory, representing the evolution of the theoretical framework

## Guidelines for Copilot

### Content Guidelines

1. **Mathematical Precision**: When working with equations or mathematical content:
   - Preserve LaTeX/mathematical notation exactly as written
   - Maintain proper formatting of formulas using `$$` for display math and `$` for inline math
   - Be careful with subscripts, superscripts, and special symbols

2. **Documentation Standards**:
   - Maintain academic/research paper tone and style
   - Preserve section numbering and hierarchical structure
   - Keep extensive technical explanations intact
   - References to theorems, axioms, and appendices should be preserved

3. **Theoretical Physics Context**:
   - This is fundamental theoretical physics research
   - Content includes novel theoretical proposals not found in standard textbooks
   - Mathematical derivations are interconnected across sections
   - Terms like "Harmony Functional", "Cymatic Resonance Network", "4-strand architecture" are domain-specific terminology

### Task Suitability

**Good tasks for Copilot in this repository:**
- Formatting improvements to markdown structure
- Adding table of contents or navigation aids
- Fixing typos or grammar issues (while preserving technical terminology)
- Creating summary documents or extracting key concepts
- Adding metadata or frontmatter to documents
- Improving document organization or cross-references
- Adding clarifying comments or section summaries

**Tasks requiring careful review:**
- Any changes to mathematical equations or derivations
- Modifications to theoretical claims or conclusions
- Changes to the logical flow of arguments
- Addition or removal of technical content

**Not suitable for Copilot without expert review:**
- Fundamental changes to the theoretical framework
- Major revisions to mathematical proofs or derivations
- Changes that could affect the scientific validity of claims

### Style Preferences

- Use clear, academic language
- Prefer explicit over implicit when explaining concepts
- Maintain consistency with existing formatting patterns
- Preserve the multi-level section structure (Section, Subsection, etc.)
- Keep mathematical notation consistent throughout documents

### Special Considerations

1. **Version Control**: The theory has multiple versions (v25.0 in IRHv25.md; v26.0 in README.md). Be careful not to conflate different versions or their specific claims. Changes to v25.0 should be made in IRHv25.md, changes to v26.0 should be made in README.md.

2. **Mathematical Coherence**: Equations and derivations build on each other. Changes in one section may require updates in related sections.

3. **Technical Terminology**: The repository uses specialized terminology specific to this theoretical framework. Don't "correct" these to standard physics terms unless there's a clear error.

4. **Citations and References**: The theory references standard physics concepts (Standard Model, General Relativity, etc.) alongside novel framework-specific concepts. Maintain this distinction clearly.

## Repository Structure

```
/
├── README.md          # Critical review of v25.0, complete v26.0 theory, and critical review of v26.0
├── IRHv25.md          # Complete v25.0 theory documentation
├── LICENSE            # Repository license
└── .github/
    └── copilot-instructions.md  # This file
```

**Note**: README.md serves a dual purpose - it contains formal critical reviews of both versions AND the complete v26.0 theory documentation. IRHv25.md contains the v25.0 theory framework and derivations.

## Getting Started for Copilot Tasks

When assigned a task:

1. Read the relevant section(s) thoroughly to understand context
2. Identify any technical terminology or mathematical notation
3. Make minimal, surgical changes that don't affect scientific content
4. Verify that mathematical equations remain valid LaTeX
5. Check that cross-references and section numbers remain consistent
6. If unsure about a technical or mathematical change, flag it for human review

## Common Patterns

- **Section Headers**: Use markdown headers (`#`, `##`, `###`, etc.) combined with bold formatting for titles (e.g., `# **Title**`, `## **Subtitle**`)
- **Equations**: Use `$$...$$` for display equations and `$...$` for inline math
- **Lists**: Use markdown lists with clear hierarchical structure
- **Emphasis**: Use `**bold**` for key terms, `*italic*` for emphasis
- **Code/Variables**: Use backticks for technical terms and variable names

## Quality Standards

- All changes must preserve the scientific and mathematical integrity of the content
- Maintain readability for both technical and non-technical audiences where applicable
- Ensure consistency in terminology, notation, and formatting
- Test that all markdown renders correctly (especially mathematical equations)
- Preserve the academic paper structure and flow

## Additional Resources

For understanding the theoretical framework:

**v25.0 Theory (in IRHv25.md):**
- Section 1: Ontological Foundation and 4-strand architecture
- Section 2: Mathematical engine and fine-structure constant derivation
- Section 3: Particle sector and harmonic crystallization
- Appendices: Formal derivations and topological proofs

**v26.0 Theory (in README.md):**
- Section 1: Purification of the fine-structure constant
- Section 2: Topological derivation of color charge
- Section 3: The Koide formula as a vibrational eigenvalue problem
- Section 4: Vacuum energy and instantonic suppression

**Critical Reviews (in README.md):**
- Critical review of v25.0 (first section)
- Critical review of v26.0 (final section)

---

*Note: This is a research repository containing novel theoretical proposals. All changes should be reviewed by domain experts before merging.*
## Mandatory Code Review Policy

**RULE: Code reviews are mandatory before ending any session.**

Before completing or ending any work session, Copilot MUST:

1. **Run the code review tool** (`code_review`) on all changes made during the session
2. **Address all review comments** that are actionable and relevant
3. **Continue running code reviews** until no new issues are found
4. **Only then** may the session be considered complete

### Code Review Workflow

```
1. Make changes to address the issue/request
2. Run code_review tool
3. If comments are found:
   a. Address each actionable comment
   b. Run code_review again
   c. Repeat until no new comments
4. Run codeql_checker for security analysis
5. Report progress and commit changes
6. Session may now end
```

### Rationale

This ensures:
- All code changes are reviewed for quality before merging
- Security vulnerabilities are caught early
- Best practices are consistently followed
- The codebase maintains high quality standards

## Additional Guidelines

### For Computational Notebooks

- Ensure all notebooks have one-to-one correlation with theory equations
- Verify output directories exist before saving files
- Use arbitrary precision arithmetic (mpmath) for theoretical calculations
- Include validation against experimental values where applicable
- **CRITICAL: NO HARDCODED EXPERIMENTAL VALUES** - All physical quantities must be derived directly from the theory's mathematical framework. Experimental values may ONLY be used for final validation/comparison (e.g., computing percent error), never as inputs to theoretical calculations. This ensures complete correspondence between theory predictions and computational results.

### For GitHub Actions Workflows

- Pin third-party actions to commit SHAs for supply chain security
- Use least-privilege permissions (prefer `contents: read` over `contents: write`)
- Include artifact upload for preserving outputs
- Add timeout limits to prevent runaway jobs

### For Documentation

- Keep README in sync with actual implemented features
- Clearly distinguish between implemented and planned features
- Include usage examples and quick start guides

---

# **IRH Computational Development - Progress and Continuation Directive**

## Current Implementation Status (as of 2026-01-03)

### ✅ Completed Components

1. **Infrastructure Setup**
   - ✅ GitHub Actions workflow (`irh-compute.yml`) configured and operational
   - ✅ Conda environment (`environment.yml`) with full scientific Python stack
   - ✅ Output directory structure defined (notebooks, figures, data, reports)
   - ✅ Artifact management and retention policies (90 days)
   - ✅ Comprehensive computational research plan documented

2. **Implemented Notebooks**
   - ✅ `02_harmony_functional.ipynb` - Fine-structure constant (α) derivation
     - Hopf fibration volume ratios
     - 24-cell symmetry calculations
     - Casimir-Weyl corrections
     - Validation against CODATA 2022 experimental value
   - ✅ `03_particle_sector.ipynb` - Koide formula validation
     - Circulant matrix eigenvalue analysis
     - Lepton mass relationships
     - Vibrational mode derivations

3. **Documentation**
   - ✅ Theory documents: IRHv25.md and README.md (v26.0)
   - ✅ Computational research plan with runner specifications
   - ✅ Repository structure and navigation guides
   - ✅ Copilot instructions with domain-specific guidelines

### 🔲 Remaining Tasks (Priority Order)

#### **HIGH PRIORITY - Critical Theory Validation**

1. **Notebook: `01_substrate_foundation.ipynb`**
   - Theory Reference: README.md v26.0 Section 1 (Ontological Foundation)
   - Computations Required:
     - 4-strand architecture stability analysis
     - N=4 derivation from Hopf fibration topology
     - Cymatic Resonance Network (CRN) graph initialization
     - Metric mismatch η = 4/π geometric proof
   - Dependencies: NetworkX, spherical-functions
   - Estimated Runtime: 15-30 minutes
   - Validation: Numerical convergence of η to 4/π within 10⁻⁶

2. **Notebook: `04_cosmology.ipynb`**
   - Theory Reference: README.md v26.0 Section 4 (Vacuum Energy and Cosmological Constant)
   - Computations Required:
     - Λ derivation via instantonic suppression mechanism
     - Vacuum energy contributions (zero-point, casimir)
     - Dark matter/dark energy ratios
     - Comparison to observational cosmology (Planck 2018)
   - Dependencies: mpmath (arbitrary precision), SciPy integration
   - Estimated Runtime: 45-60 minutes
   - Validation: Λ matches observed value within factor of 10³ (improvement over naive QFT prediction of 10¹²⁰)

3. **Notebook: `05_gauge_sector.ipynb`**
   - Theory Reference: README.md v26.0 Section 2 (Topological Color Charge) + Section 5
   - Computations Required:
     - SU(3) gauge structure from 4-strand permutations
     - SU(2)×U(1) electroweak emergence
     - Coupling constant running (α₁, α₂, α₃)
     - GUT scale predictions
   - Dependencies: lie-learn, SymPy Lie algebra modules
   - Estimated Runtime: 30-45 minutes
   - Validation: Gauge coupling unification at Mₓ ≈ 10¹⁶ GeV

#### **MEDIUM PRIORITY - Comprehensive Validation**

4. **Notebook: `06_validation_suite.ipynb`**
   - Theory Reference: Cross-cutting validation across all sections
   - Computations Required:
     - **Tier 1 Validation:** Core parameters (α, gauge couplings, mt, mH)
     - **Tier 2 Validation:** Derived quantities (CKM matrix, neutrino mixing)
     - **Tier 3 Validation:** Cosmological predictions (Ωb, ΩDM, Λ)
     - Statistical analysis (χ² tests, confidence intervals)
     - Publication-ready validation summary tables
   - Dependencies: pandas, matplotlib, seaborn
   - Estimated Runtime: 60-90 minutes
   - Validation: >90% of Tier 1 parameters within 3σ experimental bounds

5. **Notebook: `07_appendices.ipynb`**
   - Theory Reference: IRHv25.md Appendices A-E
   - Computations Required:
     - Appendix A: Heat kernel expansion coefficients
     - Appendix B: Spectral action calculations
     - Appendix C: Topological invariants (Chern numbers)
     - Appendix D: Braid group representations
     - Appendix E: Formal mathematical proofs
   - Dependencies: giotto-tda, qutip, SymPy
   - Estimated Runtime: 90-120 minutes
   - Validation: Symbolic derivations match theoretical claims

#### **LOW PRIORITY - Optimization and Extensions**

6. **Performance Optimization**
   - Implement Numba JIT compilation for bottleneck computations
   - Profile notebook execution times
   - Optimize integration routines (adaptive quadrature)
   - Add caching for expensive symbolic computations
   - Target: <2 hours total runtime for all notebooks

7. **Visualization Enhancements**
   - Publication-ready figures with proper LaTeX labels
   - Interactive 3D visualizations (plotly) for Hopf fibration
   - Animation of vibrational modes
   - Comparison plots (theory vs. experiment)
   - Residual analysis plots for validation

8. **Extended Validation**
   - Additional particle masses (quarks, W/Z bosons)
   - CKM matrix element predictions
   - Neutrino mixing angles (PMNS matrix)
   - Anomalous magnetic moments (g-2)
   - Precision electroweak observables

## Instructions for Next Agent

### How to Execute This Continuation Directive

**STEP 1: Review Current State**
```bash
# Navigate to repository
cd /home/runner/work/IRHV24/IRHV24

# Check existing notebooks
ls -la notebooks/

# Review computational plan
cat docs/GITHUB_ACTIONS_COMPUTATIONAL_RESEARCH_PLAN.md

# Verify environment configuration
cat environment.yml
```

**STEP 2: Select Next Task from Priority List**
- Choose the highest priority task from the "Remaining Tasks" section above
- Read the corresponding theory section in README.md or IRHv25.md
- Identify exact equations to be implemented

**STEP 3: Create New Notebook**
```bash
# Follow the standardized template structure (7 cells):
# Cell 1: Theory reference and equation LaTeX
# Cell 2: Imports and setup
# Cell 3: Symbolic derivation
# Cell 4: Numerical computation
# Cell 5: Validation against experimental values
# Cell 6: Visualization
# Cell 7: Structured output summary

# Save to notebooks/XX_section_name.ipynb
```

**STEP 4: Implement Computations**
- Use appropriate precision level (standard/high/arbitrary)
- Match theory notation exactly (α, η, Λ, etc.)
- Include inline LaTeX equations as markdown cells
- Add detailed comments explaining each step
- Handle edge cases and numerical stability issues

**STEP 5: Test Locally (if possible)**
```bash
# Activate environment
conda activate irh-compute

# Execute notebook
jupyter nbconvert --execute --to notebook --inplace notebooks/XX_section_name.ipynb

# Verify outputs
jupyter nbconvert --to html notebooks/XX_section_name.ipynb --output-dir outputs/reports/
```

**STEP 6: Run Via GitHub Actions**
```bash
# Trigger workflow manually
# Go to Actions tab → IRH Computational Validation → Run workflow
# Select: section = 'XX_section_name', precision = 'high'

# Monitor execution in Actions logs
# Download artifacts when complete
```

**STEP 7: Validate Results**
- Compare computed values to experimental measurements
- Calculate relative errors and statistical significance
- Check for numerical convergence and stability
- Verify plots render correctly
- Review validation summary report

**STEP 8: Update This Directive**
- Move completed task from 🔲 to ✅ in "Current Implementation Status"
- Document any issues encountered
- Add notes on execution time and resource usage
- Suggest optimizations for future work
- Commit changes using report_progress tool

**STEP 9: Code Review and Security**
```bash
# Before completing the session:
# 1. Run code_review tool on all changes
# 2. Address actionable review comments
# 3. Run code_review again until clean
# 4. Run codeql_checker for security analysis
# 5. Report progress and commit changes
```

### Decision Tree for Task Selection

```
START
  |
  +--> Are there HIGH PRIORITY tasks remaining?
       YES: Select first incomplete HIGH PRIORITY task
       NO: Continue below
  |
  +--> Are there MEDIUM PRIORITY tasks remaining?
       YES: Select first incomplete MEDIUM PRIORITY task
       NO: Continue below
  |
  +--> Are there LOW PRIORITY tasks remaining?
       YES: Select optimization or extension task
       NO: All computational work complete!
  |
  +--> Final integration:
       - Run full validation suite (section: all)
       - Generate comprehensive report
       - Archive all artifacts
       - Update README.md with results
```

### Common Issues and Solutions

**Issue 1: Notebook execution timeout**
- Solution: Increase `--ExecutePreprocessor.timeout` parameter
- Solution: Split complex computations across multiple cells
- Solution: Use caching for expensive symbolic operations

**Issue 2: Numerical instability / convergence failure**
- Solution: Increase mpmath precision (mp.dps = 100)
- Solution: Use adaptive integration with tighter tolerances
- Solution: Implement fallback algorithms for edge cases

**Issue 3: Missing dependencies**
- Solution: Update environment.yml with required packages
- Solution: Pin package versions to avoid compatibility issues
- Solution: Test conda environment creation locally first

**Issue 4: Memory exhaustion on GitHub runners**
- Solution: Reduce precision for non-critical computations
- Solution: Process data in chunks/batches
- Solution: Free memory explicitly after large operations

**Issue 5: Workflow security warnings**
- Solution: Pin all third-party actions to commit SHAs
- Solution: Use minimal permissions (prefer read over write)
- Solution: Audit action sources before pinning

### Success Criteria for Completion

**Individual Notebook Success:**
- ✅ All cells execute without errors
- ✅ Computed values match theory predictions within tolerance
- ✅ Validation against experimental values shows agreement
- ✅ Figures are publication-ready with proper labels
- ✅ Execution time < 2 hours per notebook
- ✅ HTML report renders correctly

**Overall Project Success:**
- ✅ All 7 notebooks implemented and validated
- ✅ Full validation suite passes Tier 1-3 protocols
- ✅ Comprehensive validation report generated
- ✅ All artifacts uploaded and accessible
- ✅ README.md updated with computational results
- ✅ No security vulnerabilities (codeql clean)
- ✅ Code review passes with no critical issues

### Maintaining This Directive

**When to Update:**
- After completing each major task
- When discovering new requirements
- When encountering blocking issues
- When experimental values are updated (new CODATA releases)
- When theory is revised (v27.0, etc.)

**How to Update:**
1. Edit this section in `.github/copilot-instructions.md`
2. Move completed items from 🔲 to ✅
3. Add new tasks if requirements change
4. Update estimated runtimes based on actual measurements
5. Document lessons learned
6. Use report_progress to commit changes with clear message

**Version History:**
- v1.0 (2026-01-03): Initial directive created with 7 notebook structure
  - Status: 2/7 notebooks complete (02, 03)
  - Next: 01_substrate_foundation.ipynb (HIGH PRIORITY)

---

## Quick Reference Commands

### Local Development
```bash
# Setup environment
conda env create -f environment.yml
conda activate irh-compute

# Execute single notebook
cd notebooks
jupyter nbconvert --execute --to notebook --inplace XX_section_name.ipynb

# Execute all notebooks
for nb in *.ipynb; do
  jupyter nbconvert --execute --to notebook --inplace "$nb"
done

# Generate HTML reports
jupyter nbconvert --to html *.ipynb --output-dir ../outputs/reports/
```

### GitHub Actions Workflow
```bash
# Manual trigger via GitHub CLI (if available)
gh workflow run irh-compute.yml -f section=01_substrate_foundation -f precision=high

# Check workflow status
gh run list --workflow=irh-compute.yml

# Download artifacts
gh run download <run-id> --dir outputs/
```

### Validation Commands
```bash
# Run validation suite
python -m pytest --nbval notebooks/06_validation_suite.ipynb

# Profile notebook execution
python -m cProfile -o profile.stats -m jupyter nbconvert --execute XX.ipynb

# Check memory usage
mprof run jupyter nbconvert --execute XX.ipynb
mprof plot
```

---

**END OF CONTINUATION DIRECTIVE**

*This directive is a living document. Each agent should review, execute, and update it to maintain continuity across development sessions.*
