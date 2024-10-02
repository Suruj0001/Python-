# from abc import ABSMeta,abstractmethod
from abc import abstractmethod, ABCMeta


class Food():
    _metaclass_ = ABCMeta
    @abstractmethod
    def ingredients(self):
        pass
    def taste(self):
        pass

class Veg(Food):
    def ingredients(self):
            print("tomato","onion","cottage cheese")
    def taste(self):
            print("Good")

class Nonveg(Food):
     def ingredients(self):
            print("chicken","meat","beef")
     def taste(self):
            print("Good too")

obj = Veg()
obj.ingredients()
obj.taste()

obj2 = Nonveg()
obj2.ingredients()
obj2.taste()


