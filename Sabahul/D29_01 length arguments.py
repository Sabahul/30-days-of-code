# Python program to demonstrate
# variable length arguments


# variable arguments
def myFun1(*argv): 
	for arg in argv: 
		print(arg, end =" ") 
		
# variable keyword arguments
def myFun2(**kwargs):
	for key, value in kwargs.items(): 
		print ("% s == % s" %(key, value)) 

# Driver code 
myFun1('Hello', 'Welcome', 'You to', 'Chandigarh University')
print()
myFun2(first ='Chandigarh University !', mid ='Welcome', last ='You ')
