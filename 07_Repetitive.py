# 07_Repetitive.py
'''
    [반복문]
        조건에 만족하면 수행한다 (조건문과 동일)
            > 단 조건에 만족하지 않을 때까지

        1. while문
            - 조건식이 참이면 수행문 수행
            - if문과 기본 구조가 동일
                > if문 : 조건이 참이면 수행하고 끝
                > while문 : 조건이 참이면 수행하고 다시 조건식을 비교

        [while문 기본 구조]
        while 조건식:
            수행문
            수행문

'''
# while문

num = 0
while num < 3:
    print("num =", num)
    num += 1 # num = num + 1

# while문 순서
# 조건비교 -> (만족)수행 -> 조건비교 -> (만족)수행 -> ...

print()
'''
num = 0
while num < 3:
    print("num =", num)
'''

'''
    (1) 무한반복
    처음 반복문과는 다르게 num의 값을 수행문에서 증가시키지 않았다.
    조건식에서 비교 대상인 num의 값이 계속 동일하기 때문에
    항상 조건이 만족하여 반복문이 끝나지 않는다. --> 무한 반복 현상
    Ctrl + C : 강제 종료

    (2) 조건변수
    num과 같이 조건식의 비교에 사용되는 변수는 '조건변수'이다.
    반복문에서는 이 조건변수를 다루는게 매우 중요
    조건변수를 어떻게 다루었는지에 따라 반복 횟수가 정해진다.
    조건변수는 조건식에서 그 값이 사용되기 때문에 미리 생성되어진 변수여야 한다.

    초기 값 (조건변수 생성)
    while 조건식: (조건변수 사용)
        수행문 (반복해서 수행하고 싶은 코드 + 조건변수의 변화식)
'''

# 반복 횟수 지정

# 초기 값을 입력 받아 준다.
'''
count = int(input("반복할 횟수 입력 : ")) # 조건변수

while count > 0:
    print("count =", count)
    count -= 1
'''

# 특정 조건 만족
'''
input_num = "종료"

while input_num != 0:
    input_num = int(input("0을 입력하면 종료 : "))
'''

'''
    반복문 공통
        - break문 : 반복문을 빠져 나간다(탈출)

        - continue문 : 반복문의 첫 문장으로 돌아간다.
                       수행문을 끝낸다.
'''
# break
'''
while True: # 항상만족 -> 무한반복
    input_num = input("x을 입력하면 종료 : ")
    if input_num == "x" or input_num == "exit":
        break
'''    
                        
# continue 

num = 1
while num < 10:
    if num % 2 == 0: # 짝수
        num += 1
        continue

    print("num =", num)
    num += 1

print()

'''
    2. for문
        - 리스트, 튜플, 문자열 등 요소가 나열된 형태의 값을
          첫 요소부터 마지막 요소까지 변수에 대입하며 반복

        [for문 기본 구조]
        for 변수 in 리스트 또는 요소가 여러개인 값 :
            수행문

        ex) for a in [1,2,3]:
            

'''
# for문

# 범위 지정 반복문
for z in [1, 2, 3]:
    print(z)
print("for문 끝", z)

for z in "대한민국":
    print(z)

for z in [1, 2, 3, 4, 5]:
    print("hi~")

print()

'''
    range()함수 : 지정한 범위만큼의 숫자들을 반환

    for i in range(10): 0 ~ 9까지 순서대로 i에 대입
'''
for i in range(10):
    print(i)
print()

'''
    range(10) : 0 ~ 9
    range(5)  : 0 ~ 4

    range(1, 10) : 1 ~ 9 (끝은 포함x)
    range(50, 101) : 50 ~ 100

    range(1, 10, 2) : 1 ~ 9, 값이 2씩 증가 -> 1, 3, 5, 7, 9
    range(10, 0, -1) : 10 ~ 1, 값이 1씩 감소

    reversed(range(10)) : 0 ~ 9 를 뒤집는다. -> 9 ~ 0 

'''
print()

# for문으로 1 ~ 10까지 합 구하기

# 1 ~ 10까지 숫자들을 반복
# 누적할 변수
my_sum = 0

for i in range(1, 11): # 1 ~ 10
    my_sum += i # my_sum = my_sum + i

print("1~10까지 합 :", my_sum)
print()

# 입력 횟수만큼 반복
'''
count = int(input("반복 횟수 입력 : "))

for i in range(count, 0, -1):
    print(i)
print()

for i in reversed(range(1, count+1)):
    print(i)
'''

# for문 예시 (1)

# 손님리스트 : 이름, 나이

guest_list = [["아이유", 17], ["지코", 30], ["이민호", 24]]

num = 0
for guest in guest_list:
    #print(guest)
    name = guest[0]
    age = guest[1]
    num += 1
    print("{}번 손님 입장!".format(num))
    if age > 19:
        print("{}님은 성인입니다. 입장!".format(name))
    else:
        print("{}님은 미성년자입니다. 돌아가세요".format(name))

    if age < 20:
        print()
        continue

    print("{}번째 손님인 {}님은 성인입니다. {}세".format(num, name, age))
    print()

print()

# for문 활용 예시 2
# 구구단 출력 - for문의 수행문 안에 또 다른 for문이 중첩된 2중for문

for i in range(2, 10): # i : 2 ~ 9 --> 단 
    for j in range(1, 10): # j : 1 ~ 9 --> 곱 
        print("{} * {} = {}".format(i, j, (i*j)))
    print()

for i in range(1, 4): # 1 ~ 3
    for j in range(1, 4): # 1 ~ 3
        for k in range(1, 4): # 1 ~ 3
            print(i, j, k)

'''
    i j k
    1 1 1
    1 1 2
    1 1 3
    1 2 1
    1 2 2
    1 2 3
    1 3 1
    1 3 2
    1 3 3
    2 1 1
    2 1 2
    2 1 3
    2 2 1
    2 2 2
    2 2 3
    2 3 1
    2 3 2
    2 3 3
    3 1 1

'''













































































        
