# ALP-ttbar Toy MC v1.6 — Preregistration: Magnetic-Field and Material-Budget Scan of the Two-Hypothesis Vertex Fit for Displaced Light ALP → e⁺e⁻

**Author:** Won Shik Paik (Independent Researcher, Auckland, New Zealand)
**Date frozen:** 2026-11-04 (this file is committed to GitHub before any v1.6 simulation or fit is run)
**Builds on:** v1.5, https://doi.org/10.5281/zenodo.23924862 (preregistration https://doi.org/10.5281/zenodo.23905511); toy study motivated by arXiv:2610.38932
**Zenodo (this preregistration, PDF):** https://doi.org/10.5281/zenodo.23942338
**GitHub:** https://github.com/wspaik5/ALP_ttbar_Toy_MC_v1.6_Preregistration_Field_Material_Scan
**Status:** plan only. No v1.6 outcome exists at the time of this commit.
**PDF version:** same text plus two figures drawn only from analytic formulas and published v1.5 numbers (no new
simulation).

---

## 0. Why v1.6

v1.5 found no gain from a two-hypothesis vertex fit at 17–50 MeV in a 3.8 T field: a free vertex absorbs a small
opening angle Δφ by moving along the track by s₀ = Δφ/Δω, leaving only a mismatch Δφ²/(2Δω), which is below the hit
resolution. Its outlook (Sec. 10 of the v1.5 preregistration) noted that this mismatch scales as 1/B, and that photon
conversions and bremsstrahlung scale with the material budget. v1.6 tests both in the same toy.

Analytic expectation for two tracks of opposite charge with pT = 10 GeV each (Δω = 2 · 0.3 B / (1000 pT) per mm):

| B | s₀ at Δφ = 1 mrad | mismatch at 1 mrad | mismatch at 10 mrad |
|---|---|---|---|
| 3.8 T | 4.4 mm | 2.2 µm | 0.22 mm |
| 2.0 T | 8.3 mm | 4.2 µm | 0.42 mm |
| 1.0 T | 16.7 mm | 8.3 µm | 0.83 mm |
| 0.5 T | 33.3 mm | 16.7 µm | 1.67 mm |
| 0.2 T | 83.3 mm | 41.7 µm | 4.17 mm |

The field also enters in three other ways, which pull in different directions:

- **Bremsstrahlung displacement.** A fractional curvature loss moves later hits by an amount proportional to ω, i.e. to
  B. At lower field the same energy loss distorts the hits less.
- **Conversion vertex location.** A conversion vertex is located by where two oppositely curved tracks become tangent.
  As B decreases the tracks straighten, the tangent point is less constrained along the track, and the material veto
  becomes less precise.
- **Momentum resolution** degrades roughly as 1/B, which widens the reconstructed mass.

Reducing the material lowers the conversion rate (∝ X₀) and the bremsstrahlung and multiple scattering in the tracker.
v1.6 quantifies these trade-offs in the toy. The B → small limit is also a first look at a tracker with little bending
in the vertex region (as in a forward VELO-like detector), without modelling such a geometry.

## 0a. Related work (prior art)

The ingredients of v1.6 are not new, and this study does not claim them:

- **Field and material in detector design.** Scanning the solenoid field and the tracker material budget to trade
  momentum resolution against multiple scattering, conversions and bremsstrahlung is a standard part of detector
  optimisation, e.g. for the FCC-ee concepts [A2, A3] and the Electron-Ion Collider trackers [A4].
- **Reduced field for low-mass dielectrons.** ALICE has recorded pp data at 13 TeV with the field reduced from 0.5 T to
  0.2 T to extend dielectron measurements to low-pT electrons [A1].
- **Using the field to reject conversions.** Low-mass dielectron analyses use the variable φ_V, the orientation of the
  pair opening angle relative to the magnetic field: conversion pairs acquire an apparent opening mainly in the plane
  perpendicular to the field and are removed with a cut in φ_V and mass [A5]. The H_conv/H_ALP comparison of v1.5 uses
  the same physical fact (conversion tracks are parallel at their origin and are separated only by the field), applied
  to the vertex fit in the transverse plane. φ_V itself is not available in this transverse-plane toy.
  For displaced pairs, the field-induced apparent opening appears for ALP pairs as well as for conversions, so the
  discriminating information is the true opening, and in particular its component along the field (in the r–z view),
  which the field does not bend and bremsstrahlung barely changes.

