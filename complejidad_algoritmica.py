import time


def factorial(n):
    answer = 1

    while n > 1:
        answer *= n
        n -= 1

    return answer


def factorial_r(n):
    if n == 1:
        return 1
    return n * factorial_r(n - 1)


if __name__ == '__main__':
    n = 998

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(f'El tiempo de ejecucíon fue de: {final-comienzo}')

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(f'El tiempo de ejecucíon recursiva fue de: {final - comienzo}')
