# STUDENT SCORE TRACKER
student_names = []
student_scores = []
for name in range(3):
    names = input(f"Enter the student name here {name+1}: ")
    student_names.append(names)
print(student_names)
for score in range (3):
    scores= int(input(f"Enter the student score here {score+1}: "))
    student_scores.append(scores)
print(student_scores)
nested = [[student_names], [student_scores]]
print(nested)