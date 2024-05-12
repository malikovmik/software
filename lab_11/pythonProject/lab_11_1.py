def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci_gen()

for x in range(200):
    fib_number = next(fib_gen)
    print(fib_number, end='\n')