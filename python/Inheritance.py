class Friend1:
    Friend1name = ""
    def friendName(self):
        print("Hey i m here" , self.Friend1name)

class Friend2:
    friend2name = ""
    def friend2(self):
        print("Hey fr2 nsme is : ", self.friend2name)

class Friend3(Friend1,Friend2):
    def Friend(self):
        print("Friend Name: ", self.Friend1name)
        print("Friend2 name is : ",  self.friend2name)

obj = Friend3()  #declaring
obj.Friend1name = "Raffale"
obj.friend2name = "Sukhoi"

obj.Friend()   ## calling

