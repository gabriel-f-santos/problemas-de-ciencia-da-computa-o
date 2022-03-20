#gerando o número correspondente a ordem de fibonacci


def fib1(n: int) -> int:
    if n < 2:
        return n
    return fib1(n-1)+fib1(n-2)

if __name__ == 'main':
    print(fib1(4))
