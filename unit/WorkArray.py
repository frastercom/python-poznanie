a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(0, len(a)):
    for j in range(i + 1, len(a[i])):
        print(a[i][j], end=" ")
    print()

# 1 2 3
# 5 6
# 9

# 2 3
# 6