# 06_Conditional.py

'''
    제어문 - 조건문, 반복문
        > 코드를 상황에 따라 제어한다.

    [조건문]
        조건을 판단하여 상황에 맞게 처리

        if문   -만약, ~~ 면
            '만약' 조건에 만족하면 수행해라!
                만족한다 = True
                만족 x   = False
'''

# 조건문

if 3 > 0:
    print("3은 0보다 크다")
    #print(3 > 0)

'''
[if문 기본 구조]
if 조건식:
    수행문

elif 조건식:
    수행문

elif 조건식:
    수행문

else:
    수행문

    1. 조건식
        참(True)이나 거짓(False)이 있어야 한다. 식의 결과가 T/F
        조건식의 끝에는 콜론(:)을 붙인다.
        콜론(:) 뒤부터는 수행문으로 간주

    2. 수행문
        조건식이 만족할 때 수행하는 코드들
        반드시 들여쓰기를 해야한다. --> 공백 4개
        수행문 코드 간의 들여쓰기가 맞지 않으면 오류가 난다.

        들여쓰기만 맞으면 수행문을 여러 줄 작성할 수 있고
        들여쓰기를 끝내면 if문의 수행문이 끝난 것

    3. elif 조건식 :  (else if) 다른 만약
        위 조건식이 만족하지 않으면 이 조건식은 만족하느냐?
        if문에 종속된다. (if문 없이 사용불가)
            > 조건문의 시작은 if문으로 시작
        여러 개 사용 가능

    4. else :
        위 조건식이 만족하지 않으면 '무조건' 수행해라!
            > 조건식이 없다.
        if문에 종속된다.
        하나만 사용 가능

        > if문 밑에 elif나 else가 종속된 경우 하나의 '조건문'
        
'''

# 입력한 값이 양/음/0 판별
'''
num = int(input("숫자 입력 : "))

if num > 0:
    print("양수")

elif num < 0:
    print("음수")

#elif num == 0: # 비교 연산 기호 중 == 기호는 같은지 비교 
#    print("0이다.")

else:
    print("0이다.")
'''
# if문 중첩 (다중 if문)
print()
'''
score = int(input("점수 입력 : "))

if score >= 60 : # 크거나 같으면
    print("합격")
    if score == 100:
        print("만점입니다.")
    print("진심으로 축하합니다.")
else:
    if score == 0:
        print("빵점....")
    print("불합격")
'''

'''
    [비교연산자]
        조건식에 자주 사용되는 연산자

        a < b   a가 b보다 작냐?
        a > b   a가 b보다 크냐?
        a <= b  a가 b보다 작거나 같냐?
        a >= b  a가 b보다 크거나 같냐?
        a == b  a와 b가 같냐?
        a != b  a와 b가 다르냐? 

    [논리연산자]
        a or b    a 또는 b 중에 하나라도 참이면 참 / 둘 다 거짓이어야 거짓
        a and b   a와 b 둘 다 참이어야 참 / 둘 중 하나라도 거짓이면 거짓
        not a     a가 참이면 거짓으로 / 거짓이면 참으로 

    [포함연산자]
        a in b      b안에 a가 있으면 참 / 없으면 거짓 
        a not in b  b안에 a가 있으면 거짓/ 없으면 참

        ex) if 4 in [1, 2, 3, 4]: print("4")

        "A" in ["A", "B"] --> True
        "A" in "ABC"      --> True
        "A" in ["AB", "ABC", "AC"] --> False
'''

a, b = map(int, input("두 수 입력 : ").split())

# and
'''
if a > 0 and b > 0:
    print("둘 다 양수")

elif a < 0 and b < 0:
    print("둘 다 음수")
'''
# or
'''
if a > 0 or b > 0:
    print("둘 중 하나는 양수")

if a < 0 or b < 0:
    print("둘 중 하나는 음수")
'''

# not
'''
if not a > 0:
    print("첫 번째 양수가 아니다.")
'''

# in, not in

my_list = [1, 2, 3]
'''
if a in my_list:
    print("첫 번째 숫자는 1,2,3 중에 있다.")

if b not in [1, 2, 3]:
    print("두 번째 숫자는 [1, 2, 3]중에 없다.")
'''

if ((a in my_list) and (b in my_list)):
    print("둘 다 1,2,3 중에 있다.")

if ((a in my_list) or (b in my_list)):
    print("둘 중 하나는 1,2,3 중에 있다.")

#if a > 5 and a < 10:
    
    

































































        
