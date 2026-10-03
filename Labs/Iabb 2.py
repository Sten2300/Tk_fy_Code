import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# --- 1. KONSTANTER ---
EPSILON_0 = 8.854187e-12
AREA_M2 = 0.1 * 0.1 * np.pi  # 0.0314 m^2

# --- 2. MÄTDATA ---
# Serie 1 (Plattor: u = mm, C = nF)
u1_mm = np.array([2.16, 3.18, 4.20, 5.05, 6.32, 7.35, 8.57, 9.97, 11.23])
C1_F = np.array([0.357, 0.222, 0.158, 0.148, 0.139, 0.128, 0.108, 0.098, 0.095]) * 1e-9

# Serie 2 (Vatten: u = mm, C = pF)
# Outlier vid 122 mm är exkluderad för att få en rättvisande linjär lutning k
u2_mm = np.array([0, 40, 65, 90, 115, 140, 166, 216])
C2_pF = np.array([23.1, 29.0, 37.4, 47.1, 58.0, 68.5, 78.1, 90.4])

# --- 3. BERÄKNINGAR OCH REGRESSION ---

# Serie 1: C = k1 * (1/u) + C0
def model1(u, k, C0):
    return k * (1/u) + C0

popt1, _ = curve_fit(model1, u1_mm, C1_F)
k1 = popt1[0]
eps_r1 = (k1 * 1e-3) / (EPSILON_0 * AREA_M2)

# Serie 2: C = k2 * u + C0 (Linjär mot höjd)
def model2(u, k, C0):
    return k * u + C0

popt2, _ = curve_fit(model2, u2_mm, C2_pF)
k2 = popt2[0]  # Enhet: pF/mm

# --- 4. UTSKRIFT AV RESULTAT ---
print("=== SLUTGILTIGA RESULTAT ===")
print(f"SERIE 1 (Plattor):")
print(f"  k1 (inverterad lutning): {k1:.4e} F*mm")
print(f"  Epsilon_r:               {eps_r1:.3f}")

print(f"\nSERIE 2 (Vattennivå):")
print(f"  k (lutning per höjd):    {k2:.4f} pF/mm")
print(f"  Bas-kapacitans (C0):     {popt2[1]:.2f} pF")

# --- 5. VISUALISERING ---
plt.figure(figsize=(12, 5))

# Graf Serie 1
plt.subplot(1, 2, 1)
plt.scatter(1/u1_mm, C1_F * 1e9, color='blue', label='Mätdata')
plt.plot(1/u1_mm, model1(u1_mm, *popt1) * 1e9, 'r-', label='Regression')
plt.title('Serie 1: Kapacitans vs 1/u')
plt.xlabel('1/u [1/mm]')
plt.ylabel('C [nF]')
plt.grid(True)

# Graf Serie 2
plt.subplot(1, 2, 2)
plt.scatter(u2_mm, C2_pF, color='green', label='Mätdata')
plt.plot(u2_mm, model2(u2_mm, *popt2), 'r-', label=f'k = {k2:.3f} pF/mm')
plt.title('Serie 2: Kapacitans vs Vattennivå')
plt.xlabel('Vattenhöjd u [mm]')
plt.ylabel('C [pF]')
plt.grid(True)

plt.tight_layout()
plt.show()