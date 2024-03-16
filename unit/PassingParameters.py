def stepen(x, n):
    m = 1
    for _ in range(n):
        m *= x
    return m

x = int(input())
print(stepen(x, 3))