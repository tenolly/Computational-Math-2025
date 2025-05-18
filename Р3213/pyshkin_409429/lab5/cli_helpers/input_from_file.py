def input_file():
    while True:
        filename = input("Введите имя файла: ")
        
        try:
            with open(filename, "r") as f:
                lines = f.readlines()
                
                if len(lines) < 2:
                    print("Ошибка: файл должен содержать две строки.")
                    continue
                
                x_line = lines[0].strip()
                y_line = lines[1].strip()
                
                x = list(map(float, x_line.split()))
                y = list(map(float, y_line.split()))
                
                if len(x) != len(y):
                    print("Ошибка: количество x и y в файле не совпадает.")
                    continue
                
                if len(x) < 2:
                    print("Ошибка: должно быть не менее двух точек.")
                    continue
                
                return x, y
            
        except FileNotFoundError:
            print("Ошибка: файл не найден.")
            
        except ValueError:
            print("Ошибка: некорректные данные в файле.")
            
        except Exception:
            print("Ошибка, попробуйте еще раз.")
    