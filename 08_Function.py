# 08_Function.py

'''
    [함수 - Function]  (method 메서드, 메소드)
        - 특정 작업을 수행하는 일련의 문장들을 하나로 묶은 것

        - 함수의 장점
            1. 한 번 만들어 놓으면 언제든지 재사용 가능
            2. 중복된 코드 제거
            3. 프로그램의 구조화

    [함수의 기본 구조]
    def 함수이름(매개변수):
        수행문
        return 반환 값

        1. 매개변수 (parameter)
            - 함수가 호출 될 때 값을 받을 '변수'
            - 개수 제한없고, 필요 없으면 생략 가능
            - 우리가 함수를 호출할 때 전달하는 '값'을 '인수'라고 부른다.
                > argument

        2. 반환 값
            - return 뒤에 오는 값은, 함수의 수행이 완료되고 되돌려주는 값
            - return을 사용하면 함수의 수행이 끝난다.

        - 매개변수와 반환 값의 유/무에 따른 함수 형태
            1. 매개변수와 반환 값이 둘 다 있다.
            2. 매개변수와 반환 값이 둘 다 없다.
            3. 매개변수만 있다.
            4. 반환 값만 있다. 

'''

# 함수는 정의하기만 하면 프로그램 수행에 영향이 없다.

# 1. 매개변수, 반환 값 둘 다 있다.
def add(a, b):
    return a+b

# add함수는 매개변수가 2개 -> 값을 2개 전달
result = add(3, 5) # 함수 호출 (1)
print("{} + {} = {}".format(3, 5, result))
print("{} + {} = {}".format(100, 200, add(100, 200))) # 함수호출 (2)
# 반환 값이 있는 함수를 호출 했을 때는
# 함수의 기능 수행이 끝난 뒤 반환 값을 들고 온다.
# (1) add(3, 5)는 함수의 반환 값인 8로 대체 -> 변수 대입
# (2) add(100, 200) -> 300으로 대체 -> format()에서 사용
print()

# 2. 매개변수, 반환 값 둘 다 없다.
def sayHo():
    print("HoHo~~")
    print("HoHohohohohoHoHo!!")

# 함수를 호출하면 코드의 흐름이 내가 호출한 함수의 수행문으로 점프
# 함수의 수행문이 끝나면 함수를 호출했던 원래 위치로 되돌아온다.
# 단, return 반환 값이 있다면 그 값을 들고온다.

print("sayHo 호출 전")
sayHo()
print("sayHo 호출 후")
print()

# 매개변수에 따라 함수를 호출할 때는 그 규칙을 맞춰줘야 한다.
# 반환 값에 따라서는 그 규칙을 맞추지 않아도 사용은 가능

result = sayHo() # None : 내용이 없다는 뜻
print("sayHo의 결과1 :", result)
print("sayHo의 결과2 :", sayHo())
print()

# 3. 매개변수만 있다.
def say(talk):
    print(talk)

say("안녕하세요")

# 4. 반환 값만 있다.
def get():
    return "good day!!"

print(get())
str1 = get()
print(str1)

# ================================================================

# 여러 값 반환하기
def calc(a, b):
    return a+b, a-b, a*b, a/b # 튜플 

print(calc(10, 3))
a, b, c, d = calc(10, 3)
# a, b, c, d = (13, 7, 30, 3.333333..)

print(a, b, c, d)
print()

# 매개변수에 초기 값 사용
def print_info(name, age, phone="010-xxxx-xxxx"):
    print("이름 :", name)
    print("나이 :", age)
    print("전화번호 :", phone)

print_info("홍길동", 20, "010-1234-5678")
print()
print_info("아이유", 19)
print()

# print()함수의 sep=' ', end='\n'은 초기값이 적용된 매개변수

# 매개변수에 초기 값을 적용하려면, 초기 값이 들어가는 매개변수는 맨 뒤에 위치

# 키워드 인수 : 함수의 매개변수명을 키워드로 사용

def print_info(name, age, phone):
    print("이름 :", name)
    print("나이 :", age)
    print("전화 :", phone)

print_info("홍길동", 20, "010-1111-2222")
print_info(age=25, phone="112", name="경찰서") 
# print(1, 2, 3, sep='', end='')
print()

print(1, 2, 3)
print()

# 가변인수 : 전달하는 값의 개수가 변할 수 있다.

def add(*args): # *떼면 튜플
    for i in args:
        print(i,"", end='')

add(1, 2, 3, 5, 6)
print()

# 일반 매개변수, 가변인수를 혼용할 때 가변인수는 마지막에 위치
'''
def fn(*args, a):
    print(args)

fn(1, 2, 3, 4, 5, 6, 7, a=1)
'''
print()

def func3():
    print("func3() 시작")
    print("func3() 끝")
def func2():
    print("func2() 시작")
    func3()
    print("func2() 끝")
def func1():
    print("func1() 시작")
    func2()
    print("func1() 끝")

print("func1 호출 전")
func1()
print("func1 호출 후")
print()

'''
    재귀함수
        - 함수의 수행문 안에서 나 자기 자신 함수를 다시 호출하는 함수
        - 수행문이 반복되기 때문에 반복문과 유사
        - 너무 많이 반복 수행하다보면 프로그램 오류 발생
        - 함수 호출 시 'stack'이라는 구조의 메모리를 사용
            Queue : First In, First Out(FIFO) - 입구/출구 따로
            Stack : First In, Last Out(FILO) - 출입구 하나(우물)
                > Stack 용량이 초과될 정도로 많이 호출하면 오류
                > StackOverFlow 오류
                > 함수 수행이 끝난 후 돌아갈 위치를 저장하고 있어서
                  함수는 Stack을 사용
'''

def func(num):
    print("func() 시작, num =", num)
    if num == 1:
        print("num이 1일때부터 끝")
        return # 함수에서 반환 값없이 return만 쓰면 함수 종료 

    func(num - 1) # 내 함수를 다시 호출 = 재귀호출
    print("func() 끝, num =", num)

func(3)                
print()

# 지역변수와 전역변수
#  지역변수 : 특정 지역에서만 사용가능한 변수
#  전역변수 : 전체 영역에서 사용가능한 변수 

value = "전역변수"

def func1():
    print("func1() 호출!")
    print(value)

def func2():
    print("func2() 호출!")
    value_func2 = "func2의 지역변수"
    print(value_func2)

    # value 라는 전역변수가 이미 있는데 지역에서 value에 값을 대입하게되면
    # 전역변수 value의 값이 변경되는게 아니라 같은 이름으로
    # 이 지역의 value 지역변수가 생성
    value = "지역변수로 변경"
    print(value)

def func3():
    print("func3() 호출")
    global value_func3 # 지역변수를 전역변수로 만드는 명령
    value_func3 = "func3의 지역변수"

func1()
print()
func2()
#print(value_func2) # func2에만 존재하는 value_func2
print(value)
func3()
print(value_func3)



















































