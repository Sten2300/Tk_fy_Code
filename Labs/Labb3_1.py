import numpy as np
import matplotlib.pyplot as plt

# --- Parametrar från instruktionen ---
R = 0.155    # Radie i meter 
N = 150      # Antal varv 
I = 0.995     # uppmätt ström
mu0_4pi = 1e-7

def calculate_Bz_axis(zp, R, I, N, Ntheta=200):
    # Förenklad Biot-Savart för punkter enbart på z-axeln
    # B = (mu0 * N * I * R^2) / (2 * (R^2 + z^2)^(3/2))
    B_tesla = (4 * np.pi * mu0_4pi * N * I * R**2) / (2 * (R**2 + zp**2)**(1.5))
    return B_tesla * 10000  # Konvertera till Gauss 

# --- Dina mätdata för z-axeln (Rådata i den ordning de togs) ---
z_raw = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, -2, -4, -6, -8, -10, -12, -14, -16]) + 1.7 #nollnivå satt 1.7 cm från noll
u_raw = np.array([29.2, 27.7, 24.9, 21.7, 18.6, 15.5, 13.1, 10.7, 9.0, 29.5, 28.5, 26.1, 22.9, 19.9, 16.8, 13.9, 11.6])

# --- SORTERING AV ARRAYERNA ---
# Detta indexerar om dina data så att de går från -16 till +16 sekventiellt
idx = np.argsort(z_raw)
z_exp_cm = z_raw[idx]
u_exp_mv = u_raw[idx]

# Konvertering till Gauss baserat på 5 mV/G 
B_exp_gauss = u_exp_mv / 5.0  

# --- Data från testelever (Tabell 1 i instruktionen) ---
z_others = np.array([-20, -15, -10, -5, 0, 5, 10, 15, 20])
u_emil = np.array([5.4, 8.7, 14.5, 22.6, 30.0, 29.4, 21.9, 14.1, 8.6]) 
u_bjorn = np.array([3.1, 1.3, 8.2, 16.4, 20.0, 41.1, 28.2, 21.3, 17.1]) 
u_agnes = np.array([5.7, 9.8, 16.6, 25.3, 29.1, 24.5, 15.4, 9.3, 5.7]) 

# --- PLOT 1: Teoretisk jämförelse ---
z_theory_m = np.linspace(-0.25, 0.25, 200)
B_theory = [calculate_Bz_axis(z, R, I, N) for z in z_theory_m]

plt.figure(figsize=(10, 5))
plt.plot(z_theory_m * 100, B_theory, 'b-', label='Teori (Biot-Savart)')
plt.scatter(z_exp_cm, B_exp_gauss, color='red', label='mätdata')
plt.title('Figur 6: Mätresultat $B(z)$ vs Teoretisk modell')
plt.xlabel('Position z [cm]')
plt.ylabel('Magnetisk flödestäthet [Gauss]')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()

# --- PLOT 2: Jämförelse med andra elever ---
plt.figure(figsize=(10, 5))
plt.plot(z_exp_cm, u_exp_mv, 'ro-', label='Data (sorterad)')
plt.plot(z_others, u_emil, 'g--s', label='Emil', alpha=0.7)
plt.plot(z_others, u_bjorn, 'k--x', label='Björn', alpha=0.7)
plt.plot(z_others, u_agnes, 'm--d', label='Agnes', alpha=0.7)
plt.title('Figur 7: Jämförelse med Emils, Björns och Agnes data')
plt.xlabel('Position z [cm]')
plt.ylabel('Utsignal $U_{ut}$ [mV]')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()