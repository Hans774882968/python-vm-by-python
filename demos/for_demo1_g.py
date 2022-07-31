arr0 = [3, 4, 5, 6, 7]
arr1 = [2, 3, 4, 5]
ii = 0
for i in arr0:
    jj = 0
    for j in arr1:
        print(i, j, i * 10 + j)
        arr1[jj] += 1
        jj += 1
    arr0[ii] += 1
    ii += 1
print('结束力', ii, jj)
