"""
IRH v68 Gap Resolution Scripts
==============================

This package contains scripts for resolving theoretical gaps identified
in IRHv68.md as documented in KimiAudit.md and IRHv68_Author_Response.md.

Phases:
- baseline_assessment: Compute current theory score and identify gaps
- resolve_theta0: θ₀ = 2/9 topological derivation
- resolve_cosmological: Cosmological constant via SUSY D₄
- resolve_vev: VEV cascade from SO(8) breaking
- resolve_ckm_pmns: CKM/PMNS matrix completion
- resolve_dark_matter: Dark matter CMB acoustic peaks
- resolve_mass_scale: Mass scale from D₄ self-energy
- resolve_nlo: NLO corrections via lattice perturbation theory
- gemini_council: AI council checkpoints with Gemini
- final_synthesis: Aggregate results and generate report

Author: IRH Computational Research Team
"""

from pathlib import Path

# Package root
PACKAGE_ROOT = Path(__file__).parent

# Output directory
OUTPUT_DIR = PACKAGE_ROOT.parent.parent / "outputs" / "gap_resolution"
