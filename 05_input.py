# 05_input.py

'''
    프로그램에서 값을 입력 받고, 유동적인 코드를 작성

    표준입출력 : standard input/output

    input() 작동 순서
        1. '입력 대기 상태'
        2. 입력 후 엔터
        3. 입력된 내용이 '문자열'로 반환
            > 입력된 값을 변수에 대입, 바로 사용
'''
# (1) input()이 사용되면 입력 대기 상태가 된다.
#input()

# (2) 입력된 내용은 '문자열'로 돌아오기 때문에, 변수에 대입 가능
'''
input_str = input()
print("입력한 값 :", input_str)
'''
# (3) input()은 입력한 문자열이기 때문에, 바로 사용도 가능
#print("입력한 값2 : "+ input())

# (4) input() 함수의 또 다른 기능
'''
print("문자열을 입력 : ", end='')
input_str = input()
'''
'''
input_str = input("이름 입력 : ")
# 1. 문자열 출력
# 2. 입력대기 상태
# 3. 입력 후 엔터 -> 문자열로 반환
# 4. 반환 된 값을 변수에 대입
print("이름은 {} 입니다.".format(input_str))
'''


# (5) 입력된 값을 숫자로 다루겠다.
'''
input_num = input("숫자 입력 : ")

input_num = int(input_num)

print("입력한 값은 {} 입니다.".format(input_num + 10))
'''
'''
input_num1 = int(input("첫 번째 숫자 입력 : "))
input_num2 = int(input("두 번째 숫자 입력 : "))
print("두 수의 합 :", input_num1 + input_num2)
'''

# 여러 값을 입력 받고 정수로 변환
# split() : 기준 되는 문자로 해당 문자열을 나눈다. (나눈 결과는 리스트로 반환)
print("하 하 하".split())

# map() : 특정한 함수를 반복사용할 때
# map(반복 수행할 함수의 이름, 요소가 여러 개인 값)

#a, b = 1, 2
a, b = map(int, ["1", "2"])
# a, b = int("1"), int("2")
# a, b = 1, 2
print(a+b)
print()

num1, num2 = map(int, input("두 수 입력 : ").split())

print(num1 + num2)
























































