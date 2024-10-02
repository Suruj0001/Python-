# a  = int(input("Enter your age : \n"))
# if(a>18):
#     print("You are above 18 and ready to vote")
# else:
#     print("You are under 18 and cant vote")

# ** Q1 Write a program to exete greatest of four numbers entered by the user

# a = int(input("Enter your 1st number \n"))
# b = int(input("Enter your 2nd number \n"))
# c = int(input("Enter your 3rd number \n"))
# d = int(input("Enter your 4th number \n"))

# #using nested if else or if elif will be time consuming so we will use pass

# if(a>b):
#     f1 = a
# else:
#     f1 = b

# if(c>d):
#     f2 = c
# else:
#     f2 = d

# if(f1>f2):
#     print("Greatest of all number is " , f1)
# else:
#     print("Greatest of all numbers is " , f2)

#  q2. **Write a program to whether a student is pass or fail , if it requires total 40% and atleast 33% to pass any subject 
# take marks  as user input

# from logging import PercentStyle
# from unittest import result


# a = input("Enter the student name \n")
# b = int(input("Enter the mark obtaned in OS \n"))
# c = int(input("Enter the mark obtained in MATH \n"))
# d = int(input("Enter the marks obtaned in COA \n"))
# result =  ((b + c + d) / 300 * 100 )
# result = int(result)
# if(b<33 or c<33 or d<33):
#     print("You have failed")
# elif(result < 40): 
#     print("You have FAIL with marks " , result)
# else:
#     print(a + " " + "PASS")
'''
# Q3. A Span comment is defined as text like "make a lot of money" "buy this" "Subscribe this" 
from distutils.spawn import spawn


text = input("Enter your Text \n")
if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("Subscribe" in text):
    spam = True
else:
    spam = False
if(spam):
    print("Its a Scam")
else:
    print("Not a Scam")
'''

# #Write a Program to find whether a given username contain 10 Characters
# text = input("Enter Your Name \n")
# n = len(text)
# if(n>10):
#     print("more than 10 characters")
# else:
#     print("less than 10 Characters")

# q4 . Write a program to know whether a name is in a list or not
names = ["Suruj" , "Tanish" , "Piyush" , "Journav" , "Arif"]
a = input("Enter a name \n")
if(a in names):
    print("Yes the name is in the list")
else:
    print("No The name is not in the List") 