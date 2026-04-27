# mini exercise

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __str__(self):
        return f"Student({self.name}, grade={self.grade})"

    def introduce(self):
        return f"Hello, my name is {self.name} and my grade is {self.grade}"

    def is_passing(self):
        if self.grade == "A" or self.grade == "B":
            return True
        return False
    
    def status(self):
        if self.is_passing():
            return f"{self.name} is passing."
        else:
            return f"{self.name} needs help."

    @classmethod
    def from_string(cls, student_str):
        name, grade = student_str.split("|")
        return cls(name, grade)

# test all methods
s1 = Student("Wilson", "A")
s2 = Student("Eve", "C")

print(s1)               # __str__
print(s1.introduce())   # introduce
print(s1.status())      # status → calls is_passing internally
print(s2.status())      # should say needs help
print(s2.is_passing())  # False

s3 = Student.from_string("Adeline|B")
print(s3.name)
print(s3.status())

s = Student.from_string("Eve|A")
print(s.name)
