# Q. Write a program to build a simple Student Management System
# using Python which can perform the following operations:
# 1. Display
# 2. Search
# 3. Delete


import weakref

class Classroom:
    _students = []

    def __init__(self, name, std, rollno):
        self.name = name
        self.std = std
        self.rollno = rollno
        self.__class__._students.append(self)

    @classmethod
    def display(cls):
        for i in cls._students:
            print(i.name)

    @classmethod
    def delete(cls, std):
        cls._students.remove(std)
        print(std.name+" is removed from classroom")
        del std

    @classmethod
    def search(cls, rno):
        for i in cls._students:
            if i.rollno == rno:
                print("Roll no {} is {}".format(rno,i.name))
                break


std1 = Classroom('Abby', 8, 1)
std2 = Classroom('Puzu', 8, 2)

Classroom.display()

Classroom.delete(std1)

Classroom.display()

Classroom.search(2)