What v1.6 adds is limited to this search: it quantifies, in the preregistered toy of v1.0–v1.5, how the field and the
material budget change the conversion-induced loss in reach for top-associated displaced ALP → e⁺e⁻ with the v1.5
two-hypothesis selection. No search found an earlier study of this specific combination, but that is not claimed as
proof that none exists.

## 1. Questions

- **Q1 (primary).** With the v1.5 selection, how does the limit degradation from conversions at 17, 50, 100 and 200 MeV
  (cτ = 1 mm) change with the field B and with the material scale factor f?
- **Q2.** How do the Δχ² separation (conversions vs. ALP pairs), the conversion vertex resolution and the curvature
  (momentum) resolution change with B and f?

## 2. Unchanged from v1.5 (frozen)

- Mini simulation (`minitrack.py`), barrel geometry and sensor radii, hit resolution (15 µm pixel / 35 µm strip),
  Highland scattering, Bethe–Heitler bremsstrahlung.
- Signal generation (`mag.make_events`, seeds) and conversion generation (`conversions_truth`, seed 5), simulation seeds
  31 (conversions) and 41 (signal).
- Fits: H_conv = v1.4 fit (b); H_ALP seeded from H_conv; Δχ² = χ²_conv − χ²_ALP (`fit2h.py`).
- Selection `scan_v15` (exemption threshold k, veto width nσ, mass window) and the V-nomass variant; counting rule and
  metrics as in v1.1–v1.5.

## 3. Configurations (frozen)

Field B and material scale factor f (all material thicknesses X₀ in `bkg.py` and `minitrack.py` multiplied by f):

| config | B | f | purpose |
|---|---|---|---|
| R | 3.8 T | 1 | reference (must reproduce v1.5, Sec. 5) |
| B2 | 2.0 T | 1 | field scan |
| B1 | 1.0 T | 1 | field scan |
| B05 | 0.5 T | 1 | field scan |
| B02 | 0.2 T | 1 | field scan (low-bending limit; ALICE has run at 0.2 T [A1]) |
| M05 | 3.8 T | 0.5 | material scan |
| M025 | 3.8 T | 0.25 | material scan |
| C | 2.0 T | 0.5 | combined (about the field of the FCC-ee concepts [A2, A3]; context only) |

**Parameters that follow B and f** (fixed in advance):

- The curvature ω = −q · 0.3 B / (1000 pT) in simulation and fit uses the configured B.
- The relative momentum resolution used for the pair-mass smearing in `bkg.measure` scales as
  p_res = 0.02 × (3.8 T / B).
- The angular multiple-scattering term in `bkg.measure` scales as ms_term = 2.0 mrad·GeV × √f.
- The conversion probability per layer, the scattering and the bremsstrahlung all use f·X₀.

**Statistics.** To keep the run time manageable, each configuration uses the first 100,000 base conversion pairs and the
first 60,000 base signal pairs per mass (all 55,676 at 17 MeV), i.e. whole simulation chunks of 20,000. The weights are
scaled by the inverse of the subsample fraction. Because whole chunks are used, config R reproduces the v1.4/v1.5 hits of
these pairs exactly.

## 4. Sanity gate (frozen)

Before any degradation is computed:

1. **Identity (config R).** H_conv vertex radius and Δχ² equal the published v1.5 values for the same pairs within
   10⁻⁶ mm and 10⁻⁶, for ≥ 99.9% of pairs.
2. **Every configuration and sample.** Fit success ≥ 95% for H_conv and H_ALP; fraction with Δχ² < −0.1 at most 1%.

The median reported vertex resolution is recorded but not gated, because it is expected to grow at low field. If the gate
fails, the code is fixed, the failure and the fix are reported, and the gate is re-run.

## 5. Validation (independent samples only; criteria frozen)

Following the v1.5 lesson, the null reference is the boundary mixture ½χ²₀ + ½χ²₁, not χ²₁.

- **Y1 (null, no brems, B = 0.2 T and 2.0 T).** The v1.3 V4 collinear sample (seed 404) simulated at each field, fit (b)
  with c_k = 0. Fraction with Δχ² < 10⁻³ between 40% and 60%; median of the non-zero part between 0.30 and 0.65.
- **Y2 (response vs. field, no brems).** The v1.5 X2 generator (seed 606; pT = 10 GeV each, r uniform in 30–300 mm,
  |η| < 1.0) at Δφ = 2 mrad, simulated at B = 3.8, 2.0, 1.0, 0.5 and 0.2 T. The median Δχ² must increase monotonically
  as B decreases.
