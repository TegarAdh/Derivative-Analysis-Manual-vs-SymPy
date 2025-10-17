# Derivative-Analysis-Manual-vs-SymPy

# Function Derivatives with Python and SymPy

This project demonstrates **manual and computational approaches** to finding derivatives of mathematical functions using **Python’s SymPy library**.  
It also includes a visualization of the **tangent** and **normal lines** at a specific point on the curve.

---

## 📘 Project Overview

The goal of this project is to:
- Calculate function derivatives **manually** and **verify** them using Python.
- Visualize the relationship between a function, its **derivative**, and the **tangent/normal lines**.
- Provide clear examples for educational purposes in **Calculus** and **Symbolic Computation**.

---

## 🧮 Features

- Symbolic differentiation using `sympy.diff()`
- Simplification of derivative expressions with `sympy.simplify()`
- Visualization using `matplotlib`
- Tangent and normal line plotting at a given point
- Examples of 10 derivative problems with both manual and computational solutions

---

## 🧠 Example Code

```python
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define variable and function
x = sp.Symbol('x')
f = x**2  # Change this to your desired function

# Derivative
f_prime = sp.diff(f, x)

# Tangent & Normal at x = a
a = 1
fa = f.subs(x, a)
m_tangent = f_prime.subs(x, a)
tangent_eq = m_tangent*(x - a) + fa
normal_eq = (-1/m_tangent)*(x - a) + fa

# Convert to numerical functions
f_num = sp.lambdify(x, f, 'numpy')
tangent_num = sp.lambdify(x, tangent_eq, 'numpy')
normal_num = sp.lambdify(x, normal_eq, 'numpy')

# Plot
x_vals = np.linspace(-2, 3, 400)
plt.figure(figsize=(8,6))
plt.plot(x_vals, f_num(x_vals), label="f(x)", color="blue")
plt.plot(x_vals, tangent_num(x_vals), label="Tangent Line", color="red", linestyle="--")
plt.plot(x_vals, normal_num(x_vals), label="Normal Line", color="green", linestyle=":")
plt.scatter([a], [fa], color="black", label=f"Point ({a},{fa})")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.legend()
plt.title("Function Derivative, Tangent, and Normal Line")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
```
## 📊 Example Output

Below is an example of the function, its tangent, and normal line plotted using Matplotlib:

<p align="center"> <img src="images/derivative_plot.png" alt="Derivative Graph Example" width="600"/> </p>
---
## 🔧 Requirements

Make sure you have Python 3 installed and the following packages:
```
pip install sympy numpy matplotlib
```

## 🚀 How to Run
1. Clone this repository
   ```
   git clone https://github.com/TegarAdh/Function-Derivatives-with-Python-and-SymPy.git
   cd Function-Derivatives-with-Python-and-SymPy
   ```
2. Run the Python script
   ```
   python derivative_plot.py
   ```
3. Modify the variable f = ... in the code to test different functions.

---
## 🧾 Example Functions
| No. | Function ( f(x) )                | Manual Derivative ( f'(x) )             |
| --- | -------------------------------- | --------------------------------------- |
| 1   | ( 5x^3 )                         | ( 15x^2 )                               |
| 2   | ( 7 )                            | ( 0 )                                   |
| 3   | ( 4x^2 + 3x - 2 )                | ( 8x + 3 )                              |
| 4   | ( (x^2 + 1)(x^3 - 2x) )          | ( 5x^4 - 3x^2 - 2 )                     |
| 5   | ( \frac{x^2 + 3}{(x^2 + 1)^2} )  | ( -\frac{2x(x^2 + 5)}{(x^2 + 1)^3} )    |
| 6   | ( (3x^2 + 1)^5 )                 | ( 30x(3x^2 + 1)^4 )                     |
| 7   | ( (x^2 + 2)(x^2 - 1) )           | ( 4x^3 + 2x )                           |
| 8   | ( \frac{2x^3}{x^2 + 1} )         | ( \frac{2x^2(x^2 + 3)}{(x^2 + 1)^2} )   |
| 9   | ( (x^2 + 1)^3(x^3 - 2) )         | ( 3(x^2 + 1)^2(3x^4 + x^2 - 4x) )       |
| 10  | ( \frac{x^3 + 2x}{(x^2 + 1)^2} ) | ( -\frac{x^4 + 3x^2 - 2}{(x^2 + 1)^3} ) |

## 📚 References
- [SymPy Documentation](https://docs.sympy.org/latest/index.html)
- [NumPy Documentation](https://numpy.org/doc/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Python Official Website](https://www.python.org/)
- [Markdown Syntax Guide](https://www.markdownguide.org/basic-syntax/)

## 👨‍💻 Author
Tegar Adhi Nugraha Christ During
[Tegar](https://github.com/TegarAdh)
🗓️ Created: October 2025
