import json


# Dictionary ={1:'Welcome', 2:'to',
# 			3:'Geeks', 4:'for',
# 			5:'Geeks',}

# # Indentation can be used for pretty(সুন্দর)-printing
# json_string = json.dumps(Dictionary,indent = 6)

# print('Equivalent json string of dictionary:',
# 	json_string)






# Dictionary ={1:'Welcome', 2:'to',
# 			3:'Geeks', 4:'for',
# 			5:'Geeks'}

# # If specified, separators should be
# # an (item_separator, key_separator)tuple
# # Items are separated by '.' and key,
# # values are separated by '='
# json_string = json.dumps(Dictionary,separators =(". ", " = "))

# print(type(json_string))
# print('Equivalent json string of dictionary:',json_string)







Dictionary ={3:'Welcome', 2:'to',
			1:'Geeks'}

json_string = json.dumps(Dictionary,sort_keys = True)

print('Equivalent json string of dictionary:',
	json_string)
