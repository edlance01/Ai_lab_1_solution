from abc import ABC, abstractmethod

# Define an interface/abstract base class (Dependency Inversion)
class Student(ABC):

    def __init__(self, name: str, grade: int):
        self.name = name
        # Ensuring the grade attribute can be as high as 16
        if not (0 <= grade <= 16):
            raise ValueError("Grade must be between 0 and 16.")
        self.grade = grade

    @abstractmethod
    def attend_class(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


# Research Mixin for Multiple Inheritance
class ResearcherMixin:
    def do_research(self):
        return f"{self.name} is performing academic research."
