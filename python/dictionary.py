'''
from turtle import update


myDict = {
    "Fast" : "In a Quick Manner" ,
    "Harry" : "A Coder" ,
    "Marks" : [1 , 2 , 5] , 
    "another" : {'harry' : 'Player'}
}

#myDict['Marks'] = [45 , 78]
#print(myDict['Marks'])
#print(myDict.keys())
newDict = {
    "Lnino" : "friend" ,
    "Suruj" : "Friend" , 
    "Suresh" : "Friend" 
}
myDict.update(newDict)
print(myDict)

'''
'''
#sets in Python
b = set()
b.add(4)
b.add(5)
b.add((4 , 6 , 7 , 8)) #Tuples can be added to sets in Python
print(b)
b.remove(5)
print(b)
print(b.pop())  # removes an arbitray element 
print(b)

'''

'''
#q1
myDict = {
    "Kapre" : "Clothes",
    "Vastu" : "Items" , 
    "Jaal" : "Water" 
}
print("Choose from the following : " , myDict.keys())
a = input("Enter the name of the Hindi Word \n" )
print("The Meaning of the above word is " , myDict[a])

'''
'''
#q2

num1 = int(input("Enter the number 1 \n"))
num2 = int(input("Enter the number 2 \n"))
num3 = int(input("Enter the number 3 \n"))
num4 = int(input("Enter the number 4 \n"))
num5 = int(input("Enter the number 5 \n"))
num6 = int(input("Enter the number 6 \n"))
num7 = int(input("Enter the number 7 \n"))
num8 = int(input("Enter the number 8 \n"))
num9 = int(input("Enter the number 9 \n"))

s = { num1 , num2 , num3 , num4 , num5 , num6 , num6 , num7 , num8 , num9}
print(s)

'''

favlang = {}
a = input("Enter Your Favourite language Suruj\n")
b = input("Enter Your Favourite Language Binod\n")
c = input("Enter Your Favourite Language Piyush\n")
d = input("Enter Your Favourite Language Arif\n")
favlang["Suruj"] = a
favlang["Binod"] = b
favlang["Piyush"] = c
favlang["Arif"] = d
print(favlang)

