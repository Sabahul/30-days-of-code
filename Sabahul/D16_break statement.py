# Python program to
# demonstrate break statement

s = 'Sabahul'
# Using for loop
for letter in s:

	print(letter)
	# break the loop as soon it sees 'e'
	# or 's'
	if letter == 'a' or letter == 's':
		break

print("Out of for loop")
print()

i = 0

# Using while loop
while True:
	print(s[i])

	# break the loop as soon it sees 'e'
	# or 's'
	if s[i] == 'a' or s[i] == 's':
		break
	i += 1

print("Out of while loop")
