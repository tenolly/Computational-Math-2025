import sympy as sp

def input_function():
    while True:
        x_sym = sp.symbols("x")
        functions = {
            "sin(x)": sp.sin(x_sym),
            "cos(x)": sp.cos(x_sym),
            "exp(x)": sp.exp(x_sym),
            "x^2": x_sym**2,
        }
        
        print("Доступные функции:")
        for i, name in enumerate(functions.keys(), 1):
            print(f"{i}. {name}")
            
        try:
            choice_num = int(input("Выберите номер функции: "))
            if choice_num < 1 or choice_num > len(functions):
                raise ValueError()
            
            func_name = list(functions.keys())[choice_num - 1]
            selected_func = functions[func_name]
            
            break
        except ValueError:
            print("Ошибка: некорректный выбор функции.")
    
    while True:
        try:
            a = float(input("Введите начало интервала a: "))
            b = float(input("Введите конец интервала b: "))
            if a >= b:
                print("Ошибка: a должно быть меньше b.")
                continue
            
            n = int(input("Введите количество точек n (не менее 2): "))
            if n < 2:
                print("Ошибка: количество точек должно быть не менее 2.")
                continue
            
            break
        except ValueError:
            print("Ошибка: некорректный ввод числа.")
        
    step = (b - a) / (n - 1)
    
    x_vals = [a + i * step for i in range(n)]
    y_vals = []
    
    for xi in x_vals:
        y = selected_func.subs(x_sym, xi).evalf()
        y_vals.append(float(y))
        
    return x_vals, y_vals, sp.lambdify(x_sym, functions[func_name]) 
