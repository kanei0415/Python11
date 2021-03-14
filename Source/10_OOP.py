# 10_OOP.py

'''
    [Object Oriented Programming] - 객체 지향 프로그래밍
        - 객체지향이론
            실제 세계는 사물(객체)로 이루어져 있으며,
            발생하는 모든 사건들은 사물(객체)간의 상호작용이다.

        - 특징
            1. 코드의 재사용성이 높다.
            2. 코드를 관리하기 좋다.
            3. 프로그램의 신뢰성이 높아진다.

        - '클래스'와 '객체'
            1. 클래스는 일종의 설계도(틀)이며,
               객체는 그 설계도를 통해 만들어진 실제 사물
                   갤럭시s20 설계도 --> 갤럭시s20

            2. 클래스(class)
                - 정의 : 객체를 정의해 놓은 것
                - 용도 : 객체를 생성

            3. 객체 (object)
                - 정의 : 실제로 존재하는 것
                - 용도 : 클래스에 정의된 대로 사용

            - 객체 / 인스턴스
                1. 인스턴스 (instance) : 사례, 경우, 실체
                    클래스를 통해 실제로 만들어진 객체를 '인스턴스'

            - 객체의 구성 요소 : 속성, 기능
                (속성 : 갤럭시s20의 색상정보, 기능 : 갤럭시s20으로 사진을 찍는다.)

                > 객체는 클래스에서 정의한 다수의 속성과 기능을 가질 수 있다.
                    >> 속성 : 변수
                    >> 기능 : 함수
'''
# OOP

'''
    1. 클래스(설계도)는 속성(변수)을 정의하거나, 기능(함수)을 정의할 수 있다.

    2. 클래스 안에 정의된 함수는 '메서드(method)' 라고 부른다.
        > 메서드를 만들 때는 반드시 최소 하나의 매개변수가 필요한다. (규칙)
        > self 라는 이름으로 만든다.
'''

class Car:
    def power_on(self): # self는 매개변수가 아니라 인스턴스의 역할을 한다. 
        print("부릉부릉!")
        self.power = True # bmw.power = True, bmw 인스턴스에 power 변수를 추가 
        self.drive() # bmw.drive()

    def drive(self):
        print("주행시작~!")
        
# 인스턴스 생성
# 변수명 = 클래스명()
bmw = Car() # Car 클래스의 객체(인스턴스) 생성
bmw.power_on() # 클래스에 정의된 함수 호출
print("bmw의 시동 여부 :", bmw.power)

# 클래스에 여러 속성/기능을 정의 해두고, 인스턴스라는 하나의 단위로 묶어서 다루겠다.

tico = Car()
tico.drive()
#print("tico의 시동 여부 :", tico.power)
tico.power = "시동켜짐"
print("tico의 시동 여부 :", tico.power)

tico.model = "TICO의 최신모델"
#print(bmw.model)
print(tico.model)

# 만들어지는 인스턴스별로 속성(변수)이 다를 수 있다.

# 클래스 없이 자동차 2대를 다뤄보기
car1_model = "BMW" # 모델명 
car1_power = False # 시동 on/off
car1_max_speed = 200 # 최고 속도 

car2_model = "SONATA"
car2_power = True
car2_max_speed = 180
print()
# 자동차가 주행하는 함수
def drive_car(model, power, max_speed, speed): # speed : 주행하고 싶은 속도 
    print("{} 주행 준비..".format(model))
    if power == False:
        print("주행불가 : 시동을 켜주세요")
        return
    if speed > max_speed:
        print("{}의 최고속도는 {}km입니다. 속도를 줄입니다.".format(model, max_speed))
        speed = max_speed
    print("{}km로 주행합니다. 출발~~".format(speed))

drive_car(car1_model, car1_power, car1_max_speed, 200)
#           "BMW"       False           200       200
print()
drive_car(car2_model, car2_power, car2_max_speed, 200)
#           "SONATA"    True            180       200

# 1) 각 변수들은 서로 전혀 연관성이 없다.
# 2) 함수를 호출할 때, 일일이 매개변수로 모든 값을 전달해줘야 한다.
print()
class Car:
    def drive_car(self, speed): # speed : 주행하고 싶은 속도 
        print("{} 주행 준비..".format(self.model))
        if self.power == False:
            print("주행불가 : 시동을 켜주세요")
            return
        if speed > self.max_speed:
            print("{}의 최고속도는 {}km입니다. 속도를 줄입니다.".format(self.model, self.max_speed))
            speed = self.max_speed
        print("{}km로 주행합니다. 출발~~".format(speed))

