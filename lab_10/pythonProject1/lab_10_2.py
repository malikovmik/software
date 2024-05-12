def read_file(filename):
    try:
        with open(filename, "r") as file:
            data = file.read()
            if not data:
                raise Exception("Файл пустой")
            else:
                print("нформация из файла:")
                print(data)
    except FileNotFoundError:
        print("Файл не найден")
    except Exception as e:
        print("Ошибка:", e)

print("Попытка считать данные:")
read_file("empty.txt")

print("Попытка считать данные:")
read_file("data_fail.txt")