def add_student():
    name = input("Enter student name: ")
    course = input("Enter course name: ")

    try:
        with open("students.txt", "a", encoding="utf-8") as file:
            file.write(f"Name: {name}\n")
            file.write(f"Course: {course}\n")
            file.write("-" * 25 + "\n")

        print("Student saved successfully!")

    except OSError as error:
        print(f"Unable to save student details: {error}")


def view_students():
    try:
        with open("students.txt", "r", encoding="utf-8") as file:
            content = file.read()

        if content:
            print("\n--- Student Records ---")
            print(content, end="")
        else:
            print("No student records found.")

    except FileNotFoundError:
        print("No records file exists yet. Add a student first.")

    except OSError as error:
        print(f"Unable to read student records: {error}")


while True:
    print("\n1. Add student")
    print("2. View students")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")