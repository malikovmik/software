class CustomException(Exception):
    pass

def check_integers_only(lst):
    for elem in lst:
        if not isinstance(elem, int):
            raise CustomException("Список должен содержать только целые числа")

try:
    check_integers_only([1, 2, 'a', 4, 5])
    print("Список содержит только целые числа")
except CustomException as e:
    print("Произошло исключение:", e)

try:
    check_integers_only([6, 7, 8, 9])
    print("Список содержит только целые числа")
except CustomException as e:
    print("Произошло исключение:", e)
