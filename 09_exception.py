# 09_exception.py

'''
    [예외처리]
        개발자가 의도하지 않은 오류 발생에 대한 처리
            > 프로그램 오류가 나면 프로그램이 종료

        try, except문

    try:
        기본 수행문(무조건 진입해서 수행)
    except:
        오류 발생 시 수행되는 수행문

'''
'''
try:
    input_num = int(input("숫자 입력 : "))
    print("결과 :", input_num)

except:
    print("숫자를 입력하세요!")

finally:
    print("예외처리 끝!")
'''
# (1) try문 : 오류가 발생되는 '예상'지역
# (2) except문 : 오류 발생 시 '처리'지역

# finally문 : 마지막에 무조건 수행되는 구문
#   > 정상/오류 구분 없이 무언가 마무리할 코드가 있을 때 사용

# 오류 구분하기
try:
    '''
    num1, num2 = map(int, input("두 수 입력 : ").split())
    print("나눈 결과 :", (num1 / num2))
    '''
    print(abc)
    my_list = [1, 2, 3, 4, 5]
    
    index = int(input("인덱스 입력 : "))
    try:
        print(my_list[index])
    except:
        print("인덱스가 잘못되었습니다.")
        

except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")

except ValueError:
    print("숫자를 정확히 입력하세요")

except:
    print("뭔진 모르지만 오류!")

num1, num2 = map(int, input("두 수 입력 : ").split())

if num2 == 0:
    print("0으로 나눌 수 없습니다.")
else:
    print("나눈 결과 :", (num1 / num2))































































