from abc import ABC, abstractmethod


# test


class AbstractRegistry(ABC):
    @abstractmethod
    def add(self, entity):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, entity_id):
        pass

    @abstractmethod
    def update(self, entity_id, **kwargs):
        pass

    @abstractmethod
    def delete(self, entity_id):
        pass


class StudentRegistry:

    def __init__(self) -> None:
        self.students = []

    def add(self, student):
        self.students.append(student)

    def get_all(self):
        return self.students

    def get_by_id(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def update(self, student_id, **kwargs):
        student = self.get_by_id(student_id)
        if student:
            student.name = kwargs.get('name', student.name)
            student.age = kwargs.get('age', student.age)
            student.grade = kwargs.get('grade', student.grade)

    def delete(self, student_id):
        self.students = [s for s in self.students if s.id != student_id]


class Student:
    def __init__(self, name, age, grade) -> None:
        self.id = id(self)
        self.name = name
        self.age = age
        self.grade = grade