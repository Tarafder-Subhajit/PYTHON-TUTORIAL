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

#REGEX findall
import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")

#REGEX match
text = "The quick brown fox"
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")

#REGEX replace
text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "red"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)

#REGEX search
text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")

#REGEX split
import re

text = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)