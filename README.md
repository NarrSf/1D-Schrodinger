# 1D Schrödinger Equation Numerical Solver

A robust Python implementation to solve the **Time-Independent Schrödinger Equation (TISE)** for various potential wells using the **Finite Difference Method**.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen.svg)

## 📖 Introduction

This project solves the one-dimensional Schrödinger equation:
$$\hat{H}\psi(x) = E\psi(x)$$
where the Hamiltonian is defined as:
$$\hat{H} = -\frac{\hbar^2}{2m} \frac{d^2}{dx^2} + V(x)$$

By discretizing the spatial domain, the differential equation is transformed into a **Matrix Eigenvalue Problem**, allowing us to find the quantized energy levels ($E_n$) and their corresponding wavefunctions ($\psi_n$).

## 🚀 Features

* **Finite Difference Engine:** Converts the kinetic energy operator into a tridiagonal matrix.
* **Automated Visualization:** Overlays wavefunctions on top of their respective energy levels.
* **Physical Phenomena:** Clear demonstration of **Zero-Point Energy** and **Quantum Tunneling**.
* **Modular Potential:** Easily switch between Harmonic Oscillator, Square Wells, or custom functions.

## 🛠️ Installation & Requirements

Ensure you have Python installed. You can install the necessary libraries using pip:

```bash
pip install numpy scipy matplotlib
