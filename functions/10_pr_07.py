def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "     Suruj is a good      "
n = remove_and_split(this, "Suruj")
print(n)
# print(this)
# print(this.strip())
