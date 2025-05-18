import matplotlib.pyplot as plt

import sympy as sp
import numpy as np

from solver import euler_method, fourth_order_runge_kutta_method, milne_method


USE_RUNGE_RULL = True


def ask_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except Exception:
            print("Некорректное значение, попробуйте еще раз")


def select_equation_and_parameters():
    print("Выберите ОДУ:")
    print("1. y' = x + y")
    print("2. y' = y * cos(x)")
    print("3. y' = x^2 - y")
    
    x = sp.Symbol("x")
    y = sp.Symbol("y")
    
    equations = [
        x + y,
        y * sp.cos(x),
        x**2 - y
    ]
    
    y_func = sp.Function("y")
    equations_to_solve = [
        sp.Eq(y_func(x).diff(x), x + y_func(x)),
        sp.Eq(y_func(x).diff(x), y_func(x) * sp.cos(x)),
        sp.Eq(y_func(x).diff(x), x ** 2 - y_func(x))
    ]
    
    while True:
        try:
            choice = int(input("Введите номер уравнения (1-3): ")) - 1
            f_expr = equations[choice]
            break
        except Exception:
            print("Некорректное значение, попробуйте еще раз")
    
    f = sp.lambdify((x, y), f_expr, "numpy")

    x0 = ask_float("Начальное значение x0: ")
    y0 = ask_float("Начальное значение y0: ")
    xn = ask_float("Конечное значение xn: ")
    h = ask_float("Шаг h: ")
    eps = ask_float("Точность eps: ")
    
    solution = sp.dsolve(equations_to_solve[choice], y_func(x), ics={y_func(x0): y0})
    true_f = sp.lambdify(x, solution.rhs)

    return f, true_f, x0, y0, xn, h, eps


def plot_points(method_result, true_result, title):
    true_x_values, true_y_values = true_result
    x_values, y_values = method_result
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(true_x_values, true_y_values, "bo-", linewidth=2, markersize=6, label="Реальное решение")
    plt.plot(x_values, y_values, "ro-", linewidth=2, markersize=6, label=title)
    
    plt.title("График решения ОДУ", fontsize=14)
    plt.xlabel("x", fontsize=12)
    plt.ylabel("y", fontsize=12)
    plt.grid(True)
    plt.legend()
    
    plt.show()


def main():
    f, true_f, x0, y0, xn, h, eps = select_equation_and_parameters()
    
    euler_x, euler_y = euler_method(f, x0, y0, xn, h, USE_RUNGE_RULL, eps)
    print("Метод Эйлера:", euler_x, euler_y, sep="\n")
    
    runge_x, runge_y = fourth_order_runge_kutta_method(f, x0, y0, xn, h, USE_RUNGE_RULL, eps)
    print("Метод Рунге-Кутта:", runge_x, runge_y, sep="\n")
    
    milne_x, milne_y = milne_method(f, x0, y0, xn, h, eps)
    true_solution = [true_f(x) for x in milne_x]
    
    print("Метод Милне:", milne_x, milne_y, sep="\n")
    print("Вектор погрешностей:", [abs(milne_x[i] - true_solution[i]) for i in range(len(milne_x))])
    
    true_points = np.linspace(x0, xn, int(abs(xn - x0) * 100))
    true_solution = [true_f(x) for x in true_points]
    plot_points((euler_x, euler_y), (true_points, true_solution), "Метод Эйлера")
    plot_points((runge_x, runge_y), (true_points, true_solution), "Метод Рунге-Кутта")
    plot_points((milne_x, milne_y), (true_points, true_solution), "Метод Милне")
    

if __name__ == "__main__":
    main()
