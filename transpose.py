row = int(input("no of rows : " ))
col = int(input("no of columns: "))

print("Matrix values :")
matrix= [[int(input()) for i in range(col)] for i in range(row)]

for n in matrix:
    print(n)

result =[[0 for i in range(row)] for j in range(col)]

for x in range(row):
   for y in range(col):
       result[x][y] = matrix[y][x]
print("transpose matrix  ")
for y in result:
    print(y)