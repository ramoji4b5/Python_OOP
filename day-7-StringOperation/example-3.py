"""String Methods"""

##str.capitalize()
    #Returns a copy of the original string, with only the first letter as upper case and keeping all the other characters as lower case.

name = "interview Bit docs"
name.capitalize()

#casefold() :Returns a string with each character as lower case.
#str.casefold()

myText = "Interview Bit Problem Solving"
x = myText.casefold()
print(x)

"""
Syntax:

str.center(width, fillChar)
width is the length of the resulting string.
fillChar (optional) is the character to be padded. If not provided takes space as default parameter.
"""
txt = "interviewBit"
# [Mandatory] length is the first parameter
x = txt.center(20)
print(x)
# [Optional] 2nd parameter is character
# to fill the missing space on each side
x = txt.center(20, '*')
print(x)

"""count()
str.count(substring, start, end)
Substring is the substring you’re counting for.
Start (optional): index where search starts. By default ‘0’.
Stop (optional) index where search stops. By default it stops at the last index.
"""

myText = 'Hello World Hello'
# [Mandatory] string value to search format
x = myText.count('Hello')
print('Count of Hello in myText = ', x)
# [Optional] start & end IndexError
x = myText.count('Hello', 0, 6)
print('Count of Hello in myText from index 0 to 6 =', x)
# [Optional] start index & end Index
x = myText.count('Hello', 7)
print('Count of Hello in myText from index 7 till end = ', x)

"""string.encode(encoding='UTF-8',errors='strict')
"""
print('***********************************************************')
S1 = 'Hello World'
print(S1.encode('UTF-8'))
S2 = 'hellö wörld'
print('original string', S2)
print('The encoded version with ignore:', S2.encode("ascii", "ignore"))
print('The encoded version with replace:', S2.encode("ascii", "replace"))
print('***********************************************************')

"""
endsWith()
Returns true if a string ends with a specified suffix.
str.endsWith(suffix, start, end)"""

text = "Welcome to interview bit"
result = text.endswith('bit')
print(result)
result = text.endswith('interview')
print(result)
result = text.endswith('Welcome to interview bit')
print(result)

"""expandTabs()
Returns a string by replacing all the ‘\t’ characters with white space characters.
string.expandtabs(tabsize)
"""

S1 = 'Hello\tWorld\t!'
print(S1.expandtabs())

print(S1.expandtabs(10))

print(S1.expandtabs(15))

"""find()
Returns index of first occurrence of a substring in a string, if found. If not found returns -1.
str.find(substr, start, end)
"""
sentence = 'Good Morning, Hello! Hello? How are you?'
# 1 first occurrence of 'Hello' (Case Sensitive)
result = sentence.find('Hello')
print("#1:",result)
# 2 returns -1 if substring not found
result = sentence.find('Bye')
print("#2:", result)
# 3 Substring is searched in 'Hello? How are you?'
print("#3:", sentence.find('Hello', 20))
# 4 Substring is searched in 'Morning, Hello! Hello? How are you?'
print("#4:", sentence.find('you', 5))
# 5 Substring is searched in 'od Morning, Hello! Hello?'
print("#5:", sentence.find('Morning, Hello!', 2, -13))
# 6 Substring is searched in 'Morning, Hello!'
print("#6:", sentence.find('ing', 5, 20))
###########################################################
"""format()
str.format()
"""

# Positional Parameters
S1 = 'Hello {0} World! {1}'
print(S1.format('beautiful', 'good morning'))

S2 = 'Hello {0}, your bank balance is {1:9.2f}'
print(S2.format('customer', 999.456))

# Keyword Parameters
S2 = 'Hello {name}, good {timeofday}!'
print(S2.format(timeofday='afternoon', name='John'))

"""formatMap()
Is similar to the format method, Returns a string by replacing the placeholders in the original string with the values provided as key-value objects (dictionary ) in parameters.
"""

bankDetail = {'name': 'John', 'bankBalance': 1000}
S1 = 'greetings {name}, your balance is {bankBalance}'
print(S1.format_map(bankDetail))
# prints 'greetings John, your balance is 1000'
# returns a string by replacing keys name & bankBalance in the string S1 from mappings available in bankDetail object

"""index()
Returns index of first occurrence of a substring in a string, if found. (Just like find())
Syntax:
str.index(substr, start, end)"""

