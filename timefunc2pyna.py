from datetime import datetime
## Today week day .
given_date = datetime.today()
print(given_date.strftime('%A'))

## Only time
given_date1 = datetime.today().time()
print(given_date1)



# Today week day.
# import calendar
# from datetime import datetime

# given_date = datetime(2021,7,3)
# week_day = calendar.day_name[given_date.weekday()]
# print(week_day)

# Today week day
"""from datetime import datetime
time1 = datetime.now()
week_day = time1.strftime('%A')
print(week_day)"""