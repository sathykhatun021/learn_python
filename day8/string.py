variable1= "sathy"
variable2= """ \nNote: It does not matter whether you enclose your strings in single or double quotes, the output remains the same.

Sometimes, the user might need to put quotation marks in between the strings. Example, consider the sentence: He said, “I want to eat an apple”.

How will you print this statement in python?: He said, "I want to eat an apple". We will definitely use single quotes for our convenience"""
print("name: " + variable1, variable2)
print(variable1[0])
print(variable1[1])
print(variable1[2])
print(variable1[3])
print(variable1[4])
print("\n")
for character in variable2:
    print(character)