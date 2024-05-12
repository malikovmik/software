from lab_4_5 import geron

def main():
    print("Введите длины сторон треугольника: ")
    a = float(input("Длина стороны а: "))
    b = float(input("Длина стороны b: "))
    c = float(input("Длина стороны c: "))

    area = geron(a, b, c)

    print("Площадь треугольника: ", area)

if __name__ == '__main__':
    main()