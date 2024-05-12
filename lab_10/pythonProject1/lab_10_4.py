def custom_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__} с аргументами: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} вернула результат: {result}")
        return result
    return wrapper

@custom_decorator
def example_function(x, y):
    return x + y

example_function(3, 5)
