"""v1.6 preregistration figures. NO simulation: analytic formulas of README Sec. 0 and published v1.5 numbers only."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

PT = 10.0                                            # GeV per leg (illustrative, README Sec. 0)
FIELDS = [(3.8, 'C0'), (2.0, 'C1'), (1.0, 'C2'), (0.5, 'C4'), (0.2, 'C3')]

# ---------------- Figure P1: analytic mismatch vs opening and vs field
fig, ax = plt.subplots(1, 2, figsize=(11, 4.0))
dphi = np.logspace(-1, np.log10(30), 200) * 1e-3
for B, c in FIELDS:
    dw = 2 * 0.3 * B / 1000 / PT
    ax[0].plot(dphi * 1e3, dphi**2 / (2 * dw) * 1e3, c=c, label=f'B = {B} T')
ax[0].axhline(15, c='gray', ls=':', lw=1); ax[0].text(0.12, 17, '15 µm pixel hit resolution', color='gray', fontsize=8)
for x, t in ((1.37, '≈17 MeV'), (13.7, '≈200 MeV')):
    ax[0].axvline(x, c='k', lw=0.6, alpha=0.4); ax[0].text(x * 1.07, 0.03, t, fontsize=7)
ax[0].set_xscale('log'); ax[0].set_yscale('log'); ax[0].set_ylim(0.02, 3e4)
ax[0].set_xlabel(r'transverse opening angle $\Delta\phi$ [mrad]')
ax[0].set_ylabel(r'mismatch $\Delta\phi^2/(2\Delta\omega)$ [µm]'); ax[0].legend(fontsize=7, loc='upper left')
ax[0].set_title('(a) mismatch left after the vertex shift', fontsize=10)

Bs = np.logspace(np.log10(0.15), np.log10(4.5), 100)
dw = 2 * 0.3 * Bs / 1000 / PT
ax[1].plot(Bs, 1e-3 / dw, 'k-', label=r'vertex shift $s_0$ at 1 mrad [mm]')
ax[1].plot(Bs, 1e-6 / (2 * dw) * 1e3, 'C3-', label='mismatch at 1 mrad [µm]')
ax[1].plot(Bs, Bs / 3.8, 'C0--', label='bremsstrahlung hit displacement (relative to 3.8 T)')
ax[1].plot(Bs, 3.8 / Bs, 'C2:', label='momentum resolution (relative to 3.8 T)')
for B, c in FIELDS:
    ax[1].axvline(B, c=c, lw=0.6, alpha=0.5)
ax[1].set_xscale('log'); ax[1].set_yscale('log'); ax[1].set_xlabel('B [T]')
ax[1].set_title('(b) competing scalings with the field', fontsize=10); ax[1].legend(fontsize=7, loc='upper right')
fig.suptitle(r'Fig. P1 (analytic, no simulation): field dependence, $p_T$ = 10 GeV per leg', fontsize=9.5)
plt.tight_layout(); plt.savefig('figP1_field_scalings_analytic.png', dpi=160)

# ---------------- Figure P2: material predictions at 17 MeV vs published v1.5
fig, ax = plt.subplots(figsize=(6.4, 4.4))
f = np.linspace(0.2, 1.05, 100)
ax.plot(f, 126 * np.sqrt(f), 'k--', lw=1, label=r'conversion yield only: $126\times\sqrt{f}$ (counting rule)')
ax.plot([1.0], [126], 'D', c='C0', ms=7, label='v1.5 published (3.8 T, f = 1, full statistics)')
for x, lo, hi, t in ((0.5, 40, 90, 'P1 (M05)'), (0.25, 20, 63, 'P2 (M025)')):
    ax.fill_between([x - 0.03, x + 0.03], lo, hi, color='C2', alpha=0.35, lw=0)
    ax.text(x + 0.04, np.sqrt(lo * hi), t, fontsize=8, color='C2', va='center')
ax.set_yscale('log'); ax.set_ylim(10, 300); ax.set_xlim(0.15, 1.1)
ax.set_xlabel('material scale factor f'); ax.set_ylabel(r'17 MeV limit degradation from conversions (c$\tau$ = 1 mm)')
ax.legend(fontsize=7, loc='lower right'); ax.grid(alpha=0.25)
ax.set_title('Fig. P2: preregistered material predictions at 17 MeV (3.8 T)\n'
             '(published v1.5 point and analytic yield scaling only; no v1.6 result shown)', fontsize=9)
plt.tight_layout(); plt.savefig('figP2_material_predictions.png', dpi=160)
print('ok')