- **Y3 (propagation at low field).** For 10 GeV tracks at B = 0.2 T, the simulated hit positions without scattering or
  bremsstrahlung agree with the analytic helix (sagitta) to better than 0.1 µm at every layer.

If a criterion fails, the code is fixed and the fix is reported.

## 6. Predictions (written before running)

Values are the degradation from conversions with the v1.5 two-hypothesis selection (cτ = 1 mm). For reference, v1.5
(3.8 T, f = 1, full statistics) gave 126× / 68× / 28× / 9.1× at 17 / 50 / 100 / 200 MeV.

- **P1 (material, primary).** M05 at 17 MeV between **40× and 90×**. Halving the conversions alone gives about ×0.7
  under the counting rule (limit ∝ √background); less bremsstrahlung should add a further gain.
- **P2 (material).** M025 at 17 MeV between **20× and 63×**.
- **P3 (field, primary).** B02 at 17 MeV is **worse than R** (degradation larger than config R). The loss of conversion
  vertex location at low field is expected to outweigh the larger mismatch.
- **P4 (field).** B02 at 200 MeV is **better than R** (degradation smaller than config R), because 10 mrad openings give
  millimetre-scale mismatches at 0.2 T and are exempted cleanly.
- **P5 (mechanism).** The fraction of 17 MeV ALP pairs with Δχ² > 9 increases monotonically from R to B02 and reaches
  **≥ 30%** at B02. The same fraction for conversions (r < 800 mm) at B02 is **lower** than in R.
- **P6 (cost).** The core relative curvature resolution of signal tracks (H_ALP fit, |ω_fit/ω_true − 1|, MAD) is at
  least **10× worse** at B02 than in R.
- **P7 (combined).** C at 17 MeV lies **between** M05 and B2 (bounded by the two single-parameter changes).

Each prediction is reported as confirmed or refuted against these statements. Refuted predictions are not re-framed.
Predictions P1–P4 and P7 are evaluated on the subsample; config R on the same subsample is the comparison point.

## 7. Reporting

v1.6 note with a Figure 10:
- (a) degradation versus B at f = 1 for 17 / 50 / 100 / 200 MeV;
- (b) degradation versus f at 3.8 T;
- (c) Δχ² > 9 fractions (conversions and ALP pairs) and curvature resolution versus B.

The note also contains the Y1–Y3 validation, the prediction table, "Deviations from preregistration", "Limitations" and
"Future directions". All configurations are reported, including those that show no gain.

## 8. Limitations known in advance

- All v1.0–v1.5 limitations apply (transverse plane only, barrel only, idealised layers, no pattern recognition, toy
  material map, crude counting rule, selection optimised on the same samples, truth used for the material list, cosh η
  and the scattering momentum).
- The field is uniform; the barrel geometry is kept fixed. Low-field configurations are not a model of any real detector
  (in particular not of a forward VELO-like geometry), only a change of one parameter in this toy.
- Scaling all material by one factor ignores where the material is; the momentum-resolution scaling with 1/B is an
  assumption; charge identification, pattern recognition and two-track separation at low field are not modelled.
- **Only the transverse (bending-plane) opening is used.** The component of the opening angle along the field (r–z view)
  is not simulated or fitted. Conversions have almost no opening in that view, it is not affected by the field, and
  bremsstrahlung changes it very little, so it may separate ALP pairs from conversions better than any change of the
  field studied here. The field scan therefore varies only the bending-plane part of the problem. Planned later steps,
  each under its own preregistration and changing one ingredient at a time: (i) a three-dimensional vertex fit that
  includes the r–z opening, with the single-Gaussian bremsstrahlung model of fit (b); (ii) the same with a full
  Gaussian-sum filter (e.g. ACTS). Neither is tested in v1.6.
- Subsampled statistics; only trends and ratios are meaningful. No statement about the design of real detectors is made.

[A1] ALICE Collaboration, Soft-dielectron excess in proton-proton collisions at √s = 13 TeV, arXiv:2005.14522.
[A2] N. Bacchetta et al., CLD – A Detector Concept for the FCC-ee, arXiv:1911.12230.
[A3] The IDEA detector concept for FCC-ee, arXiv:2502.21223.
[A4] Latest vertex and tracking detector developments for the future Electron-Ion Collider, arXiv:2305.15593.
[A5] ALICE Collaboration, Dielectron production in proton-proton collisions at √s = 7 TeV, arXiv:1805.04391.
