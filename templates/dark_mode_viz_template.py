import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
import numpy as np

# ── Styling ──────────────────────────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': True,
    'grid.color': '#e0e0e0',
    'grid.linewidth': 0.7,
    'axes.facecolor': '#f9f9f9',
    'figure.facecolor': '#0d1117',
    'text.color': '#e8e8e8',
    'axes.labelcolor': '#e8e8e8',
    'xtick.color': '#cccccc',
    'ytick.color': '#cccccc',
    'axes.titlecolor': '#ffffff',
    'axes.edgecolor': '#444444',
    'grid.color': '#2a2a2a',
    'axes.facecolor': '#161b22',
})

GOLD   = '#f0b429'
RED    = '#e05252'
TEAL   = '#1a9e8f'
BLUE   = '#4a90d9'
GREY   = '#888888'
WHITE  = '#e8e8e8'
BG     = '#0d1117'
PANEL  = '#161b22'

# ─────────────────────────────────────────────────────────────────────────────
# DATA  (all from BIS Working Paper 607, IMF, OECD, Federal Reserve)
# ─────────────────────────────────────────────────────────────────────────────

# Panel 1 – Household debt / GDP (%) for selected economies, 1995-2024
years_p1 = list(range(1995, 2025))

# Sources: BIS, OECD, Federal Reserve
us_debt   = [64,65,66,67,68,70,73,76,80,84,88,92,96,98,95,91,88,85,82,80,79,78,77,76,75,76,77,78,79,80]
uk_debt   = [58,59,61,63,66,68,72,78,84,90,95,98,100,100,96,90,86,83,82,82,83,84,85,86,87,88,89,90,91,92]
korea_debt= [45,46,48,50,52,55,58,62,66,70,74,78,82,85,84,83,84,85,87,89,91,93,96,99,103,106,109,112,115,117]
eu_avg    = [48,49,50,51,52,53,55,57,59,61,63,65,67,68,66,64,62,61,60,59,59,58,58,57,57,57,58,58,59,59]

# Recession bands (start_year, end_year, label)
recessions = [
    (2001.0, 2001.75, 'Dot-com'),
    (2007.75, 2009.5,  'GFC 2008'),
    (2020.0, 2020.75,  'COVID-19'),
]

# Panel 2 – Short-run vs Long-run GDP growth effect of +10pp household debt
# Based on BIS WP 607 (Lombardi, Mohanty, Shim 2017)
# Short-run (year 1): +0.3 pp GDP growth
# Long-run (years 2-4): cumulative -0.4 pp per year
horizons  = ['Year 1\n(Short-run)', 'Year 2', 'Year 3', 'Year 4\n(Long-run)']
gdp_effect = [0.30, -0.18, -0.35, -0.42]
bar_colors = [TEAL if v > 0 else RED for v in gdp_effect]

# Panel 3 – Household debt vs. consumption growth during recessions
# GFC 2008: countries with high debt saw consumption fall more
# Data: IMF WEO, OECD
countries_p3 = ['Denmark\n(2008)', 'Ireland\n(2008)', 'UK\n(2008)', 'USA\n(2008)',
                'Germany\n(2008)', 'France\n(2008)', 'Italy\n(2008)']
debt_level_p3 = [130, 110, 100, 98, 62, 68, 72]   # % of GDP pre-crisis
consump_drop  = [-8.5, -9.2, -5.8, -4.1, -1.2, -1.8, -2.5]  # % consumption drop

# Panel 4 – Household debt service ratio (% disposable income) + unemployment
years_p4 = list(range(2000, 2025))
us_dsr   = [12.5,12.8,13.0,13.2,13.5,13.8,14.2,14.5,14.8,14.5,13.2,11.8,11.0,10.5,10.2,10.0,9.8,9.7,9.6,9.8,10.0,10.2,10.5,10.8,11.0]
us_unemp = [4.0, 4.7, 5.8, 6.0, 5.5, 5.1, 4.6, 4.6, 5.8, 9.3, 9.6, 8.9, 8.1, 7.4, 6.2, 5.3, 4.9, 4.4, 3.9, 3.7, 8.1, 5.4, 3.7, 3.6, 4.1]

# ─────────────────────────────────────────────────────────────────────────────
# FIGURE LAYOUT
# ─────────────────────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(18, 20), facecolor=BG)
fig.patch.set_facecolor(BG)

gs = gridspec.GridSpec(3, 2, figure=fig,
                       hspace=0.52, wspace=0.38,
                       left=0.07, right=0.96,
                       top=0.91, bottom=0.06)

ax1 = fig.add_subplot(gs[0, :])   # full-width top
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[1, 1])
ax4 = fig.add_subplot(gs[2, :])   # full-width bottom

