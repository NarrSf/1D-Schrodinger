1D Schrödinger Equation Solver: Numerical Analysis
This repository contains a Python-based numerical solver for the Time-Independent Schrödinger Equation (TISE) in one dimension. Using the Finite Difference Method, the project visualizes quantum states and energy eigenvalues for various potential wells.

🚀 Overview
The solver discretizes the Hamiltonian operator into a matrix form (H=T+V) and solves the resulting eigenvalue problem:

H
^
 ψ=Eψ
By calculating the eigenvectors and eigenvalues of the Hamiltonian matrix, we can determine the allowed energy levels and the corresponding wavefunctions for any given potential V(x).

✨ Key Features
Numerical Engine: Uses scipy.linalg.eigh for efficient and accurate computation of Hermitian matrices.

Physical Insights: * Calculates Zero-Point Energy.

Demonstrates Quantum Tunneling into classically forbidden regions.

Visualizes Wavefunction Nodes corresponding to higher energy states.

Customizable Potentials: Easily switch between:

Quantum Harmonic Oscillator (QHO)

Infinite/Finite Square Well

Anharmonic Potentials (e.g., V(x)= 
2
1
​	
 kx 
2
 +λx 
4
 )

🛠️ Tech Stack
Python 3.x

NumPy: For matrix operations and grid discretization.

SciPy: For solving the linear algebra eigenvalue problem.

Matplotlib: For high-quality physics-based visualizations.

📊 Results
The solver accurately predicts the equidistant energy levels for the Harmonic Oscillator:

E 
n
​	
 =(n+ 
2
1
​	
 )ℏω

As seen in the generated plots, the wavefunctions exhibit the expected parity and nodal structure.
