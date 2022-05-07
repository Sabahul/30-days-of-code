
# Python program to demonstrate
# overriding in multilevel inheritance


class Parent():
		
	# Parent's show method
	def display(self):
		print("Inside Parent")
	
	
# Inherited or Sub class (Note Parent in bracket)
class Child(Parent):
		
	# Child's show method
	def show(self):
		print("Inside Child")
	
# Inherited or Sub class (Note Child in bracket)
class GrandChild(Child):
		
	# Child's show method
	def show(self):
		print("Inside GrandChild")		
	
# Driver code
g = GrandChild()
g.show()
g.display()
