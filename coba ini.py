import sympy as sp

# Definisi variabel
x = sp.Symbol('x')

# 1
f1 = 5*x**3
f1_prime = sp.diff(f1, x)
print("Soal 1:")
print("f(x) =", f1)
print("f'(x) =", f1_prime)
print()

# 2
f2 = 7
f2_prime = sp.diff(f2, x)
print("Soal 2:")
print("f(x) =", f2)
print("f'(x) =", f2_prime)
print()

# 3
f3 = 4*x**2 + 3*x - 2
f3_prime = sp.diff(f3, x)
print("Soal 3:")
print("f(x) =", f3)
print("f'(x) =", f3_prime)
print()

# 4
f4 = (x**2 + 1)*(x**3 - 2*x)
f4_prime = sp.diff(f4, x)
print("Soal 4:")
print("f(x) =", f4)
print("f'(x) =", sp.simplify(f4_prime))
print()

# 5
f5 = (x**2 + 3)/(x**2 + 1)**2
f5_prime = sp.diff(f5, x)
print("Soal 5:")
print("f(x) =", f5)
print("f'(x) =", sp.simplify(f5_prime))
print()

# 6
f6 = (3*x**2 + 1)**5
f6_prime = sp.diff(f6, x)
print("Soal 6:")
print("f(x) =", f6)
print("f'(x) =", f6_prime)
print()

# 7
f7 = (x**2 + 2)*(x**2 - 1)
f7_prime = sp.diff(f7, x)
print("Soal 7:")
print("f(x) =", f7)
print("f'(x) =", sp.expand(f7_prime))
print()

# 8
f8 = 2*x**3/(x**2 + 1)
f8_prime = sp.diff(f8, x)
print("Soal 8:")
print("f(x) =", f8)
print("f'(x) =", sp.simplify(f8_prime))
print()

# 9
f9 = (x**2 + 1)**3*(x**3 - 2)
f9_prime = sp.diff(f9, x)
print("Soal 9:")
print("f(x) =", f9)
print("f'(x) =", sp.expand(f9_prime))
print()

# 10
f10 = (x**3 + 2*x)/(x**2 + 1)**2
f10_prime = sp.diff(f10, x)
print("Soal 10:")
print("f(x) =", f10)
print("f'(x) =", sp.simplify(f10_prime))
print()
