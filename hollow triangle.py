n = int(input("Enter number of rows:"))
for i in range (1,n+1):
    row="  "
    for j in range (1,n+1):
        row+=(str(j)+"  ")if (i==1 or i==n or j==1 or j==n) else"   "
    print(row)
n = int(input("Enter number of rows: "))
for i in range (1,n+1):
    spaces=" "*(n-i)
    numbers=" ".join(str(j)for j in range (1,i+1))
    print(spaces+numbers)    
    
n = int(input("Enter number of rows: "))
for i in range (1,n+1):
    print(" ".join(str(j)for j in range (1,i+1))) 
    height_str = input("Enter the n of the triangle: ")
n = int(height_str)

for i in range(n):
    for j in range(n):
        if j == 0 or i == n - 1 or i == j:
            print("*", end="")
        else:
            print(" ", end="")
    print()