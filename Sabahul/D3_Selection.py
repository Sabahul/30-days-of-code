# Basically selection statement is also known as decision making statements 
# Here a code to demonstrate the use of decision making statements.
choice = input(f'Which Subject do you like, Press\nP - Python\nD - Data Structure: ')
if choice == 'P':
    print('Welcome to Pythotn Programming!')
elif choice == 'D':
    print('Welcome you in Study of Data Science!')
else:
    print('You are not interested in these subject')
