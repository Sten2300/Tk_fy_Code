import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# --- 1. TEORETISKA BERÄKNINGAR ---
R_ohm = 1e6      # Ändra till din resistans i Ohm
C_farad = 10e-6  # Ändra till din kapacitans i Farad (t.ex. 10uF = 10e-6)

tau_theo = R_ohm * C_farad
t_half_theo = tau_theo * np.log(2)

print("--- TEORETISKA VÄRDEN ---")
print(f"Teoretisk tau: {tau_theo:.4f} s")
print(f"Teoretisk t1/2: {t_half_theo:.4f} s")

# --- 2. EXPERIMENTELL REGRESSION (Om du har mätpunkter) ---
# t_data = sekunder, V_data = spänning (Volt)
t_data = np.array([0, 1, 2, 3, 4, 5, 10]) # Exempeldata
V_data = np.array([10.0, 9.0, 8.1, 7.3, 6.6, 6.0, 3.7]) # Exempeldata

def discharge_model(t, V0, tau):
    return V0 * np.exp(-t / tau)

# Vi gör en gissning på tau för att hjälpa algoritmen
popt, _ = curve_fit(discharge_model, t_data, V_data, p0=[V_data[0], tau_theo])
V0_fit, tau_exp = popt
t_half_exp = tau_exp * np.log(2)

print(f"\n--- EXPERIMENTELLA RESULTAT ---")
print(f"Beräknad tau från mätdata: {tau_exp:.4f} s")
print(f"Beräknad t1/2 från mätdata: {t_half_exp:.4f} s")

# --- 3. VISUALISERING ---
plt.figure(figsize=(8, 5))
plt.scatter(t_data, V_data, color='blue', label='Mätpunkter')
t_fine = np.linspace(0, max(t_data), 100)
plt.plot(t_fine, discharge_model(t_fine, *popt), 'r-', label=f'Regression (tau={tau_exp:.2f}s)')
plt.axvline(tau_exp, color='green', linestyle='--', label='tau (37%)')
plt.axvline(t_half_exp, color='orange', linestyle='--', label='t1/2 (50%)')

plt.xlabel('Tid [s]')
plt.ylabel('Spänning [V]')
plt.title('Urladdning av kondensator - RC-krets')
plt.legend()
plt.grid(True)
plt.show()