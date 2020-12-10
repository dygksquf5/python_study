class LondonPackage:
    def detail(self):
        print("런던 패키지 여행! ")


if __name__ == "__main__":
    print(" 내부에서 모듈 사용! ")
    to_do = LondonPackage()
    to_do.detail()
else:
    print("외부에서 모듈 사용 ")
