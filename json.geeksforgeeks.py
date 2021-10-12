import json

Dictionary ={(1, 2, 3):'Welcome', 2:'to',
			3:'Geeks', 4:'for',
			5:'Geeks'}


# Our dictionary contains tuple
# as key, so it is automatically
# skipped If we have not set
# skipkeys = True then the code throws the error

json_string = json.dumps(Dictionary,skipkeys = True)

# ------------>  skipkeys: যদি skipkeys সত্য হয় (ডিফল্ট: মিথ্যা),
# তাহলে ডিক্ট কীগুলি একটি মৌলিক ধরনের নয় (str, int, float, bool, None)
# একটি TypeError বাড়ানোর পরিবর্তে বাদ দেওয়া হবে।

print('Equivalent json string of dictionary:',
	json_string)
print(type(json_string))







# We are adding nan values
# (out of range float values)
# in dictionary
Dictionary ={1:'Welcome', 2:'to',
			3:'Geeks', 4:'for',
			5:'Geeks', 6:float('nan')}

# If we hadn't set allow_nan to
# true we would have got
# ValueError: Out of range float
# values are not JSON compliant

json_string = json.dumps(Dictionary,allow_nan = True)
# allow_nan: যদি allow_nan মিথ্যা (ডিফল্ট: সত্য) হয়,
# তাহলে JSON স্পেসিফিকেশনের কঠোর সম্মতিতে সীমানার ফ্লোট ভ্যালু (nan, inf, -inf)
# এর ক্রমানুসারে এটি একটি ValueError হবে। যদি allow_nan সত্য হয়,
# তাদের জাভাস্ক্রিপ্ট সমতুল্য (NaN, Infinity, -Infinity) ব্যবহার করা হবে।


print('Equivalent json string of dictionary:',
	json_string)

