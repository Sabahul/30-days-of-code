# program to display student's marks from record


student_name = 'Sabahul'

marks = {'Sabahul': 90, 'Rahul': 55, 'Sarthak': 91}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')
