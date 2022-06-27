def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "     Anand is a good      "
n = remove_and_split(this, "Anand")
print(n)
# print(this)
# print(this.strip())
