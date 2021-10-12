# Python program to extract numeric digit
# from A string by regular expression...

# Importing module required for regular
# expressions
# import re
#
# # Example String
# s = 'My 2 favourite numbers are 7 and 10'
#
# # find all function to select all digit from 0
# # to 9 [0-9] for numeric Letter in the String
# # + for repeats a character one or more times
# lst = re.findall('[0-9]+', s)
#
# # Printing of List
# print(lst)






# Python program to extract emails From
# the String By Regular Expression.

# Importing module required for regular
# expressions
import re

# Example string
s = """Hello from shubhamg199630@gmail.com
		to priya@yahoo.com about the meeting @2PM"""

# \S matches any non-whitespace character
# @ for as in the Email
# + for Repeats a character one or more times
lst = re.findall('\S+@\S+', s)

# Printing of List
print(lst)
