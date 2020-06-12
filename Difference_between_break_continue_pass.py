# Difference between break,continue and pass statement
#Break:finishes loop execution
#Continue:jumps to next iteration
#pass: does nothing


#Break Statement
# loop from 1 to 10 
for i in range(1, 11):
# If i is equals to 6, break the loop as soon it encounter 6
	if i == 6: 
		break
	else:  
		print(i, end = " ")
		

'''ouput:
          1 2 3 4 5
'''		

#Continue Statement
# loop from 1 to 10 
for i in range(1, 11):
# If i is equals to 6, continue to next iteration without printing 6
	if i == 6: 
		continue
	else:  
		print(i, end = " ")


''' output:
         1 2 3 4 5 7 8 9 10
'''
		
#Pass Statement
# loop from 1 to 10 
for i in range(1, 11):
# If i is equals to 6,pass statement simply does nothing and continue to next iteration without printing 6
	if i == 6: 
		pass
	else:  
		print(i, end = " ")

''' output:
         1 2 3 4 5 7 8 9 10
'''


		
		
