arr = [20, 30, 40, 50, 60]
i = 1
if arr[i] <= 20:
    print(arr[i], "<= 20")
elif arr[i] <= 30:
    print(arr[i], "<= 30")
else:
    print(arr[i], "> 30")
tmp = arr[i]
arr[i] += 20
print(tmp, arr[i], arr)
