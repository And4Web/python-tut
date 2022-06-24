myDict = {
    "fast": "In a Quick Manner",
    "anand": "A Coder",
    "marks": [1, 2, 5],
    "anotherdict": {'anand': 'Player'},
    1: 2
}

# Dictionary Methods
print(list(myDict.keys())) # Prints the keys of the dictionary
print(myDict.values()) # Prints the keys of the dictionary 
print(myDict.items()) # Prints the (key, value) for all contents of the dictionary 
print(myDict)
updateDict = {
    "Lovish": "Friend",
    "Divya": "Friend",
    "Shubham": "Friend",
    "Anand": "A Dancer"
}
myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("anand")) # Prints value associated with key "anand"
print(myDict["anand"]) # Prints value associated with key "anand"

# The difference between .get and [] sytax in Dictionaries?
print(myDict.get("anand2")) # Returns None as anand2 is not present in the dictionary
print(myDict["anand2"]) # throws an error as anand2 is not present in the dictionary