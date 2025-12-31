from .protocols import Student, ResearcherMixin


class CollegeStudent(Student, ResearcherMixin):
    def attend_class(self):
        print(f"[Lecture] {self.name} signed in. (Attendance is OPTIONAL)")

    def __str__(self):
        return f"College Student: {self.name} (Grade {self.grade})"