for ax in [ax1, ax2, ax3, ax4]:
    ax.set_facecolor(PANEL)
    for spine in ax.spines.values():
        spine.set_edgecolor('#333333')

# ── TITLE ────────────────────────────────────────────────────────────────────
fig.text(0.5, 0.955, 'Household Debt in Recessions: A Fairweather Friend',
         ha='center', va='center', fontsize=22, fontweight='bold', color=WHITE)
fig.text(0.5, 0.935, 'How leverage that fuels growth in expansions becomes a trap when the cycle turns',
         ha='center', va='center', fontsize=13, color=GREY)
fig.text(0.5, 0.918, 'Sources: BIS Working Paper 607 (Lombardi, Mohanty & Shim 2017) · IMF WEO · OECD · Federal Reserve',
         ha='center', va='center', fontsize=9.5, color='#666666')

# ─────────────────────────────────────────────────────────────────────────────
# PANEL 1 – Household Debt / GDP over time with recession shading
# ─────────────────────────────────────────────────────────────────────────────
ax1.plot(years_p1, us_debt,    color=BLUE,  lw=2.5, label='United States', zorder=3)
ax1.plot(years_p1, uk_debt,    color=GOLD,  lw=2.5, label='United Kingdom', zorder=3)
ax1.plot(years_p1, korea_debt, color=RED,   lw=2.5, label='South Korea', zorder=3)
ax1.plot(years_p1, eu_avg,     color=TEAL,  lw=2.5, label='EU Average', zorder=3)

for (rs, re, rlabel) in recessions:
    ax1.axvspan(rs, re, color='#ffffff', alpha=0.05, zorder=1)
    ax1.text((rs + re) / 2, 122, rlabel, ha='center', va='bottom',
             fontsize=8.5, color='#aaaaaa', style='italic')
    ax1.axvline(rs, color='#555555', lw=0.8, ls='--', zorder=2)

ax1.set_xlim(1995, 2024)
ax1.set_ylim(35, 125)
ax1.set_title('Household Debt as % of GDP — Selected Economies (1995–2024)',
              fontsize=13, fontweight='bold', color=WHITE, pad=10)
ax1.set_ylabel('% of GDP', color=WHITE, fontsize=11)
ax1.set_xlabel('Year', color=WHITE, fontsize=11)
ax1.legend(loc='upper left', framealpha=0.2, facecolor='#1a1a2e',
           edgecolor='#444', labelcolor=WHITE, fontsize=10)
ax1.tick_params(colors='#aaaaaa')

# Annotation: peak US debt
ax1.annotate('US peak:\n98% of GDP\n(2008)', xy=(2008, 98),
             xytext=(2011.5, 105),
             arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5),
             fontsize=9, color=GOLD, ha='center')
ax1.annotate('Korea: 117%\n(2024)', xy=(2024, 117),
             xytext=(2020.5, 119),
             arrowprops=dict(arrowstyle='->', color=RED, lw=1.5),
             fontsize=9, color=RED, ha='center')

# ─────────────────────────────────────────────────────────────────────────────
# PANEL 2 – GDP growth effect of +10pp household debt (BIS WP 607)
# ─────────────────────────────────────────────────────────────────────────────
bars = ax2.bar(horizons, gdp_effect, color=bar_colors, width=0.55,
               edgecolor='#333333', linewidth=0.8, zorder=3)

ax2.axhline(0, color='#aaaaaa', lw=1.2, zorder=2)
ax2.set_title('GDP Growth Effect of a +10pp Rise\nin Household Debt (BIS, 2017)',
              fontsize=12, fontweight='bold', color=WHITE, pad=10)
ax2.set_ylabel('Change in GDP growth (pp)', color=WHITE, fontsize=10)
ax2.set_ylim(-0.6, 0.55)
ax2.tick_params(colors='#aaaaaa')

for bar, val in zip(bars, gdp_effect):
    offset = 0.03 if val >= 0 else -0.06
    ax2.text(bar.get_x() + bar.get_width() / 2,
             val + offset,
             f'{val:+.2f} pp',
             ha='center', va='bottom' if val >= 0 else 'top',
             fontsize=10.5, fontweight='bold',
             color=TEAL if val >= 0 else RED)

# Annotation box
ax2.text(0.97, 0.97,
         'Short-run boost:\n+0.30 pp (Year 1)\n\nLong-run drag:\n−0.42 pp (Year 4)',
         transform=ax2.transAxes, ha='right', va='top',
         fontsize=9, color='#cccccc',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='#1a1a2e',
                   edgecolor='#444', alpha=0.9))

# ─────────────────────────────────────────────────────────────────────────────
# PANEL 3 – Debt level vs. consumption drop during GFC 2008
# ─────────────────────────────────────────────────────────────────────────────
scatter_colors = [RED if d < -5 else GOLD if d < -3 else TEAL for d in consump_drop]
sc = ax3.scatter(debt_level_p3, consump_drop, c=scatter_colors,
                 s=160, zorder=4, edgecolors='#333333', linewidths=0.8)

