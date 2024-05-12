def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Создаем генератор чисел Фибоначчи
fib_gen = fibonacci()

# Записываем все числа Фибоначчи в файл
with open("fib.txt", "w") as file:
    for _ in range(200):
        fib_number = next(fib_gen)
        file.write(str(fib_number) + "\n")

# Получаем последнее число Фибоначчи
last_fib_number = fib_number

print("Последнее число Фибоначчи:", last_fib_number)
