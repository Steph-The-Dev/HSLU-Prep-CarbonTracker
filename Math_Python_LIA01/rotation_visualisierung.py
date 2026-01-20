"""
Visualisierung einer 2D-Rotationsmatrix mit NumPy und Matplotlib
================================================================
Dieses Skript zeigt, wie ein Vektor um 45 Grad gedreht wird.
"""

import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# 1. ROTATIONSMATRIX ERSTELLEN
# =============================================================================

def erstelle_rotationsmatrix(winkel_grad):
    """
    Erstellt eine 2x2 Rotationsmatrix für einen gegebenen Winkel.
    
    Parameter:
        winkel_grad: Drehwinkel in Grad (positiv = gegen Uhrzeigersinn)
    
    Rückgabe:
        2x2 NumPy Array (Rotationsmatrix)
    """
    winkel_rad = np.radians(winkel_grad)
    
    cos_theta = np.cos(winkel_rad)
    sin_theta = np.sin(winkel_rad)
    
    R = np.array([
        [cos_theta, -sin_theta],
        [sin_theta,  cos_theta]
    ])
    
    return R

# =============================================================================
# 2. HAUPTPROGRAMM
# =============================================================================

# Winkel festlegen
WINKEL = 45  # Grad

# Rotationsmatrix berechnen
R = erstelle_rotationsmatrix(WINKEL)

print("=" * 50)
print(f"Rotationsmatrix für {WINKEL}°:")
print("=" * 50)
print(R)
print()

# Original-Vektor definieren (zeigt nach rechts)
original_vektor = np.array([1, 0])

# Vektor drehen
gedrehter_vektor = R @ original_vektor

print(f"Original-Vektor:     {original_vektor}")
print(f"Gedrehter Vektor:    {gedrehter_vektor}")
print()

# =============================================================================
# 3. VISUALISIERUNG
# =============================================================================

# Figure erstellen mit dunklem Stil
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 10))

# Hintergrund anpassen
fig.patch.set_facecolor('#1a1a2e')
ax.set_facecolor('#16213e')

# Koordinatensystem zeichnen
ax.axhline(y=0, color='#4a5568', linestyle='-', linewidth=0.8, alpha=0.5)
ax.axvline(x=0, color='#4a5568', linestyle='-', linewidth=0.8, alpha=0.5)

# Gitter hinzufügen
ax.grid(True, alpha=0.2, color='#4a5568')

# Einheitskreis zeichnen (zur Orientierung)
theta = np.linspace(0, 2*np.pi, 100)
ax.plot(np.cos(theta), np.sin(theta), 
        color='#718096', linestyle='--', linewidth=1, alpha=0.5, 
        label='Einheitskreis')

# Original-Vektor zeichnen (cyan)
ax.quiver(0, 0, original_vektor[0], original_vektor[1],
          angles='xy', scale_units='xy', scale=1,
          color='#00d4ff', width=0.02, 
          label=f'Original: [{original_vektor[0]}, {original_vektor[1]}]')

# Gedrehter Vektor zeichnen (magenta/pink)
ax.quiver(0, 0, gedrehter_vektor[0], gedrehter_vektor[1],
          angles='xy', scale_units='xy', scale=1,
          color='#ff6b9d', width=0.02,
          label=f'Gedreht ({WINKEL}°): [{gedrehter_vektor[0]:.3f}, {gedrehter_vektor[1]:.3f}]')

# Rotationsbogen zeichnen
winkel_bogen = np.linspace(0, np.radians(WINKEL), 30)
bogen_radius = 0.3
ax.plot(bogen_radius * np.cos(winkel_bogen), 
        bogen_radius * np.sin(winkel_bogen),
        color='#ffd93d', linewidth=2, label=f'Drehwinkel: {WINKEL}°')

# Winkel-Text
ax.annotate(f'{WINKEL}°', 
            xy=(0.25, 0.12), 
            fontsize=14, 
            color='#ffd93d',
            fontweight='bold')

# Achsen-Einstellungen
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')

# Titel und Labels
ax.set_title(f'2D-Rotationsmatrix: Drehung um {WINKEL}°', 
             fontsize=18, fontweight='bold', color='white', pad=20)
ax.set_xlabel('X-Achse', fontsize=12, color='white')
ax.set_ylabel('Y-Achse', fontsize=12, color='white')

# Legende
legend = ax.legend(loc='upper left', fontsize=11, 
                   facecolor='#1a1a2e', edgecolor='#4a5568')
for text in legend.get_texts():
    text.set_color('white')

# Rotationsmatrix als Text im Plot anzeigen
matrix_text = f"""Rotationsmatrix R({WINKEL}°):
┌                      ┐
│ {R[0,0]:7.4f}  {R[0,1]:7.4f} │
│ {R[1,0]:7.4f}  {R[1,1]:7.4f} │
└                      ┘

Berechnung:
v' = R · v
[{gedrehter_vektor[0]:.4f}]   [{R[0,0]:.4f}  {R[0,1]:.4f}]   [{original_vektor[0]}]
[{gedrehter_vektor[1]:.4f}] = [{R[1,0]:.4f}  {R[1,1]:.4f}] · [{original_vektor[1]}]"""

ax.text(0.98, 0.02, matrix_text, 
        transform=ax.transAxes, 
        fontsize=10, 
        fontfamily='monospace',
        color='#a0aec0',
        verticalalignment='bottom',
        horizontalalignment='left',
        bbox=dict(boxstyle='round,pad=0.5', 
                  facecolor='#1a1a2e', 
                  edgecolor='#4a5568',
                  alpha=0.9))

plt.tight_layout()
plt.savefig('rotation_visualisierung.png', dpi=150, facecolor='#1a1a2e')
plt.show()

print("=" * 50)
print("✓ Visualisierung gespeichert als 'rotation_visualisierung.png'")
print("=" * 50)
