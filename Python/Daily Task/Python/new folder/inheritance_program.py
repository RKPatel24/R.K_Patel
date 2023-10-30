class A : # parent class 
    def display(self):
        print("A class here")

class B(A):
    def display(self):
        print("B class here")

obj = B()
obj.display()
obj.displayB()