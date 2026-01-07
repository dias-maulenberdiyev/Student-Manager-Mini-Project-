students = {}


def add_student():
    """Add a new student with their first grade. Return True on success, False on error."""
    name = input("Enter the student's name: ").strip()
    if name == "":
        print("Error: name cannot be empty")
        return False

    try:
        grade = int(input("Enter the student's grade: ").strip())
    except ValueError:
        print("Error: grade must be an integer")
        return False

    if name in students:
        print("Error: student already exists")
        return False

    students[name] = [grade]
    return True


def update_grade():
    """Update an existing student's grade by selecting an index. Return True on success, False on error."""
    name = input("Enter the student's name: ").strip()
    if name not in students:
        print("Error: student not found")
        return False

    grades = students[name]
    if len(grades) == 0:
        print("Error: this student has no grades to update")
        return False

    # Show grades with indices to make choosing an index easy
    print(f"{name}'s grades:")
    for i, g in enumerate(grades):
        print(f"  {i}: {g}")

    try:
        index = int(input("Enter the index of the grade to update: ").strip())
    except ValueError:
        print("Error: index must be an integer")
        return False

    if index < 0 or index >= len(grades):
        print("Error: index out of range")
        return False

    try:
        new_grade = int(input("Enter the new grade: ").strip())
    except ValueError:
        print("Error: grade must be an integer")
        return False

    grades[index] = new_grade
    return True


def remove_student():
    """Remove a student from the dictionary. Return True on success, False on error."""
    name = input("Enter the student's name: ").strip()
    if name not in students:
        print("Error: student not found")
        return False

    del students[name]
    return True


def display_students():
    """Display all students and their grades."""
    if not students:
        print("No students found.")
        return

    for name, grades in students.items():
        # Match the sample output: show a single grade as a number, otherwise show the list
        if len(grades) == 1:
            print(f"{name}: {grades[0]}")
        else:
            print(f"{name}: {grades}")


def main():
    """Main menu loop."""
    while True:
        print("\n1. Add a new student")
        print("2. Update a grade")
        print("3. Remove a student")
        print("4. Display all students")
        print("5. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            if add_student():
                print("Student added successfully!")

        elif choice == "2":
            if update_grade():
                print("Grade updated successfully!")

        elif choice == "3":
            if remove_student():
                print("Student removed successfully!")

        elif choice == "4":
            display_students()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    main()
