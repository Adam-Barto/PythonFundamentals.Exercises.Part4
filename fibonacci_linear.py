def fibonnaci(n):
    global c
    a = 0
    b = 1
    for x in range(1, n):
        c = a + b
        a = b
        b = c
    print(c)


fibonnaci(30)
