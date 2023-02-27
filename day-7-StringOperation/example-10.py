"""rpartition()
Returns a 3 element tuple, by splitting the string at the last occurrence of the argument and returns a tuple containing the string before the last occurrence of argument, the argument and string after the last occurrence of argument.

Syntax:
str.rpartition(separator)
Parameters:

    Separator: will part the string considering only the first occurance of this ‘Separator’.

Note: if separator is not found, the method returns a tuple containing the string itself, followed by two empty strings
"""
S = 'How are you? How have you been?'
x = S.rpartition('are') # splits/parts on the basis of last occurence of this parameter
print(x)
# NOTE: parts/splits only on the first occurance
S = 'How are you? How have you been?'
x = S.rpartition('you') # will part the sentence considering only the last occurance of 'you'
print(x)
# Note: if a separator is not found, the method first returns a tuple containing the string itself, followed by two empty strings.
S = 'How are you? How have you been?'
x = S.rpartition('xyz') # won't part the sentence
print(x)


"""
rsplit()
Returns a list of strings by splitting the original string into substrings on the basis of a separator. By default the separator is a space ‘ ’.
Syntax:str.rsplit(separator, maxSplit)
"""

# by default rsplit is made on the basis of space ' '
S = 'Good morning, how are you?'
x = S.rsplit()
print(x)
# 1st optional parameter signifies specific identifier based on which rsplit has to be made
S = 'stop,look,go'
x = S.rsplit(',')
print(x)
# 2nd optional parameter is maxsplit, only maxsplit number of splits are made starting from the right side
S = 'stop,look,go,stop,look,go'
x = S.rsplit(',',3)
print(x)

"""
rstrip()
Returns a string by removing the trailing characters from the right. (depends on the parameter provided)

Syntax:
str.rstrip(charactersToBeRemoved)
"""
S = '  Hello   World!   '
x = S.rstrip()
print(x) # removes only trailing spaces
# if any other trailing character/characters is to be removed instead of space ' ' then optional param 'chars' can be used
S = '.....Hello World......'
x = S.rstrip('.')
print(x)
# multiple character can also be considered while removing trailing characters
S = '...www...Hello ...www.... World...www....'
x = S.rstrip('.w')
print(x)
"""
split()
Returns a list of strings by splitting the original string into substrings on the basis of a separator. By default the separator is a space ‘ ’.

Syntax:str.split(separator, maxSplit)
"""

# by default rsplit is made on the basis of space ' '
S = 'Good morning, how are you?'
x = S.rsplit()
print(x)
# 1st optional parameter signifies specific identifier based on which rsplit has to be made
S = 'stop,look,go'
x = S.rsplit(',')
print(x)
# 2nd optional parameter is maxsplit, only maxsplit number of splits are made starting from the right side
S = 'stop,look,go,stop,look,go'
x = S.rsplit(',',3)
print(x)

"""
splitlines()
Returns a list of strings by splitting the string at line breaks and returns a list of strings that were lines in the original string.

Syntax:
str.splitlines(keepends)
"""
# splits only on the basis of line breaks
S = 'one\ntwo'
x = S.splitlines()
print(x)
# \n \r \n \f are also a part of line breaks
S = 'one\ntwo\r\nthree\ffour'
x = S.splitlines()
print(x)
# \n is also a part of line break
S = 'one two\nthree four'
x = S.splitlines(True)
print(x)
# Unlike split, it returns an empty array. Split returns an array with empty string in this case
S = ''
x = S.splitlines()
print(x)

"""
startswith()
Returns true if a string starts with a specific string prefix. If not, returns false.

Syntax:str.startswith(prefix, start, end)

"""

S = "Hello world, good morning. Hello How do you do?"
x = S.startswith("Hello")
print("#1", x)
x = S.startswith("How")
print("#2", x)
x = S.startswith("Hello", 27, 40)
print("#3", x)
x = S.startswith("Hello", 27)
print("#4", x)
tup = ("Hello", "How")
x = S.startswith(tup)
print("#5", x)
x = S.startswith(tup, 6, 20)
print("#6", x)

"""
 strip()
Returns a string by removing both trailing and leading characters from the string. (what character is removed depends on the parameter provided)

Syntax:str.Strip(charactersToBeRemoved)
"""

S = '  Hello   World!   '
x = S.strip()
print(x) # removes only trailing spaces
# if any other trailing character/characters is to be removed instead of space ' ' then optional param 'chars' can be used
S = '.....Hello World......'
x = S.strip('.')
print(x)
# multiple character can also be considered while removing trailing characters
S = '...www...Hello ...www.... World...www....'
x = S.strip('.w')
print(x)

"""
swapcase()
Returns a string by swapping the case of the original string’s characters i.e. lower case alphabets are swapped with its upper case alphabets and visa-versa.

Syntax:str.swapcase()
"""

S = "Hello World"
print(S.swapcase())

S = "h@llo W0Rld"
print(S.swapcase())
# swaps cases for alphabets and ignores special characters and numbers

"""
title()
Returns a title-cased string by converting the first character of each word to uppercase and remaining characters of each word to lowercase of the original string.

Syntax:str.title()
"""

S1 = 'welcome to scaler'
print(S1.title())
S2 = 'WeLcOme tO sCaLeR'
print(S2.title())
S3 = "welCome to Scaler's class.s,s|s?s>s"
print(S3.title())

"""
translate()
Returns a string by replacing each character with its corresponding character provided in the mapping table that has mapping of each character (that is to be replaced) and its corresponding replacement.

Syntax:str.translate(mappingTable)
"""

S = "hey, how are you?"
x = S.maketrans('hrae',
                'zabc')  # replacing 'h' with 'z', 'r' with 'a' and so on. Check 'maketrans()' method for more information.
print("#1", S.translate(x))
# third optional parameter deletes all characters

# creating a mapping table manually
# replacing 'a' with 'A', 'h' with 'H', 'e' with ''
translation = {97: 65, 104: 72, 101: None}
print("#2", S.translate(translation))

"""
upper()
Returns a string by converting each lower case to upper case alphabets.

Syntax:str.upper()
"""
S1 = "hey, how are you?"
print(S1.upper())
S2 = "Hey, HOw arE yoU?"
print(S2.upper())


"""
zfill()
Returns a string with character ‘0’ padded or concatenated to the left.

Syntax:str.zfill(width)
"""
s1 = 'abc'
print(s1.zfill(10))

s2 = '123'
print(s2.zfill(15))

s3 = '+123'
print(s3.zfill(12))

s3 = '-a233-123'
print(s3.zfill(12))

