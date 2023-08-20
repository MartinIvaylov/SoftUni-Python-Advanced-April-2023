n = int(input())
students_data = {}

for i in range(n):
    student_name, grade = input().split()
    if student_name not in  students_data:
        students_data[student_name] = []

    students_data[student_name].append(float(grade))

for student, grades in students_data.items():
    convert_grades_to_str = ' '.join(map(lambda grade: f"{grade:.2f}", grades))
    average_grade = sum(grades) / len(grades)
    print(f"{student} -> {convert_grades_to_str} (avg: {average_grade:.2f})")

