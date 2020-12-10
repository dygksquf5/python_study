import time, datetime

today_1 = time.localtime()
print(today_1)
print(time.strftime("%Y-%m-%d %H:%M:%S"))

print("오늘날짜는 ? : ", datetime.date.today())
# timedelta 두 날짜 사이의 간격!

today = datetime.date.today()
aniver = datetime.timedelta(days=100)

print( " 100일 후! : ", today + aniver)
