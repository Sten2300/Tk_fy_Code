import numpy as np
import matplotlib.pyplot as plt

# Parametrar baserade på labborationen (ekvation 8)
L = 75e-3      # Induktans: 75 mH
C = 1e-9       # Kapacitans: 1 nF
Rs = 100       # Motstånd: 100 Ohm
Ri = 50        # Generatorns utresistans
RL = 40        # Antaget inre motstånd i spolen (exempelvärde)
R_tot = Rs + Ri + RL

# Beräkna konstanter enligt labhandledningen[cite: 1]
tau = 2 * L / R_tot                         # Tidskonstanten tau = 2L/R[cite: 1]
omega = np.sqrt(1/(L*C) - (R_tot/(2*L))**2) # Vinkelfrekvensen omega[cite: 1]

# Tidsaxel (0 till 5 tidskonstanter för att se dämpningen tydligt)
t = np.linspace(0, 5 * tau, 1000)

# Signalen: i(t) = A * exp(-t/tau) * sin(omega * t)[cite: 1]
A = 1 # Amplitud (normaliserad)
i = A * np.exp(-t/tau) * np.sin(omega * t)

# Höljet (Envelopes)[cite: 1]
envelope_upper = A * np.exp(-t/tau)
envelope_lower = -A * np.exp(-t/tau)

# Skapa grafen
plt.figure(figsize=(10, 6))
plt.plot(t, i, label='Dämpad svängning $i(t)$', color='blue')
plt.plot(t, envelope_upper, '--', color='red', alpha=0.5, label='Hölje $e^{-t/\\tau}$')
plt.plot(t, envelope_lower, '--', color='red', alpha=0.5)

# Formatering
plt.title('Harmonisk svängning i RLC-krets (Uppgift 6.4)')
plt.xlabel('Tid (s)')
plt.ylabel('Ström / Spänning (relativ)')
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.axhline(0, color='black', lw=1)
plt.legend()

# Visa grafen
plt.show()