sentence = 'android is amazing, apple ios is amazing'
# testing index with SubString argument only
# 1 returns index for first occurence
result = sentence.index('is amazing')
print("#1", result)
# 2 Substring is searched in 'apple ios is amazing'
print('#2', sentence.index('amazing', 20))
# 3 Substring is searched in 'apple ios is'
print('#3', sentence.index('ios', 20, -8))
# 4 Substring is searched in 'apple ios is amazing'
print('#4', sentence.index('amazing', 20, len(sentence)))
# 5 When substring not found, will return error
#result = sentence.index('android', 20, len(sentence)) it throughs exception & execution stop
#print("#6", result)

"""
isalnum()
Returns true if all characters in a string are alphanumeric (i.e both alphabets or numeric), else returns false.
Syntax:str.isalnum()
"""
def check(name):
    if name.isalnum()==True:
        print("All characters are alphanumeric in", name)
    else:
        print("All characters are not alphanumeric in ", name)

word = "onetwothree123"
check(word)
word = "one two three 1 2 3"
check(word)

"""isalpha()
Returns true if all characters in the string are alphabets, else returns false.
Syntax:str.isalpha()"""

def check(name):
    if name.isalpha() == True:
        print("All characters are alphabetic in", name)
    else:
        print("All characters are not alphabetic in ", name)
word = "onetwothree"
check(word)
word = "one two three 1 2 3"
check(word)

"""
isalpha()
Returns true if all characters in the string are alphabets, else returns false.

Syntax:str.isalpha()
"""

def check(name):
  if name.isalpha() == True:
      print("All characters are alphabetic in", name)
  else:
      print("All characters are not alphabetic in ", name)
word = "onetwothree"
check(word)
word = "one two three 1 2 3"
check(word)

"""14. isdecimal()
Returns true if all characters in the string are decimal, else returns false.
Syntax:str.isdecimal()"""

number = "123"
print("#1",number.isdecimal())
# floats are not consider as decimal
number = "123.12"
print("#2",number.isdecimal())
# Unicode character (U+0660 (Arabic-Indic Digit Zero)) is also considered as a decimal
number = "\u0660"
print("#3",number.isdecimal())
# returns false for sub/superscript numbers as well
number = '²3455'
print("#4",number.isdecimal())
# returns false for alphas
number = "onetwothree"
print("#5",number.isdecimal())


"""isdigit
Returns true if all characters in the string are digits, else returns false.
Syntax:str.isdigit()
"""
number = "123"
print("#1",number.isdigit())
# floats are not consider as digit
number = "123.12"
print("#2",number.isdigit())
# Unicode character (U+0660 (Arabic-Indic Digit Zero)) is also considered as a digit
number = "\u0660"
print("#3",number.isdigit())
# returns true for sub/superscript numbers as well
number = '²3455'
print("#4",number.isdigit())
# returns false for alphas
number = "onetwothree"
print("#5",number.isdigit())


"""
isidentifier()
Returns true if the string is a valid identifier in python, else returns false.
Syntax: str.isidentifier()
"""

identifier = "Math"
print("#1",identifier.isidentifier())
identifier = "Python"
print("#2",identifier.isidentifier())
identifier = "Py#hon"
print("#4",identifier.isidentifier())

"""
islower()
Returns true if all alphabets in the string are lowercase, else returns false.
Syntax:str.islower()
"""
def checkForLower(x):
    if x.islower():
        print("All alphabets are in lower case")
    else:
        print("All alphabets are not in lower case!")
checkForLower("hello")
checkForLower("Hello")
checkForLower("W@$$up")

"""
isnumeric()
method supports Digits, Vulgar Fractions, Subscripts, Superscripts, Roman Numerals, Currency Numerators.
isprintable()
Returns true if all characters in the string are printable. If even a single character is non printable, it returns false.
str.isprintable()

Printable Characters:
letters and symbols
digits
punctuation
Whitespace

"""
S = 'Hello, World!'
x = S.isprintable()
print(x)
S = 'Hello \n World!'
x = S.isprintable()
print(x)
S = 'Hello \t World!'
x = S.isprintable()
print(x)

"""
isspace()
Returns true if there are only white space characters in the string. If not, returns false.

Syntax:str.isspace()
"""

S = '    '
x = S.isspace()
print("#1",x)
S = ''
x = S.isspace()
print("#2",x)
S = '  h. e. l'
x = S.isspace()
print('#3',x)
