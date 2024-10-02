'''
name = "SURUJ"
print(name[1:])
print(name[0:])
print(name[0::2])
name1 = "amazing"
print(name1[1::3])
print(len(name))


'''
'''
name = "Suruj is the one and only god"
print(name.find("is"))
'''
'''
name = "Good Afterrnoon"
value = input("Enter your name : ")
c = name + " " + value
print(c)

'''

letter = '''\tDear  <|Name|>
            You are selected !
            <|DATE>
            '''
name = input("Enter your name : ")
date = input("Enter your date : ")
letter = letter.replace("<|Name|>" , name)
letter = letter.replace("<|DATE>" , date)
print(letter)


