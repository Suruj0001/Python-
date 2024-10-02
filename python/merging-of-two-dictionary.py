dict1 = {}
dict2 = {}

print("Enter 1 item for the First Dictionary: ")
for i in range(1):
    print("Enter the Key for dict1 : ")
    dictKey = input()
    print("Enter the value for dict1 : ")
    dictVal = input()
    dict1.update({dictKey: dictVal})

print("Enter 1 item for the Second Dictionary: ")
for i in range(1):
    print("Enter the Key for dict2:")
    dictKey = input()
    print("Enter the value for value :")
    dictVal = input()
    dict1.update({dictKey: dictVal})

dict2.update(dict1)

print("Succesfully Merged")
print("The NEW one is : ")
print(dict2)
