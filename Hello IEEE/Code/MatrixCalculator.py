#Identifying the first matrix
rows1=int(input("Enter the number of rows for the first matrix: "))
columns1=int(input("Enter the number of columns for the first matrix: "))
matrix1=[]
for r1 in range(rows1):
    row1=[]
    for c1 in range(columns1):
        elements1=int(input(f"Enter the element of your 1st matrix at ({r1+1}, {c1+1}): "))
        row1.append(elements1)
    matrix1.append(row1)
print("your first matrix is: ")
for m1 in matrix1:
    print(m1)
#Identifying the second matrix
rows2=int(input("Enter the number of rows in the 2nd matrix: "))
columns2=int(input("Enter the number of columns in the 2nd matrix: "))
matrix2=[]
for r2 in range(rows2):
    row2=[]
    for c2 in range(columns2):
        elements2=int(input(f"Enter the element at({r2+1}, {c2+1}): "))
        row2.append(elements2)
    matrix2.append(row2)
print("Your 2nd matrix is: ")
for m2 in matrix2:
    print(m2)
#Summation
if rows1==rows2 and columns1==columns2:
    
    matrix_sum=[[matrix1[a][b]+matrix2[a][b] for b in range(len(matrix1[0]))] for a in range(len(matrix1))]
    print("\nthe sum: ")
    for s in matrix_sum:
        print(s)
#subtraction
    matrix_subtract=[[matrix1[a][b]-matrix2[a][b] for b in range(len(matrix1[0]))] for a in range(len(matrix1))]
    print("\nthe subtraction: ")
    for sub in matrix_subtract:
        print(sub) 
else:
    print("\nBut math can only sum matrices of the same rows and columns\n Try again with equal rows and columns")
#multiplication
if columns1==rows2:
    matrix_mult=[[[matrix1[i][k]*matrix2[k][j] for k in range(columns1)] for j in range(columns2)] for i in range(rows1)]
    print("\n\nThe multiplication: ")
    for m in matrix_mult:
        print(m)
else:
    print("\nMath can't multiply two matrices unless\n the columns of the first one = the rows of the 2nd one ")
#Scalar Multiplication for the 1st matrix
scalar=int(input("\n***Scalar Mult.***\nEnter the number you'd like your matrices to be multiplied with\n(INTEGERS Only): "))
scalar_mult1=[[scalar*matrix1[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
print(f"\nYour 1st Matrix: {scalar}*{matrix1}=")
for sc1 in scalar_mult1:
    print(sc1)
#Scalar Multiplication for the 2nd matrix
scalar_mult2=[[scalar*matrix2[i][j] for j in range(len(matrix2[0]))]for i in range(len(matrix2))]
print(f"\nYour 2nd Matrix: {scalar}*{matrix2}=")
for sc2 in scalar_mult2:
    print(sc2)
#scalar addition for the first matrix
scalar_add_req=int(input("\n***Scalar Addition***\nEnter the number you'd like the elements of your matrices to be added to\n(INTEGERS Only): "))
scalaraddition1=[[scalar_add_req+matrix1[i][j] for j in range(len(matrix1[0]))]for i in range(len(matrix1))]
print(f"\nYour 1st matrix:{scalar_add_req}+{matrix1}= ")
for add1 in scalaraddition1:
    print(add1)
#scalar addition for the 2nd matrix
scalaraddition2=[[scalar_add_req+matrix2[i][j] for j in range(len(matrix2[0]))]for i in range(len(matrix2))]
print(f"\nYour 2nd matrix:{scalar_add_req}+{matrix2}= ")
for add2 in scalaraddition2:
    print(add2)
#Min-Max Normalisation
#Normalization for the 1st matrix
min_in_row1=[]
for i in matrix1:
    min_in_row1.append(min(i))
minvalue1=min(min_in_row1)
max_in_row1=[]
for j in matrix1:
    max_in_row1.append(max(j))
maxvalue1=max(max_in_row1)
normalization1=[[(matrix1[r][c]-minvalue1)/(maxvalue1-minvalue1) for c in range(len(matrix1[0]))]for r in range(len(matrix1))]
print("\n***Matrix Normalization***\nNormalized 1st matrix: ")
for n in normalization1:
    print(n)
#Normalization for the 2nd matrix
min_in_row2=[]
for i in matrix2:
    min_in_row2.append(min(i))
minvalue2=min(min_in_row2) 
max_in_row2=[]
for j in matrix2:
    max_in_row2.append(max(j)) 
maxvalue2=max(max_in_row2)
normalization2=[[(matrix2[a][b]-minvalue2)/(maxvalue2-minvalue2) for b in range(len(matrix2[0]))]for a in range(len(matrix2))]
print("\nNormalized 2nd matrix:")
for n in normalization2:
    print(n)






 



