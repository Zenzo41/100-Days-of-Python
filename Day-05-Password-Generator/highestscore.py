student_scores = input("Enter the score of each student separated by space:").split()

for n in range(0,len(student_scores)):
    student_scores [n] = int(student_scores[n])
print(student_scores)

highest = 0
students = 0
for score in student_scores:
    students += 1
    if score > highest:
        highest = score
        
        
print(f'The highest score among {students} is {highest}')