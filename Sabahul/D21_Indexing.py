# Python3 program for demonstration
# of index() method

list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]

# Will print index of '4' in sublist
# having index from 4 to 8.
print(list1.index(4, 4, 8))

# Will print index of '1' in sublist
# having index from 1 to 7.
print(list1.index(1, 1, 7))

list2 = ['cat', 'bat', 'mat', 'cat',
		'get', 'cat', 'sat', 'pet']

# Will print index of 'cat' in sublist
# having index from 2 to 6
print(list2.index('cat', 2, 6 ))
