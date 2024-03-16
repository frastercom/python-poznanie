def stepen(x, n):
    m = 1
    for _ in range(n):
        m *= x
    return m

def printStepen():
    x = int(input())
    n = int(input())
    print(stepen(x, n))

printStepen()
printStepen()