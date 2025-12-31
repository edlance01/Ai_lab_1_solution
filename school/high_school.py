from .protocols import Student


class HighSchoolStudent(Student):
    def attend_class(self):
        print(f"[Roll Call] {self.name}: Present. (Attendance is REQUIRED)")

    def __str__(self):
        return f"High Schooler: {self.name} (Grade {self.grade})"
