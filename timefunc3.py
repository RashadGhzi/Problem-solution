# from datetime import datetime,timedelta
"""
given_date = datetime(2020, 3, 22, 10, 0, 0)
print(given_date)
add1 = given_date+timedelta(days=7,hours=12)
print(add1)
"""

from datetime import datetime
# Convert the following datetime into a string
given_date = datetime(2020, 2, 25)
print(given_date)

n = given_date.strftime("%Y-%m-%d %H:%M:%S")
print(n)


# from datetime import datetime,timedelta


# # 2020-02-25
# given_date = datetime(2020, 2, 25).date()
# print(given_date+timedelta(days=(30*4)+1))

