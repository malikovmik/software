input = input("Введите последовательность чисел, разделенных пробелом: ")

numbers_list = [int(elem) for elem in input.split()]

numbers_tuple = tuple(numbers_list)

print("Список чисел:", numbers_list)
print("Кортеж чисел:", numbers_tuple)
