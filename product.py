def max_value(arr, n):
    if n < 3:
        return -1
    arr.sort()
    return max(arr[0] * arr[1] * arr[n - 1],arr[n - 1] * arr[n - 2] * arr[n - 3])

arr = [0,-1,3,100,70,50]
n = len(arr)
max1 = max_value(arr, n)
if max1 == -1:
    print("not exists")
else:
    print("maximum product is", max1)
 