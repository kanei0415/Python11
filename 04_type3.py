# 04_type3.py

'''
    [5. 딕셔너리 자료형]
        사전!
        형태 : {key1:value1, key2:value2, ....}
            > key와 value는 한 쌍
            key = 단어, value = 뜻

            - 요소가 여러 개 나열된 자료형이긴 한데
              리스트, 문자열, 튜플은 순서가 있어서 인덱스로 인덱싱
              딕셔너리는 순서가 없고, 'key'를 가지고 인덱싱

            - 주의사항
                1. key값은 중복되면 안 된다.
                2. key 값으로는 리스트, 딕셔너리를 사용할 수 없다.
                    key = 변하지 않는 성질의 자료
                    value = 상관 없음
'''
# 딕셔너리 만들기
my_dict = {"축구":"Soccer", 2002:"한일", (1, 2):("원", "투"), "16강":[2002, 2010]}

print(my_dict)
print(my_dict["축구"])
print(my_dict[2002])
print(my_dict[(1, 2)])
print(my_dict["16강"])
print(my_dict["16강"][0])
print()

# 딕셔너리 추가, 수정, 삭제
my_dict = {1:"a"}
my_dict[2] = "b"
# 딕셔너리[key] = value 
print(my_dict)

my_dict[2] = "c"
print(my_dict)

del(my_dict[1])
print(my_dict)
print()

'''
    [6. 집합(Set) 자료형]
        - 수학에서의 집합을 의미
            > 교집합, 합집합, 차집합 등

        - 중복된 값을 허용하지 않는다.
            > 중복 제거 용도로 사용

        - 순서가 없다.(인덱싱 불가능)
'''
my_set = {1, 2, 3, 4, 1, 2, 1, 2, 3, 2, 1, 2}
print(my_set)

my_set2 = {1, 2, 1, 2, 2, "A", "A", "B", "B"}
print(my_set2)
#print(my_set2[0])
print()

'''
    [7. bool 자료형]
        - 참(True)과 거짓(False)을 표현하는 자료형

        - 자료형의 값에 따른 참과 거짓

            값               True/False
            -----------------------------
            1                   True
            0                   False
            -1                  True
            "abc"               True
            ""                  False
            [1, 2]              True
            []                  False
            ()                  False
            None                False
            -----------------------------

            거짓인 경우
                1. 요소가 없다.
                2. 숫자가 0이다.
                3. None : 값이 없다는 걸 의미하는 자료형/값
'''

# bool(value) : 값이 참인지 거짓인지 판별 

print(bool(0))
print(bool(-10))
print(bool([]))
print(bool([1, 2]))
print()

'''
    str()   : 문자열로 변환
    int()   : 정수로 변환
    float() : 실수로 변환
    list()  : 리스트로 변환
    tuple() : 튜플로 변환
    dict()  : 딕셔너리로 변환
    set()   : 집합으로 변환
    bool()  : bool 자료형으로 변환
'''
my_str = str(123)
print("문자열 : "+ my_str)

print("숫자 :", int(my_str) + 10)

print("숫자 :", float(my_str) + 10)

print(list(my_str))
print(tuple(my_str))

print(dict(a="1", b="2"))

print(set(my_str))

'''
    숫자 : 그냥 쓰면 됨
    문자열 : 따옴표로 묶는다.(4가지)
    리스트 : []
    튜플 : ()
    딕셔너리 : {k:v}
    집합 : {}
    bool : True/False
'''





























































            
