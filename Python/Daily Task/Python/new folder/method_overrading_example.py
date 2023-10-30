class A:
    def display(self):
        print("A class")

class B(A):
    def display(self):
        A.display(self)
        print("B class")

obj = B()
obj.display()