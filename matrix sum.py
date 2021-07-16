row = int(input("no of rows : " ))
col = int(input("no of columns: "))

print("First Matrix:")
a= [[int(input()) for i in range(col)] for i in range(row)]
print("First Matrix is: ")
for n in a:
    print(n)

print("Second Matrix:")
b= [[int(input()) for i in range(col)] for i in range(row)]
for n in b:
    print(n)
    
matrix=[[0 for i in range(col)] for i in range(row)]

for i in range(row):
    for j in range(col):
        matrix[i][j] = a[i][j]+b[i][j]

print("Sum of matrix : ")
for s in matrix :
    print(s)