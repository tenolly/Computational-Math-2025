import sys
from math import ceil, floor
import matplotlib.pyplot as plt

import argparse
import numpy as np
import sympy as sp

from approximation import LinearApproximation, QuadraticApproximation


def get_info_for_table(symbol, function, table):
    phi_func = sp.lambdify(symbol, function)
    phi_func_y, phi_func_e = [], []
    
    for x, y in zip(*table):
        phi_func_y.append(round(phi_func(x), 4))
        phi_func_e.append(round(y - phi_func_y[-1], 4))
    
    phi_average = sum(phi_func_y) / len(phi_func_y)
    determination = 1 - sum(elem ** 2 for elem in phi_func_e) / sum((y - phi_average) ** 2 for y in table[1])
    
    return phi_func_y, phi_func_e, determination


def get_determination_decryption(r2):
    if r2 >= 0.95:
        return "высокая точность аппроксимации"
    
    if 0.75 <= r2 < 0.95:
        return "модель в целом адекватно описывает явление"
    
    if 0.5 <= r2 < 0.75:
        return "модель слабо описывает явление"
    
    if r2 < 0.5:
        return "точность аппроксимации недостаточна и модель требует изменения"
    

def linear_approximation_info(symbol, function, table, output_file):
    x_ = sum(table[0]) / len(table[0])
    y_ = sum(table[1]) / len(table[1])
    
    numerator_sum = denominator_sum_1 = denominator_sum_2 = 0
    for x, y in zip(*table):
        numerator_sum += (x - x_) * (y - y_)
        denominator_sum_1 += (x - x_) ** 2 
        denominator_sum_2 += (y - y_) ** 2
        
    r = numerator_sum / (denominator_sum_1 * denominator_sum_2) ** 0.5
    
    phi_func_y, phi_func_e, determination = get_info_for_table(symbol, function, table)
    print(
        f"Линейная аппроксимация: {function} ({r=})\n"
        "x " + "\t".join(map(str, table[0])) + "\n"
        "y " + "\t".join(map(str, table[1])) + "\n"
        "φ " + "\t".join(map(str, phi_func_y)) + "\n"
        "e " + "\t".join(map(str, phi_func_e)) + "\n"
        f"Коэффициент детерминации: {determination} ({get_determination_decryption(determination)})\n",
        file=output_file
    )
    
    return determination
    

def quadratic_approximation_info(symbol, function, table, output_file):
    phi_func_y, phi_func_e, determination = get_info_for_table(symbol, function, table)
    print(
        f"Квадратичная аппроксимация: {function}\n"
        "x " + "\t".join(map(str, table[0])) + "\n"
        "y " + "\t".join(map(str, table[1])) + "\n"
        "φ " + "\t".join(map(str, phi_func_y)) + "\n"
        "e " + "\t".join(map(str, phi_func_e)) + "\n"
        f"Коэффициент детерминации: {determination} ({get_determination_decryption(determination)})\n",
        file=output_file
    )
    
    return determination


def plot_functions(table, linear_f, quadratic_f, a, b):
    left, right = floor(a - abs(a) * 0.2), ceil(b + abs(b) * 0.2)
    x = np.linspace(left, right, (right - left) * 50)

    plt.figure(figsize=(10, 6))
    plt.scatter(*table, color="green", label="Исходная функция", zorder=5)
    plt.plot(x, linear_f(x), color="blue", label="Линейная аппроксимация")
    plt.plot(x, quadratic_f(x), color="red", label="Квадратичная аппроксимация")

    plt.legend(loc="best")
    plt.xlabel("Ось X")
    plt.ylabel("Ось Y")
    plt.title("Графики функций")
    plt.grid(True)

    plt.show()


def main(input_file, output_file, print_text_prompts=True):
    if print_text_prompts:
        print("Введите x значения через пробел:")
        
    x_row = tuple(map(float, input_file.readline().strip().split()))
    
    if print_text_prompts:
        print("Введите y значения через пробел:")
        
    y_row = tuple(map(float, input_file.readline().strip().split()))
    
    if len(x_row) != len(y_row):
        raise ValueError("Количество значений x и y не совпадает")
    
    if print_text_prompts:
        print()
    
    lx, lfunc = LinearApproximation(table=True).solve([x_row, y_row], lambdify=False)
    qx, qfunc = QuadraticApproximation(table=True).solve([x_row, y_row], lambdify=False)
    
    l_determination = linear_approximation_info(lx, lfunc, [x_row, y_row], output_file)
    q_determination = quadratic_approximation_info(qx, qfunc, [x_row, y_row], output_file)
    if l_determination > q_determination:
        print("В данном случае линейная аппроксимация лучше", file=output_file)
    elif l_determination < q_determination:
        print("В данном случае квадратичная аппроксимация лучше", file=output_file)
    else:
        print("Линейная и квадратичная аппроксимация дают одинаковый результат", file=output_file)
    
    plot_functions([x_row, y_row], sp.lambdify(lx, lfunc), sp.lambdify(qx, qfunc), x_row[0], x_row[-1])
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", default=sys.stdin, help="path to the input file")
    parser.add_argument("--output", "-o", default=sys.stdout, help="path to the output file")
    
    args = parser.parse_args()
    
    try:
        if isinstance(args.input, str):
            args.input = open(args.input, mode="r")
        
        if isinstance(args.output, str):
            args.output = open(args.output, mode="w", encoding="utf-8")
        
        main(args.input, args.output, args.input == sys.stdin)
    except Exception as e:
        print(f"Возникла ошибка во время выполнения программы: {e}")
    finally:
        args.input.close()
        args.output.close()
