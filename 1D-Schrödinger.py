import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh

# 1. Spatial Grid Setup
N = 1000                  # Number of grid points
L = 10.0                  # Physical length of the domain
x = np.linspace(-L/2, L/2, N)
dx = x[1] - x[0]          # Grid spacing

# 2. Define the Potential Energy V(x)
# Example: Quantum Harmonic Oscillator (V = 0.5 * k * x^2)
k = 100
V = 0.5 * k * x**2 

# 3. Construct the Hamiltonian Matrix (H = T + V)
# Finite Difference approximation for the kinetic energy operator (T)
# Using natural units where h_bar = 1 and m = 1
main_diag = np.ones(N) * (-2)
off_diag = np.ones(N-1) * 1
T = (-0.5 / dx**2) * (np.diag(main_diag) + np.diag(off_diag, 1) + np.diag(off_diag, -1))

# Combine Kinetic (T) and Potential (V) energies
# V is added to the main diagonal of the Hamiltonian
H = T + np.diag(V)

# 4. Solve the Eigenvalue Problem
# eigh is optimized for symmetric/Hermitian matrices
energies, wavefunctions = eigh(H)

# 5. Visualization
plt.figure(figsize=(12, 8))

# Scale factor to amplify wavefunction amplitude for better visibility on the energy scale
scale = 10.0 

# Plot the first 4 eigenstates
for i in range(4):
    psi = wavefunctions[:, i]
    line = plt.plot(x, psi * scale + energies[i], label=f'n={i} (E={energies[i]:.2f})')
    plt.axhline(y=energies[i], color=line[0].get_color(), linestyle='--', alpha=0.3)

# Plot the Potential Well profile
plt.plot(x, V, 'k', linewidth=2, label='Potential V(x)', alpha=0.8)

# Formatting the plot
plt.ylim(-2, energies[3] + 10) 
plt.title("Numerical Solution of 1D Schrödinger Equation", fontsize=14)
plt.xlabel("Position (x)", fontsize=12)
plt.ylabel("Energy / Amplitude", fontsize=12)
plt.legend(loc='upper right')
plt.grid(True, which='both', linestyle=':', alpha=0.6)

plt.show()