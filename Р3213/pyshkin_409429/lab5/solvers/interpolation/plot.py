import matplotlib.pyplot as plt
import numpy as np


def plot_interpolation(x_points, y_points, target_x, true_func, gauss_func, newton_func, lagrange_func):
    def plot_function(x_points, y_points, func, label, color, markersize, linestyle):
        plt.scatter(x_points, y_points, color=color, zorder=5, label=label, edgecolors="black", linewidth=1)
        
        if func is not None:
            left, right = min(x_points) - 0.1, max(x_points) + 0.1
            x = np.linspace(left, right, int(abs(right - left) * 50 + 100))
            plt.plot(x, [func(value) for value in x], label=label, color=color, linestyle=linestyle)
            plt.plot(target_x, func(target_x), marker="o", markersize=markersize, color=color)
    
    
    plt.figure(figsize=(10, 6))
    
    plot_function(x_points, y_points, true_func, "Исходные функция", "red", 4, "-")
    plot_function(x_points, [newton_func(value) for value in x_points], newton_func, "Метод Ньютона", "orange", 3, "--")
    plot_function(x_points, [gauss_func(value) for value in x_points], gauss_func, "Метод Гаусса", "green", 2, "--")
    plot_function(x_points, [lagrange_func(value) for value in x_points], lagrange_func, "Метод Лагранжа", "blue", 1, "--")
    
    plt.axvline(x=target_x, color="gray", linestyle="--", linewidth=1, label="Целевое x")
    
    plt.title("Сравнение результатов интерполяции", fontsize=14)
    plt.xlabel("x", fontsize=12)
    plt.ylabel("y", fontsize=12)
    plt.grid(True, alpha=0.3)
    
    # Можно убрать, для масштаба
    plt.axis("equal")
    
    plt.legend(loc="best", fontsize=10)
    plt.tight_layout()
    plt.show()
