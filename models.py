from abc import ABC, abstractmethod

AZURE_CLIENT_ID = '76ae1e67-c3d9-464d-b7f7-e5b89398e221'
AZURE_TENANT_ID = '88d84258-a941-4406-ba09-4c3a0a10f9e3'


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