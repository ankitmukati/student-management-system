student_grade = {}


def add_student(name, grade):
    student_grade[name] = grade
    print(f"Added {name} with grade {grade}")


def update_student(name, grade):
    if name in student_grade:
        student_grade[name] = grade
        print(f"Updated {name}'s grade to {grade}")
    else:
        print(f"{name} not found.")


def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f"{name} has been deleted.")
    else:
        print(f"{name} not found.")


def view_student():
    if student_grade:
        for name, grade in student_grade.items():
            print(f"{name}: {grade}")
    else:
        print("No students found.")


def main():
    while True:
        print("\nWelcome to Student Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            name = input("Enter student name: ")
            try:
                grade = int(input("Enter grade: "))
                add_student(name, grade)
            except ValueError:
                print("Invalid grade. Please enter a number.")
        elif choice == 2:
            name = input("Enter student name: ")
            try:
                grade = int(input("Enter new grade: "))
                update_student(name, grade)
            except ValueError:
                print("Invalid grade. Please enter a number.")
        elif choice == 3:
            name = input("Enter student name: ")
            delete_student(name)
        elif choice == 4:
            view_student()
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
