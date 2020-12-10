absent = [2,5] #결석
no_book = [7] #책을 안가져 옴!!! 

for student in range(1,11):
    if student in absent:
        continue  # continue 는 아래에 있는 실행문을 실행시키지 않고, 다시 for실행문으로 (처음) 돌아가서 실행하게 됨
    elif student in no_book:
        print("오늘수업은 여기까지, {0} 교무실로 와라".format(student))
        break
    print("{0}, 책 읽어봐".format(student)) # print 마지막으로 와야 돼, 코드는 항상 순서대로 읽기때문에, 코드의 역할을 잘 생각해보면 왜 마지막에 와야되는지 논리적으로 이해가능
    
    

