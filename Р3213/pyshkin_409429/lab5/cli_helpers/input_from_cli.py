def input_console():
    while True:
        try:
            x_input = input("Введите значения x через пробел: ")
            y_input = input("Введите значения y через пробел: ")
            
            x = list(map(float, x_input.split()))
            y = list(map(float, y_input.split()))
            
            if len(x) != len(y):
                print("Ошибка: количество x и y должно совпадать. Попробуйте снова.")
                continue
            
            if len(x) < 2:
                print("Ошибка: должно быть не менее двух точек. Попробуйте снова.")
                continue
            
            return x, y
        
        except ValueError:
            print("Ошибка: введены некорректные данные. Попробуйте снова.")

