def fibonnaci(n):
    if n <= 1:
        return n
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)


print(fibonnaci(0))
print(fibonnaci(4))
print(fibonnaci(5))
