"""ljust()
Returns a left justified string of a given width.
Syntax:str.ljust(width, fillchar)
"""

#takes 2 parameters
# mandatory length of string and optional fill char
S = 'Hello world!' # without optional parameter
x = S.ljust(20)
print(x) # prints "Hello World!        "
S = 'Hello world!'
x = S.ljust(20, '#')
print(x) # prints "Hello World!########"
"""
lower()
Returns by converting all lowercase characters to uppercase characters.

Syntax:str.lower()"""

# Convert all characters to lowercase
S = 'Hello World!'
y = 'ramoji rao'
z = y.upper()
x = S.lower()
print(x)
# ignores numbers and special characters
S = 'He!!0 WO$l9'
x = S.lower()
print(z)
print(x)
"""
lstrip()
Returns a string with leading characters removed. Leading characters that are removed depend on the argument passed to the parameter.
Syntax:str.lstrip(charToBeStripped)
"""

S = '  Hello   World!   '
x = S.lstrip()
print(x) # removes only leading spaces
# if any other leading character/characters is to be removed instead of space ' ' then optional param 'chars' can be used
S = '.....Hello World......'
x = S.lstrip('.')
print(x)
S = '...www...Hello ...www.... World...'
x = S.lstrip('.w')
print(x)


"""
maketrans()
Returns a mapping table object that can be used with the translate() method to replace specific characters.

Syntax:str.maketrans(x, y, z)
Parameters:
X: if only one parameter is provided, it should be a dictionary with 1:1 mapping. As this 1:1 mapping will map character to its translation.
Y:(Optional) if this parameter is provided, make sure ‘x’ and ‘y’ both are strings of equal length. Each character in the X string is a replacement to its corresponding index in the Y string.
Z: If three arguments are passed, each character in the third argument is mapped to None.
"""
S = "hey, how are you?"
x = S.maketrans('h', 'z') # replace all occurrences of 'h' with 'z'
print(x) # returns a mapping table that can be used with the translate() method to replace specific characters.
print('#1', S.translate(x))
S = "hey, how are you?"
x = S.maketrans('hrae', 'zabc') # replacing 'h' with 'z', 'r' with 'a' and so on.
print("#2", S.translate(x))
# third optional parameter deletes all characters
S = "hey, how are you?"
x = S.maketrans('r', 'a', 'hey') # all occurences of 'h' 'e' 'y' will be deleted from the string
print("#3", S.translate(x))


"""
partition()
Returns a 3 element tuple, by splitting the string at the first occurrence of the argument and returns a tuple containing the string before the argument, the argument and string after the argument.

Syntax:str.partition(separator)
Parameters:
Separator: will part the string considering only the first occurance of this ‘Separator’.

Note: if separator is not found, the method returns a tuple containing the string itself, followed by two empty strings.
"""

S = 'How are you? How have you been?'
x = S.partition('are') # splits/parts on the basis of this parameter
print(x)
# NOTE: parts/splits only on the first occurance
S = 'How are you? How have you been?'
x = S.partition('you') # will part the sentence considering only the first occurance of 'you'
print(x)
# Note: if separator is not found, the method returns a tuple containing the string itself, followed by two empty strings.
S = 'How are you? How have you been?'
x = S.partition('xyz') # won't part the sentence
print(x)

"""
replace()
Returns a string where all occurrences of a substring are replaced with another substring.

Syntax:str.replace(substr1, substr2, count)
"""
# Replace all occurrences of substring 'WORLD' with 'there'
S = 'Hello WORLD WORLD world'
x = S.replace('WORLD','there')
print(x)
# Replace substring 'WORLD' with 'there' for only 1 occurance, using third optional parameter
S = 'Hello WORLD WORLD world'
x = S.replace('WORLD','there', 1)
print(x)


"""
rfind()
Returns the index of the latest occurrence of substring to be searched for. If not found returns -1.

Syntax:str.rfind(substr, start, end)
"""

sentence = 'Hello, Good Morning, hope you are doing great. Hello World'
#1 last occurrence of 'Hello' (Case Sensitive)
result = sentence.rfind('Hello')
print("#1:", result)
#2 returns -1 if substring not found
result = sentence.rfind('Bye')
print("#2:", result)
#3 last occurrence of Substring is searched in complete string
print("#3:", sentence.rfind('Hello', 0))
#4 last occurrence of Substring is searched in 'Morning, Hello! Hello? How are you?'
print("#4:", sentence.rfind('you', 5))
#5 The last occurance of Substring is searched in 'Hello, Good Morning, hope you are doing great. Hello'
print("#5:", sentence.rfind('Hello', 0, -5))
#6 Substring is searched in ', Good Morning, hope you are doing great. Hello '
print("#6:", sentence.rfind('ing', 5, -5))
"""
rindex()
Returns the index of the latest occurrence of substring to be searched for. If not found, throws an exception. This method is the same as rfind, only difference is rfind returns -1 incase substring is not found.

Syntax:str.rindex(substr)
"""

sentence = 'android is amazing, apple ios is amazing'
# testing index with SubString argument only
# 1 returns index for last occurence
result = sentence.rindex('is amazing')
print("#1", result)
# 2 last occurence of substring is searched in 'apple ios is amazing'
print('#2', sentence.rindex('amazing', 20))
# 3 Substring is searched in 'is amazing, apple ios is'
print('#3', sentence.rindex('is', 7, -8))
# 4 Substring is searched in 'apple ios is amazing'
print('#4', sentence.rindex('amazing', 10, len(sentence)))
# 5 When substring not found, will return error
#result = sentence.rindex('android', 20, len(sentence))
#print("#5", result)

"""
rjust()
Returns a right justified string of given width.

Syntax:
str.rjust(width, fillchar)
"""
# takes 2 parameters
# mandatory length of string and optional fill char
S = 'Hello world!' # without optional parameter
x = S.rjust(20)
print(x) # prints "        Hello World!"
S = 'Hello world!'
x = S.rjust(20, '#')
print(x) # prints ########Hello World!"
