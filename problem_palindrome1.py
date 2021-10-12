# Python3 program for the
# practical application of reverse()

# list1 = [1, 2, 3, 2, 1]
#
# # store a copy of list
# list2 = list1.copy()
#
# # reverse the list
# list2.reverse()
#
# # compare reversed and original list
# if list1 == list2:
# 	print("Palindrome")
# else:
# 	print("Not Palindrome")






# Python program to check
# if a string is palindrome
# or not
st = 'malayalam'
j = -1
flag = 0
for i in st:
	if i != st[j]:
		flag = 1
		break
	j = j - 1
if flag == 1:
	print("NO")
else:
	print("Yes")

