class Person:
    PersonNAme = None
    PersonAge = None
    def __init__(self,name,age):
            self.PersonNAme = name
            self.PersonAge = age
    def displayPersonAge(self):
          print("Age: ", self.PersonAge)

obj = Person("suruj",10)
obj.displayPersonAge()

