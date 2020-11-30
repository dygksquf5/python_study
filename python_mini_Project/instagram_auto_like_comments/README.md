# There are two different versions
1) using BeautifulSoup & selenium 
2) just Selenium 

But, as a result, I decided to use just Selenium for automating, 
due to a structure of Instagram. 
If you utilise the BeautifulSoup, you would face some scroll problem, I mean, you could control about scroll height, 
however, the process of crawling couldn't make me feel happy. It wasn't quite smooth when it comes to working on Instagram.
Thus, eventually, you would face some problems.

Due to the this reason, I would like to say that Using just Selenium would much better for this. 

# 어떠한 해쉬태그를 사용하여 검색할지, 좋아요 클릭을 몇번 반복할지에 대한 입력값을 입력
<img width="652" alt="Screenshot 2020-11-30 at 12 51 20 PM" src="https://user-images.githubusercontent.com/66229916/100567027-e7686480-330a-11eb-998c-6bb0ac10c577.png">

# Selenium 을 사용하기에 Xpath를 사용하여 필요한 구간을 찾는데, 동일한 버튼도 해쉬태그마다 크게 2가지로 나뉘기때문에 해당 버튼이 어떤 Xpath 가지고있는지 먼저 알아보기
<img width="749" alt="Screenshot 2020-11-30 at 12 51 07 PM" src="https://user-images.githubusercontent.com/66229916/100567033-eb948200-330a-11eb-8607-e7f958e853be.png">

# 시작할 때와 탐색을 끝냈을 때의 시간을 time 모듈로 알아내고 시간이 10초 이상 초과될 경우 다음 페이지로 자동넘기기 ( 무한로딩 걸렸을 때를 해결하기 위함)
<img width="522" alt="Screenshot 2020-11-30 at 12 51 36 PM" src="https://user-images.githubusercontent.com/66229916/100567039-ee8f7280-330a-11eb-8715-fcfc82c31193.png">

# 연속적인 like 버튼 클릭은 자동화 프로그램 방지 프로그램이 작동할 수 있음, 300번 클릭마다 300초씩 sleep 하여 블락 방지하기.
<img width="550" alt="Screenshot 2020-11-30 at 12 52 15 PM" src="https://user-images.githubusercontent.com/66229916/100567047-f222f980-330a-11eb-9bad-72069ce02b5a.png">
