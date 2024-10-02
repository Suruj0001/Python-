class Parent:
    def __init__(self):
            self._number = 20

class Child(Parent):
      def _init_(self):
            Parent._init_(self)
            print("Accesing the member from parent class: ", self._number)

            self._number = 30
            print("Accessing the modified protected number: ", self._number)

obj1 = Child()
obj2 = Parent()

print("Acessing a protected member of the child class: ", obj1._number)
print("Accesing the protected member of the parent class: ", obj2._number)

