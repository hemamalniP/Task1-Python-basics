row = int(input("no of rows  for first matrix: " ))
col = int(input("no of columns  for first  matrix: "))

print("First Matrix:")
mat1= [[int(input()) for i in range(col)] for i in range(row)]

print("First Matrix is: ")
for n in mat1:
    print(n)
col_b = int(input("no of columns for second matrix: "))

print("Second Matrix:")
mat2= [[int(input()) for i in range(col_b)] for i in range(col)]
for n in mat2:
    print(n)
    
mul=[[0 for i in range(col_b)] for i in range(row)]

for i in range(len(mat1)):
    for j in range(len(mat2[0])):
        for k in range(len(mat2)):
            mul [i][j]+=mat1[i][k]*mat2[k][j]
print("\nAfter Multiplication is: ")
for x in mul:
    print(x)