# P15 date caculate
from datetime import datetime

today = datetime.now()
print('Today is :' + str(today))

from datetime import timedelta
yesterday = today - timedelta(days=1)
print('Yestoday is: ' + str(yesterday))
print(f'Yestoday is: {str(yesterday.month)}月{str(yesterday.day)}日')