car1 = Car()
car2 = Car()
car1.model = "BMW"
car1.power = False
car1.max_speed = 200

car2.model = "SONATA"
car2.power = True
car2.max_speed = 180

car1.drive_car(200)
car2.drive_car(200)

# drive_car 호출 시, 정의된 매개변수는 2개이다.
# self에는 자동으로 호출하는 인스턴스가 대입
# 그 뒤 매개변수부터는 호출할 때 값을 전달

# 1) 인스턴스라는 하나의 변수에 모든 속성들을 담아놨다. (연관성이 생김)
# 2) 함수를 호출할 때 그냥 호출해도 self에 인스턴스가 대입되기 때문에
#    함수의 수행문 안에서 self.~~를 그대로 사용할 수 있다.
print()


# 3. 생성자
#   1. 인스턴스 생성 시 자동으로 호출되는 메서드(함수)
#   2. 목적 : 인스턴스 생성과 동시에 속성을 추가/초기값 지정을 하고 싶을 때 사용(초기화)
#   3. 생성자 함수의 이름 : __init__

class Car:
    def __init__(self, model, power, max_speed):
        print("생성자 호출!")
        self.model = model
        self.power = power
        self.max_speed = max_speed
    
    def drive_car(self, speed): # speed : 주행하고 싶은 속도 
        print("{} 주행 준비..".format(self.model))
        if self.power == False:
            print("주행불가 : 시동을 켜주세요")
            return
        if speed > self.max_speed:
            print("{}의 최고속도는 {}km입니다. 속도를 줄입니다.".format(self.model, self.max_speed))
            speed = self.max_speed
        print("{}km로 주행합니다. 출발~~".format(speed))

car1 = Car("BMW", False, 200)
car1.drive_car(200)
car2 = Car("SONATA", True, 180)
car2.drive_car(200)
print()

# 생성자 함수를 이용하면, 모든 인스턴스가 공통적으로 지녀야할 속성을 만들 수 있다. 

# 4. 변수와 메서드(함수)의 종류
'''
    - 클래스 변수
        1. 클래스 내부 코드에 생성
        2. 클래스 메서드에서 생성
        3. 클래스 코드 바깥에서 클래스명을 통해 생성
        
    - 인스턴스 변수
        1. 생성자에서 생성
            > 모든 인스턴스가 공통적으로 생성
        2. 인스턴스 메서드에서 생성
            > 해당 인스턴스 메서드를 호출한 인스턴스만 생성
        3. 클래스 코드 바깥에서 인스턴스명을 통해 생성
            > 해당 인스턴스에만 생성

    * 클래스변수는 한 번 만들어지면 '클래스명'이나 '인스턴스'가 접근(사용) 가능
    * 인스턴스변수는 인스턴스별로 독립적으로 생성(해당 하는 인스턴스만 사용 가능)

    - 클래스 메서드
        클래스나 인스턴스가 호출 가능
        
    - 인스턴스 메서드
        인스턴스를 통해서만 호출 가능 (클래스명으로 접근 불가능)
'''

class Car: # 클래스 정의하는 영역 
    engine = "1000cc" #클래스 변수

    @classmethod # 장식자(데코레이터) : 이게 있어야만 클래스메서드 동작 
    def clsMethod(cls):
        print("클래스 메서드")
        cls.clsValue = "클래스변수"

    def instMethod(self):
        print("인스턴스 메서드")
    
# 클래스 변수 사용 --> 클래스명.클래스변수명
print(Car.engine)
Car.clsMethod()
print(Car.clsValue)

#Car.instMethod()
car1 = Car()
print(car1.engine)
print(car1.clsValue)
car1.clsMethod()

Car.wheel = 4
print(car1.wheel)
car1.SunRoof = "썬루프 옵션 장착"

#print(Car.SunRoof)

print()

# 5. 외부 접근 제어
# 외부 = 클래스가 정의된 코드 바깥
# public : 외부 접근 허용 - 이름을 지을 때 그냥 지으면 된다.(변수/메서드)
# private : 외부 접근 차단 - 이름을 지을 때 이름 앞에 __(언더바 2개)를 붙여야된다.

class Person:
    name = "이몽룡"
    __addr = "대구시 중구"

    def print_info(self):
        print("{}님은 {}에 거주합니다.".format(self.name, self.__addr))

    def __print_info(self):
        print("__print_info()")
        print("{}님은 {}에 거주합니다.".format(self.name, self.__addr))

    def print_info2(self):
        print("print_info2()")
        self.__print_info()
        
person = Person()
print(person.name)
#print(person.__addr)
person.print_info()
#person.__print_info()
person.print_info2()
