def quad(arr, n, target):
	temp = {}
	for i in range(n - 1):
		for j in range(i + 1, n):
			temp[arr[i] + arr[j]] = [i, j]
	for i in range(n - 1):
		for j in range(i + 1, n):
			sum = arr[i] + arr[j]
			if (target - sum) in temp:
				p = temp[target - sum]
				if (p[0] != i and p[0] != j and p[1] != i and p[1] != j):
					print(arr[i], ", ", arr[j], ", ",
						arr[p[0]], ", ",arr[p[1]], sep="")
					return
arr = [1,0,0,-1,-2,2]
n = len(arr)
target = 0
quad(arr, n, target)
