import datetime
now_time = datetime.datetime.now()
formatTime=now_time.strftime('%Y-%m-%d')
formatTime1=now_time.strftime('%Y%m')
print(formatTime,formatTime1)