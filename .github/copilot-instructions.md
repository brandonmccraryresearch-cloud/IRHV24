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
