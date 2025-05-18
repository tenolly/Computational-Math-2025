import sympy as sp


x = sp.Symbol("x")
functions = [
    5 * x + 4,
    x**2 - 6*x + 1,
    4 * x**3 - x - 9,
    sp.exp(x + 1) + 1,
    5 * sp.ln(-x + 10) - 3,
    10 ** x - 3 * x
]

a, b, n = -4, 3, 10
func = functions[2]

print(f"Ограничения: [{a}, {b}], {n=}")
print(f"Функция: {func}")

f = sp.lambdify(x, func)
x_row, y_row = [], []

h = (b - a) / n
for i in range(n + 1):
    x_row.append(round(a + h * i, 4))
    y_row.append(round(f(x_row[-1]), 4))

print("Таблица значений:")
print(*x_row)
print(*y_row)
