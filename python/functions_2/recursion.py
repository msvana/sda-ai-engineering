def fib(pos: str):
    """
    Args:
    int pos: .....
    """
    if pos == 1:
        return 1
    if pos == 2:
        return 1
    return fib(pos-1) + fib(pos-2)


print(fib(1))
print(fib(2))
print(fib(3))
print(fib(7))
