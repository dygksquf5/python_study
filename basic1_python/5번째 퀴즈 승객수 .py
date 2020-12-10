#cocoa 승객 수 구하는 어플 (퀴즈 )
# import random


# customer = range(1,51)
# time = random.randint(5, 50)
# for i in customer:
#     print("[?] {0} 번째 손님 (소요시간 :{1}  분)".format(i, time)) 
    
from random import *

count = 0

for i in range(51):
    time = randrange(5,51)
    if 5 <= time <= 15:
        print ("[0] {0} 번째 손님 (소요시간 : {1} 분 )" .format(i, time))
        count += 1
    else:
        print ("[ ] {0} 번째 손님 (소요시간 : {1} 분 )" .format(i, time))
        
print ( " 총 탑승객 \"{0}\"분 ".format(count))
    







