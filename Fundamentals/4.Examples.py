#String concat
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)

#String length
text = "Python is awesome"
length = len(text)
print("Length of the string:", length)

#string case change
text2 = "Python is awesome"
uppercase = text2.upper()
lowercase = text2.lower()
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)

#string replace
text3 = "Python is awesome"
new_text = text3.replace("awesome", "great")
print("Modified text:", new_text)

#text split
text = "Python is awesome"
words = text.split()
print("Words:", words)

#text strip
text = "   Some spaces around   "
stripped_text = text.strip()
print("Stripped text:", stripped_text)

#string substring
text = "Python is awesome"
substring = "is"
if substring in text:
    print(substring, "found in the text")

#REGEX -
Link- https://www.geeksforgeeks.org/python/regular-expression-python-examples/
