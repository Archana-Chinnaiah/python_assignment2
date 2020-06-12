rows=int(input("Enter the number of rows in odd numbers:"))
for row in range(1,rows+1):
     if(row%2!=0):
         for column in range(1,row+1):
             print("*",end="")
         print()   
for row in range(rows, 0, -1):
    if(row%2==0):
        for column in range(0, row - 1):
           print("*", end='')
        print()
