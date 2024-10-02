'''
fruits = ["Banana" , "Apple" , "Mango" , "Guava"]
i = 0
while i<len(fruits):
    print(fruits[i])
    i=i+1
print("Done")

for i in range(1 , 8 , 2):
    print(i)

# Q1
a = int(input("Enter Your number"))
i = 0
while i<=10:
    print(i * a)
    i = i+1
    break

Q2

l1 = ["Harry" , "Sachin" , "Sohan" , "Rahul"]
for String in l1:
    if String.startswith("S"):
        print("Hello" + " " +  String)

'''

# Q3 Check whether a guven number is prime

# num = int(input("Enter the Num : \n"))
# prime = True
# for i in range(2 , num):
#     if( num % i == 0):
#         prime = False
#         break
# if prime:
#     print("The Number is Prime")
# else:
#     print("The Number is not Prime")


''' Q 4 Write a program to print the sum of first n natural numbers'''
# n = int(input("Enter the number : \n"))
# sum = 0
# i = 1
# while i<=n:
#     sum += i
#     print(sum)
#     i = i + 1
    
''' Q 5 Write a program to print the factorial of a number '''
# n = int(input("Enter the number : \n"))
# fact = 1 
# for i in range(1 , n+1):
#     fact = fact * i
# print(f"The Factorial of the given {n}  is {fact}")

''' Q 6 Write  a program to pattern  '''
'''
*
**
***
****
'''

# n = int(input("Enter the num \n"))
# for i in range(n):
#     print("*" * (i+1) )

''' Q 7 Write a program 
    *
  * * *
* * * * *
'''
   