

# Задача  треуголник
def triangle_type(a, b, c):
    if a is b is c:
        print("равностороний")
    elif a is b < c or a is b > c:
        print("Равнобедренный")
    elif a is not b is not c:
        print("разностороний")
    else:
        print("треугольник")
    return a + b > c and a + c > b and b + c > a


print(triangle_type(6, 9, 7))


# задача на простое и составное число
def number():
    count = 0
    num = int(input("Введите число: "))
    if num < 100_000 and num > 0:
        for i in range(1,num+1):
            if num % i == 0:
                count += 1
            if count == 3:
                break
    if count > 2:
        print(count)
        return "Составное число"
    else:
        print(count)
        return "Простое число"


print(number())


