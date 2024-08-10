str1 = "Apple"
dictionary=dict()
for char in str1:
    count=str1.count(char)
    dictionary[char]=count
print(dictionary)

str2 = "PYnative"
str=str2[::-1]
print(str)