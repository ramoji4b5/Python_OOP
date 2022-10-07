
##Sys module##

"""The sys module has a variable named argv. All the command line arguments are stored as a list of strings.

If you want the first command-line argument entered, you can access it by argv[0]."""

import sys

if len(sys.argv) != 3:
  raise ValueError("Please provide your name and age")

print(f' Your name is {sys.argv[1]} and your age is {sys.argv[2]} and {sys.argv[0]}')