from student import Student
from data_utils import load_data, save_data

def add_student():
    name = input("Enter student name: ")
    subjects = {}
    num_subjects = int(input("How many subjects? "))
    for _ in range(num_subjects):
        subject = input("Enter subject name: ")
        score = float(input(f"Enter score for {subject}: "))
        subjects[subject] = score
    student = Student(name, subjects)
    students = load_data()
    students.append(student.to_dict())
    save_data(students)
    print("\nStudent added successfully!")

def view_students():
    students = load_data()
    if not students:
        print("No students found.")
    for idx, s in enumerate(students, start=1):
        print(f"\nStudent {idx}:")
        print(f"Name: {s['name']}")
        print("Subjects and Scores:")
        for sub, score in s['subjects'].items():
            print(f"  {sub}: {score}")
        print(f"Average: {s['average']:.2f}")
        print(f"Grade: {s['grade']}")

def update_score():
    students = load_data()
    name = input("Enter name of student to update: ")
    for student in students:
        if student['name'].lower() == name.lower():
            subject = input("Enter subject to update: ")
            if subject in student['subjects']:
                new_score = float(input(f"Enter new score for {subject}: "))
                student['subjects'][subject] = new_score
                s_obj = Student(student['name'], student['subjects'])
                student.update(s_obj.to_dict())
                save_data(students)
                print("Score updated successfully!")
                return
            else:
                print("Subject not found.")
                return
    print("Student not found.")
