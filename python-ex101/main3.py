import sympy
from sympy import symbols, dsolve, diff, integrate, limit, oo, Eq, solve, Function, Matrix

t = symbols("t")
y = Function("y")

print(dsolve(Eq(y(t).diff(t, t) - y(t), sympy.exp(t)), y(t)))
print(Matrix([[1, 2], [2, 2]]).eigenvals())