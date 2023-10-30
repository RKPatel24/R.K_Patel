'''
        A
        |
        v
        B

-------------------------------
        A
        |
        V
        B
        |
        V
        C
---------------------------------
        A               B
        |               |
        -----------------
                |
                V
                C
---------------------------------
        A
        |
-----------------------------
|                            |
B                            C


'''

class A:
    num1 = 10


class B:
    num2 = 20

class c(A,B):
    def display(self):
        self.ans = A.num1 + B.num2
        return self.ans

obj = c()

print(obj.display())
        