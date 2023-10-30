class program:
    def input(self,firstname,lastname):
        self.fname = firstname
        self.lname = lastname
    def display(self):
        print("\n firstname = ",self.fname)
        print("\n lastname = ",self.lname)

obj = program()
obj.input("RAJ","KANERIYA")
obj.display()