c = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
arr0 = [0, 1, 2, 3, 4, 5, 6, 7]
for i in arr0:
    for j in arr0:
        if not j:
            c[i][j] = 1
        else:
            c[i][j] = c[i - 1][j] + c[i - 1][j - 1]
print(c)
