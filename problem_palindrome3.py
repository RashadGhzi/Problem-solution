# function to check string is
# palindrome or not
# def isPalindrome(s):
#     # Using predefined function to
#     # reverse to string print(s)
#     rev = ''.join(reversed(s))
#
#     # Checking if both string are
#     # equal or not
#     if (s == rev):
#         return True
#     return False
#
#
# # main function
# s = "malayalam"
# ans = isPalindrome(s)
# print(ans)
#
# if (ans):
#     print("Yes")
# else:
#     print("No")






# Python program to check
# if a string is palindrome
# or not

x = "malayalam"

w = ""
for i in x:
	w = i + w

if (x == w):
	print("Yes")
else:
	print("No")


