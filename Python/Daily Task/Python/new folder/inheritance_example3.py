class A:
    def inputA(self):
        self.n1 = int(input("Enter number 1 : "))
        self.n2 = int(input("Enter numver 2 : "))

    def displayA(self):
        ans = self.n1 + self.n2
        return ans
class B:
    def inputB  (self):
        self.n3 = int(input("Enter number 3 : "))
        self.n4 = int(input("Enter number 4 : "))

    def displayB(self):
        ans = self.n3 * self.n4
        return ans
    
class C(A,B):
    def displayC(self):
        print("WELCOME TO CALC WORLD")



obj = C()
obj.displayC()

obj.inputA()
obj.inputB()
print("addition = ",obj.displayA())
print("Multiplication = ",obj.displayB())