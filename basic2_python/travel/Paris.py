class ParisPackage:
    def detail(self):
        print("파리 패키지 여행! ")


if __name__ == "__main__":
    print("파일 내부에서 모듈 실행! ")
    to_do = ParisPackage()
    to_do.detail()
else:
    print("파일 외부에서 모듈 실행! ")
    

