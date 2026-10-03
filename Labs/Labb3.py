import numpy as np
import matplotlib.pyplot as plt

# --- Parametrar från instruktionen ---
R = 0.155    # Spolens radie i meter 
N = 150      # Antal varv 
I = 0.995    # Ström i Ampere 
mu0_4pi = 1e-7

def calculate_Bz(xp, yp, zp, R, I, N, Ntheta=200):
    P = np.array([xp, yp, zp])
    deltatheta = 2 * np.pi / Ntheta
    theta = np.arange(Ntheta) * deltatheta
    B_sum = np.zeros(3)
    
    for t in theta:
        # Position av strömelement ds
        r_source = np.array([R * np.cos(t), R * np.sin(t), 0])
        r = P - r_source
        ds = deltatheta * np.array([-R * np.sin(t), R * np.cos(t), 0])
        
        # Biot-Savarts lag (numerisk del) 
        dB_part = I * np.cross(ds, r) / np.linalg.norm(r)**3
        B_sum += dB_part
        
    B_tesla = mu0_4pi * N * B_sum
    return B_tesla[2] * 10000  # Returnerar z-komponenten i Gauss

# --- Era mätdata ---
# x-positioner i cm
x_exp_cm = np.array([0, 2, 4, 6, 8, 10, 18, 20, -3, -5, -7, -9, -11, -13, -19, -21])
# Utsignal i mV
u_exp_mv = np.array([29.1, 28.7, 30.5, 32.5, 36.2, 42.1, -20.5, -14.0, 30.2, 31.7, 34.0, 38.7, 46.4, 59.6, -25.1, -15.1])

# Konvertering till Gauss (5 mV/G) 
B_exp_gauss = u_exp_mv / 5.0

# --- Skapa teoretisk kurva ---
x_theory_m = np.linspace(-0.25, 0.25, 500)
B_theory = [calculate_Bz(x, 0, 0, R, I, N) for x in x_theory_m]

# --- Plotting ---
plt.figure(figsize=(10, 6))
plt.plot(x_theory_m * 100, B_theory, 'b-', label='Teoretisk kurva (Biot-Savart)')
plt.plot(x_exp_cm, B_exp_gauss, 'ro', label='Era mätvärden (Gauss)')

# Justera vyn för att se detaljerna (undviker oändliga spikar vid x=R)
plt.ylim([-10, 20]) 
plt.axhline(0, color='black', lw=1, ls='--')
plt.axvline(0, color='black', lw=1, ls='--')
plt.xlabel('Position x [cm]')
plt.ylabel('Magnetisk flödestäthet $B_z$ [Gauss]')
plt.title('Jämförelse: Mätdata vs Teori längs x-axeln')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()