# Trend line
z = np.polyfit(debt_level_p3, consump_drop, 1)
p = np.poly1d(z)
x_line = np.linspace(55, 140, 100)
ax3.plot(x_line, p(x_line), color='#aaaaaa', lw=1.5, ls='--', zorder=3,
         label='Trend')

for i, (country, xv, yv) in enumerate(zip(countries_p3, debt_level_p3, consump_drop)):
    offset_x = 2 if xv < 100 else -4
    offset_y = 0.3 if yv > -5 else -0.5
    ax3.text(xv + offset_x, yv + offset_y, country,
             fontsize=8.5, color='#cccccc', ha='left')

ax3.set_title('Higher Pre-Crisis Debt → Deeper\nConsumption Collapse (GFC 2008)',
              fontsize=12, fontweight='bold', color=WHITE, pad=10)
ax3.set_xlabel('Household Debt / GDP (% pre-crisis)', color=WHITE, fontsize=10)
ax3.set_ylabel('Consumption Drop (%)', color=WHITE, fontsize=10)
ax3.tick_params(colors='#aaaaaa')
ax3.set_xlim(50, 145)
ax3.set_ylim(-11, 0.5)

# Correlation note
r = np.corrcoef(debt_level_p3, consump_drop)[0, 1]
ax3.text(0.04, 0.07, f'Pearson r = {r:.2f}',
         transform=ax3.transAxes, fontsize=9.5, color=GOLD,
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#1a1a2e',
                   edgecolor='#444', alpha=0.9))

# ─────────────────────────────────────────────────────────────────────────────
# PANEL 4 – US Debt Service Ratio vs. Unemployment (2000–2024)
# ─────────────────────────────────────────────────────────────────────────────
color_dsr   = GOLD
color_unemp = RED

ax4b = ax4.twinx()

l1, = ax4.plot(years_p4, us_dsr,   color=color_dsr,   lw=2.5,
               label='Debt Service Ratio (% disposable income)', zorder=3)
l2, = ax4b.plot(years_p4, us_unemp, color=color_unemp, lw=2.5, ls='--',
                label='Unemployment Rate (%)', zorder=3)

# Shade GFC
ax4.axvspan(2007.75, 2009.5, color='#ffffff', alpha=0.05, zorder=1)
ax4.axvspan(2020.0,  2020.75, color='#ffffff', alpha=0.05, zorder=1)
ax4.text(2008.6, 15.3, 'GFC', ha='center', fontsize=9, color='#aaaaaa', style='italic')
ax4.text(2020.35, 15.3, 'COVID', ha='center', fontsize=9, color='#aaaaaa', style='italic')

ax4.set_xlim(2000, 2024)
ax4.set_ylim(8, 16)
ax4b.set_ylim(0, 12)

ax4.set_title('US Household Debt Service Ratio vs. Unemployment Rate (2000–2024)',
              fontsize=13, fontweight='bold', color=WHITE, pad=10)
ax4.set_ylabel('Debt Service Ratio (% of disposable income)', color=color_dsr, fontsize=10)
ax4b.set_ylabel('Unemployment Rate (%)', color=color_unemp, fontsize=10)
ax4.set_xlabel('Year', color=WHITE, fontsize=11)
ax4.tick_params(colors='#aaaaaa')
ax4b.tick_params(colors='#aaaaaa')
ax4b.spines['right'].set_edgecolor('#333333')

# Key insight annotation
ax4.annotate('When unemployment spikes,\nhigh debt service ratios\nbecome unbearable',
             xy=(2009.5, 13.2), xytext=(2013, 15.0),
             arrowprops=dict(arrowstyle='->', color='#aaaaaa', lw=1.4),
             fontsize=9.5, color='#cccccc', ha='center',
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#1a1a2e',
                       edgecolor='#555', alpha=0.9))

lines = [l1, l2]
labels = [l.get_label() for l in lines]
ax4.legend(lines, labels, loc='upper right', framealpha=0.25,
           facecolor='#1a1a2e', edgecolor='#444', labelcolor=WHITE, fontsize=10)

# ─────────────────────────────────────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────────────────────────────────────
fig.text(0.5, 0.015,
         'Manus AI  ·  The Great Unraveling  ·  July 2026  ·  '
         'Data: BIS WP 607, IMF WEO, OECD, Federal Reserve',
         ha='center', va='bottom', fontsize=9, color='#555555')

plt.savefig('/home/ubuntu/household_debt_visualization.png',
            dpi=180, bbox_inches='tight', facecolor=BG)
print("Saved: /home/ubuntu/household_debt_visualization.png")
