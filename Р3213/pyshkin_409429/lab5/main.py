import sympy as sp

from cli_helpers import input_console, input_file, input_function, input_x
from solvers.finite_differences.table import create_table, print_finite_differences_table
from solvers.interpolation import gauss_interpolation, newton_interpolation, lagrange_interpolation
from solvers.interpolation.plot import plot_interpolation


def input_data():
    print("Выберите способ ввода данных:")
    print("1. Ввод с клавиатуры")
    print("2. Загрузка из файла")
    print("3. Генерация на основе функции")
    choice = input("Ваш выбор: ")
    
    while True:
        if choice == '1':
            x, y = input_console()
            func = None
            break
        elif choice == '2':
            x, y = input_file()
            func = None
            break
        elif choice == '3':
            x, y, func = input_function()
            break
        else:
            print("Неверный выбор.")

    print("\nТаблица значений:")
    print("x:", " ".join(map("{:.4f}".format, x)))
    print("y:", " ".join(map("{:.4f}".format, y)))
    
    return x, y, func


def main():
    while True:
        x_vals, y_vals, true_func = input_data()
        
        if len(set(x_vals)) != len(x_vals):
            print("! Есть повторы среди x значений !\n")
            continue
        
        break
    
    diffs = create_table(x_vals, y_vals)
    print_finite_differences_table(x_vals, diffs)
    
    target_x = input_x()
    
    x = sp.Symbol("x")
    y_gauss = gauss_interpolation(x_vals, diffs, x)
    y_newton = newton_interpolation(x_vals, diffs, x)
    y_lagrange = lagrange_interpolation(x_vals, y_vals, x)
    
    print(f"Полученная функция интерполяции Гаусса: {y_gauss}")
    print(f"Полученная функция для интерполяции Ньютона: {y_newton}")
    print(f"Полученная функция для интерполяции Лагранжа: {y_lagrange}")
    
    gauss_func = sp.lambdify(x, y_gauss)
    newton_func = sp.lambdify(x, y_newton)
    lagrange_func = sp.lambdify(x, y_lagrange)
    
    plot_interpolation(x_vals, y_vals, target_x, true_func, gauss_func, newton_func, lagrange_func)
    

if __name__ == "__main__":
    main()
