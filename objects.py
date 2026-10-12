class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self,color):
        self.color = color
        print("My name is", self.name)
        print("I am", self.age, "years old")
        print("my color is ",self.color)


student1 = Student("Mike", 20, red)

student1.introduce()