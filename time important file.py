from datetime import datetime
from time import sleep, time

# print(datetime.now().time())
# print(datetime.now().date())
# getTime = datetime(2020,2,20, 10,20,30)
# print(getTime.strftime('date:%a %d %b %Y  time:%H:%M:%S'))
i = 0
startTime = time()
while True:
    sleep(5)
    print('Harry is a good boy.')
    # startTime = time()
    i = i + 1
    if i == 4:
        break