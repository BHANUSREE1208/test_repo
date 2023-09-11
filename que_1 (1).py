## 1. Find the faculty with highest student count who got more than 90%.
## assuming total marks = 100, 90% = 90 marks

# # check for each subject how many students got >90 marks
subject_90_marks = {}
for entry in open("C:/Users/kragh/OneDrive/Desktop/testprograms/student assignment/student_marks.csv"):
    student, subject, score = entry.split(',')
    if int(score)>90:
        if not subject in subject_90_marks:
            subject_90_marks[subject] = 1
        else:
            subject_90_marks[subject] += 1

# get the subject with max students
max_students_subject = ''
max_students = 0
for i in subject_90_marks.keys():
    if subject_90_marks[i]>max_students:
        max_students = subject_90_marks[i]
        max_students_subject = i
print(max_students)
print(max_students_subject)

# get faculty name
highest_student_count_faculty = ''
for entry in open("C:/Users/kragh/OneDrive/Desktop/testprograms/student assignment/subject_faculty.csv"):
    subject, faculty = entry.split(',')
    if subject == max_students_subject:
        highest_student_count_faculty = faculty
        break

print("Faculty with the highest student count (> 90%): {}".format(highest_student_count_faculty,max_students_subject))




##  2. Find the faculty with highest pass percentage (> 40%) """

subject_40_marks = {}
for entry in open("C:/Users/kragh/OneDrive/Desktop/testprograms/student assignment/student_marks.csv"):
    student, subject, score = entry.split(',')
    if int(score)>40:
        if not subject in subject_40_marks:
            subject_40_marks[subject] = 1
        else:
            subject_40_marks[subject] += 1
# print(subject_40_marks)

n = max(subject_40_marks, key=subject_40_marks.setdefault)
print(n)
highest_pass_percentage = (subject_40_marks[n]/(123)*(100))
print(highest_pass_percentage)

highest_pass_percentage_faculty = ''
for entry in open("C:/Users/kragh/OneDrive/Desktop/testprograms/student assignment/subject_faculty.csv"):
    subject, faculty = entry.split(',')
    if subject == n:
        highest_pass_percentage_faculty = faculty
        break
# print(highest_pass_percentage_faculty)
print("faculty with highest pass percentage (> 40%): {}".format(highest_pass_percentage_faculty))



##  3. Find the faculty with least pass percentage (<= 40%)

subject_40_marks = {}
for entry in open("C:/Users/kragh/OneDrive/Desktop/testprograms/student assignment/student_marks.csv"):
    student, subject, score = entry.split(',')
    if int(score)<=40:
        if not subject in subject_40_marks:
            subject_40_marks[subject] = 1
        else:
           subject_40_marks[subject] += 1
# print(subject_40_marks)
n = min(subject_40_marks, key=subject_40_marks.setdefault)
print(n)
least_pass_percentage = (subject_40_marks[n]/(123)*(100))
print(least_pass_percentage)
least_pass_percentage_faculty = ''
for entry in open("C:/Users/kragh/OneDrive/Desktop/testprograms/student assignment/subject_faculty.csv"):
    subject, faculty = entry.split(',')
    if subject == n:
        least_pass_percentage_faculty = faculty
        break
# # print(least_pass_percentage_faculty)
print("faculty with highest pass percentage (> 40%): {}".format(least_pass_percentage_faculty))




##  4 : who is the top student with maximum total.

import csv

with open("C:/Users/kragh/OneDrive/Desktop/testprograms/student assignment/student_marks.csv") as f:
    data = csv.DictReader(f, fieldnames=['name', 'subject', 'marks'])
    
    student_total_marks = {}
    for record in data:
        # print(record)
        if record['name'] not in student_total_marks:
            student_total_marks[record['name']] = int(record['marks'])
        else:
            student_total_marks[record['name']] += int(record['marks'])
            
# print(student_total_marks)
top_student = max(student_total_marks, key=student_total_marks.get)
max_marks = student_total_marks[top_student]
print(top_student)
print(max_marks) 


##  5. Who is the best student in Mathematics?

student_scores = {}
for entry in open("C:/Users/kragh/OneDrive/Desktop/testprograms/student assignment/student_marks.csv"):
    student, subject, score = entry.split(',')
    if subject == 'Mathematics':
        if student in student_scores:
            student_scores[student] += int(score)
        else:
            student_scores[student] = int(score)

best_student = ''
best_score = 0
for i in student_scores.keys():
    if student_scores[i] > best_score:
        best_score = student_scores[i]
        best_student = i

print("The best student in Mathematics is - {} with score {}".format(best_student,best_score))





##  6. What is the average mark for each subject, (ignore failures)?

subject_marks = {}
for entry in open("C:/Users/kragh/OneDrive/Desktop/testprograms/student assignment/student_marks.csv"):
    student, subject, score = entry.split(',')
    if int(score) >= 35:
        if subject not in subject_marks:
            subject_marks[subject] = []
        subject_marks[subject].append(int(score))

average_marks = {}
for subject, marks in subject_marks.items():
    average_marks[subject] = sum(marks) / len(marks)

for subject, average_mark in average_marks.items():
    print("Average marks for {} : {}".format(subject, average_mark))



##  7. Find the student with least numbers of marks as total


student_totals = {}
for entry in open("C:/Users/kragh/OneDrive/Desktop/testprograms/student assignment/student_marks.csv"):
    student, subject, score = entry.split(',')
    if student not in student_totals:
        student_totals[student] = 0
    student_totals[student] += int(score)

min_total = float('inf')
min_student = ''
for student, total in student_totals.items():
    if total < min_total:
        min_total = total
        min_student = student

print("Student with least total marks: {} (Total Marks: {})".format(min_student, min_total))






