def input_x():
    while True:
        try:
            x = float(input("Введите значение x, которое хотите найти: "))
            return x
        except Exception:
            print("Неверное значение, попробуйте еще раз")
    