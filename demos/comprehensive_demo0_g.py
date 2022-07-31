i = 0
arr0 = [10, 20, 30, 40]
arr1 = [1, 2, 3, 4]
for v in arr0:
    if v > 20:
        j = 0
        for w in arr1:
            if w > 2:
                print('w > 2', v * 5 + w)
            else:
                print('w <= 2', v * 5 + w)
            arr1[j] += 1
            j += 1
    else:
        print('忽略')
    arr0[i] += 10
    i += 1
print(i, arr0, arr1)
