class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_marks(self, subject, marks):
        print(self.name, "got", marks, "in", subject)


student1 = Student("Mike", 20)

student1.add_marks("Python", 90)