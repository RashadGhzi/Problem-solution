import datetime
from datetime import datetime

# # Print date and time
# print(datetime.datetime.now())

# # only time
# print(datetime.datetime.now().time())

# (Feb 25 2020  4:20PM) convert it into Python’s datetime object.

date_string = "Feb 25 2020  4:20PM"
datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print(datetime_object)



## Substract(minus) a week(7days)  from given date.
"""from datetime import datetime,timedelta
given_date = datetime(2020,6,20)
print("Given date: ", given_date)

res_date = given_date-timedelta(days=7)
print(res_date)"""




# given_date = datetime(2020, 2, 25)
# print("Given date is :", given_date)
# print("Converted to :",given_date.strftime('%A %d %B %Y'))
