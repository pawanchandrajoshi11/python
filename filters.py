# filter(testing_function, grades)

grades = ['A', 'B', 'C', 'D', 'F', 'B', 'A']

# METHOD 1
def remove_fails(grade):
    return grade!='F'


print(list(filter(remove_fails, grades)))

# METHOD 2
filtered_grades = []
for grade in grades:
    if grade!='F':
        filtered_grades.append(grade)

print(filtered_grades)


# METHOD 3
print([grade for grade in grades if grade!='F']) 