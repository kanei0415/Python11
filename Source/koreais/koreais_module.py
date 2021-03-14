# koreais_module.py         (koreais 폴더 안 저장)

# 변수
my_str = "koreais_module의 문자열!"

# 함수
def add(a, b):
    return a + b

def mul(a, b):
    return a * b

# 클래스
class Dog:
    def __init__(self, name):
        self.name = name

    def cry(self):
        print("{} : 멍멍!".format(self.name))

if __name__ == "__main__":  
    print("koreais_module 수행문~~!")

# __name__ 변수 --> 파이썬에서 제공하는 변수
# 내가 직접 실행 : "__main__"
# import : import한 이름 그대로 저장 (문자열)

    print(__name__)












