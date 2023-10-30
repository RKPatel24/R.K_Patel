'''
poly mans many and morphism mans forms

polymorphism which is derived from greak word

one name method has different different forms

there are  2 types of polymorphism :

1) method overloading
2) method overrading


=> methd overloading :
    one class have name method but different forms its called method overloading

=> method overrading :
    orent and child both have same and method its called method overreading

'''

class Student:
    def display(self):
        print("this is default display method")

    def display(self,num1):
        print("num1 = ",num1)

obj = Student()
obj.display(10)
obj.display()