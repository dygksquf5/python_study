# import travel.London
#
# to_do = travel.London.LondonPackage()
# to_do.detail()


# from travel import London
#
# to_do = London.LondonPackage()
# to_do.detail()

# 실행시켜보니 알수 있는건, 이렇게 모든 모듈을 travel 패키지에서 임포트 했을 때, 프로그램이 패키지에 있는 모~든 모듈을
# 한번씩 다 뒤진다. 시간이 걸릴듯 ㅠㅠ
# from travel import *
#
# to_do = Paris.ParisPackage()
# to_do.detail()

# import 할 모듈이 어디있는지 알고 싶을 땐! 밑의 방법을 사용 하기!

import inspect # 인스펙트 모듈 먼저 가져오고
import random # 예를들어 랜덤모듈 어디있는지 찾아보고자 할때
print(inspect.getfile(random)) # 그럼 알 수 있음!!
# 만약 다른 프로젝트를 할 때 패키지 만들고, 내 워크플레이스에 모듈(패키지 디렉토리) 파일 안두려면, 저 경로 설정 되어 있는 곳에다가 가져다 놓기!