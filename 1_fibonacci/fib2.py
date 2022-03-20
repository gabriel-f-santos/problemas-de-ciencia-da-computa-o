#gerando o número correspondente a ordem de fibonacci sem recursão (+eficiente)
def fib2(n: int) -> int:
    if n == 0: return n  
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next

if __name__ == '__main__':
    print(fib2(7))
