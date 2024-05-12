def add_three_and_input():
    try:
        number = int(input("Введите число: "))
        result = 2 + number
        print("Результат сложения:", result)
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

# Тесты
print("Тест 1: ввод числа")
add_three_and_input()

print("\nТест 2: ввод строки")
add_three_and_input()

print("\nТест 3: ввод другого неподходящего типа данных")
add_three_and_input()
