first_num=int(input("enter the first number of the range"))
last_num=int(input("enter the last number of the range"))
for num in range(first_num,last_num+1): 
     if num%75 == 0 and num%100 == 0: 
                print(str(num) + " ", end = "")
     else: 
                pass
