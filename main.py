from school import HighSchoolStudent, CollegeStudent, ResearcherMixin


def populate_students():
    """Programmatically generates a mix of 6 students."""
    students = []
    for i in range(1, 7):
        name = f"Student_{i}"
        grade = 10 + i  # Results in grades 11 through 16

        if grade <= 12:
            students.append(HighSchoolStudent(name, grade))
        else:
            students.append(CollegeStudent(name, grade))
    return students


def main():
    student_list = populate_students()

    for student in student_list:
        # 1. Print the student (Polymorphic __str__)
        print(student)

        # 2. Call the required method
        student.attend_class()

        # 3. Handle the Challenge: Use the Mixin to check capability
        if isinstance(student, ResearcherMixin):
            print(f"   Capability: {student.do_research()}")

        print("-" * 40)


if __name__ == "__main__":
    main()
