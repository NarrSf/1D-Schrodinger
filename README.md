# 1D Schrödinger Equation Numerical Solver

A professional Python-based simulation to solve and visualize the **Time-Independent Schrödinger Equation (TISE)** for various quantum potential wells using the **Finite Difference Method**.

## Overview

This project provides a numerical solution to the fundamental equation of quantum mechanics in one dimension:
$$\hat{H}\psi(x) = E\psi(x)$$
By transforming the differential Hamiltonian operator into a discrete matrix, we can compute the quantized energy levels ($E_n$) and the corresponding probability amplitudes ($\psi_n$) for particles trapped in different potentials.

## Key Features

* **Numerical Engine:** Efficiently solves the eigenvalue problem using `scipy.linalg.eigh`.
* **Physics Visualization:** * Plots wavefunctions ($\psi$) directly on their corresponding energy levels.
    * Demonstrates **Zero-Point Energy** (non-zero ground state).
    * Visualizes **Quantum Tunneling** into classically forbidden regions.
* **Modular Design:** Supports various potentials including:
    * Quantum Harmonic Oscillator (QHO)
    * Infinite/Finite Square Wells
    * Custom Anharmonic Potentials

## How It Works (Technical Breakdown)

### 1. Spatial Discretization
The continuous 1D space is mapped onto a discrete grid of $N$ points. 
* **Grid Spacing ($dx$):** Defines the resolution of the simulation.
* **Domain ($L$):** Sets the physical boundaries (e.g., from $-L/2$ to $+L/2$).

### 2. Matrix Hamiltonian ($H = T + V$)
The solver represents physical operators as square matrices:
* **Kinetic Energy ($T$):** Approximated using the **Second-Order Central Difference** method, resulting in a tridiagonal matrix.
* **Potential Energy ($V$):** A diagonal matrix where each entry $V_{ii}$ represents the potential at position $x_i$.

### 3. Solving the Physics
The script finds the **Eigenvalues** (allowed energies) and **Eigenvectors** (wavefunctions) of the $H$ matrix. To make the results intuitive, wavefunctions are scaled and vertically offset by their respective energy levels in the final plot.

