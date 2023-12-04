# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks)
        return average_marks > 50


student1 = Student("Jan Kowalski", [60, 70, 80])
student2 = Student("Anna Nowak", [40, 30, 20])

print(f"{student1.name}: Passed? {student1.is_passed()}")
print(f"{student2.name}: Passed? {student2.is_passed()}")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
