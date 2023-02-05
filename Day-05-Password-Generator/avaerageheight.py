student_heights = input("Enter the height of each student separated by comma:").split(',')
for n in range(0,len(student_heights)):
    student_heights [n] = int(student_heights[n])
print(student_heights)

sum = 0
no_of_student = 0
for student in student_heights:
    sum += student
    no_of_student += 1 
    

average = sum/len(student_heights)
print("Average height is :", round(average) )
print("Number of student in the list: ", (no_of_student))
