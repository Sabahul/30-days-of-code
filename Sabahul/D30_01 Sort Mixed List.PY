
# Sort Mixed List
# using sort() + comparator

# comparator function for sort
def mixs(num):
	try:
		ele = int(num)
		return (0, ele, '')
	except ValueError:
		return (1, num, '')


# initialize list
test_list = [4, 'gfg', 2, 'best', 'is', 3]

# printing original list
print("The original list : " + str(test_list))

# Sort Mixed List
# using sort() + comparator
test_list.sort(key = mixs)

# printing result
print("List after mixed sorting : " + str(test_list))
