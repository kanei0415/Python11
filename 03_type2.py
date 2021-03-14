# 03_type2.py
# 파이썬의 자료형들 : 숫자, 문자, 리스트, 튜플, 집합, 딕셔너리, bool

'''
    [3. 리스트 자료형]
        - 데이터들의 목록
        - 편리하다.

        리스트명(변수) = [요소1, 요소2, 요소3, ...]
'''
# 리스트 만들기
list1 = [] # 요소가 없는 빈 리스트
list2 = [1, 2, 3] # 정수
list3 = ["A", "B", "C"] # 문자열
list4 = [1, "A", 2, "B"] # 혼합
list5 = [1, "A", [2, "B"]] # 리스트 안에 또 다른 리스트 

print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print()

# type() : 자료의 종류를 가르쳐준다.
print(type(1))
print(type(1.9))
print(type("12"))
print(type([1,2]))
print()

# 리스트 인덱싱, 슬라이싱
# 순서가 있다 = 인덱싱, 슬라이싱 가능

my_list = ["아이유", "지코", "박서준"]
print(my_list)
print(my_list[0])
print()

num_list = [1, 2, 3]
print(num_list[2] + 10)
print()

# 이중 리스트 인덱싱 (리스트 안에 리스트를 요소로 가짐)
my_list = ["아이유", "지코", ["박서준", "송혜교"]]


print(my_list[2]) # 리스트
print(my_list[2][1])
print(my_list[2][0][2])
print()

# 슬라이싱도 동일하게 쓰인다.

a = [0, 1, 2]
print(a[0:2])
print(a[0:1])
# 슬라이싱의 결과는 무조건 '리스트'
print()

# 리스트 연산하기
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

print("덧셈 :", a+b) # 연결 
c = a+b
print(c)
print("곱셈 :", a*2) # 반복
print()

# 리스트 수정하기(변경, 삭제)

a = [1, 2, 3, 4, 5, 6]
a[2] = -1
print("변경 후 :", a)

#a[0:2] = 0 
a[0:2] = [0]
print("변경 후 :", a)
a[0:2] = [6, 7, 8]
print("변경 후 :", a)

a[0] = [1, 2]
print("변경 후 :", a)
print()

# 리스트 요소 삭제
a = [1, 2, 3, 4, 5, 6]

a[0:3] = [] # 슬라이싱해서 [] 대입하면 제거
print(a)
a[0] = []
print(a)

del(a[0])
print(a)

del(a[0:2])
print(a)
print()

# 리스트 관련 함수
# 리스트.함수()

# append(value) : 리스트 가장 뒤에 value를 추가

a = [1, 2, 3]
a.append(4)
print("a =", a)

a.append("아이유")
print("a =", a)

a.append([1, "A", 2])
# append는 하나의 요소만 추가할 수 있다.
print("a =", a)
print()

# sort() : 리스트 정렬하기 (숫자, 알파벳, 한글 등)

a = [2, 4, 3, 1]
a.sort() # 기본이 오름차순
print("a =", a)
a.sort(reverse=True) # 내림차순
print("a =", a)
print()

# reverse() : 리스트 뒤집기 (정렬x)
a = [2, 3, 4, 1]
a.reverse()
print("a =", a)
print()

# index(value) : 리스트에서 value를 찾고, 그 위치를 반환
a = [1, 2, 3, 4]
print("a에서 2의 위치 :", a.index(2))
print()

# insert(index, value) : 지정한 위치에 값 삽입
a.insert(2, "굿")
print("a =", a)
print()

# remove(value) : 리스트에서 '처음' 찾은 값(value) 제거
a = [1, 2, 3, 1]
a.remove(1)
print("a =", a)
#a.remove(5) # 없는 값을 지우려 하면 오류
print()

# count(value) : 리스트에 존재하는 value의 개수 반환
a = [1, 2, 3, 1, 2, 2, 2, 1, 1, 3, 3, 2, 1, 2, 3, 2]
print("a에서 2의 개수 :", a.count(2))
print()

# pop(index) : 리스트에서 index번째 값을 뽑아낸다.
#   > 뽑아낸 값을 우리가 사용할 수 있다.
#   > 리스트에서 해당 값을 제거
a = ["A", "B", "C", "D"]
print(a.pop(1))
print("a =", a)

print(a.pop()) # 인덱스 생략 시 기본이 맨 뒤
print("a =", a)
print()

# len() : 요소의 개수를 구하는 함수
a = [1, 2, 3, 4] # 리스트
b = "1234" # 문자열
c = 1234 # 숫자

print("리스트 요소의 개수 :", len(a))
print("문자열 요소의 개수 :", len(b))
#print("정수 요소의 개수 :", len(c))
# 값이 여러 개 존재하는 자료형만 len()를 사용할 수 있다.
print()

#copy() : 모든 값들을 '복제'하여 새로운 리스트 생성
a = [1, 2, 3, 4]
b = a.copy()
c = a

print("기존 a :", a)
print("복제 b :", b)
print("대입 c :", c)
print()

a[0] = -30
print("기존 a :", a)
print("복제 b :", b)
print("대입 c :", c)
print()

# clear() : 리스트의 모든 요소 제거
a.clear()
print("a =", a)
print()

# list의 요소들이 '문자열'로만 이루어진 경우
# 문자열 관련 함수 중 join()을 이용하여 '하나의 문자열'을 만들 수 있다.
my_list = ["대", "한", "민", "국"]
print("!".join("join"))

print("".join(my_list))
print()

'''
    [4. 튜플(Tuple)]
        - 리스트와 비슷하다.
            > 차이점
                1. 생성법
                    리스트 []
                    튜플 ()

                2. 튜플은 한 번 만들면 변경할 수 없다.
'''

# 튜플 만들기
a = ()
b = (1,) # 요소가 한 개일 땐 뒤에 콤마를 붙인다. 
c = (1, 2, 3, "A", "B", "C")
d = 1, 2, 3, 4 # () 생략해도 튜플
e = (1, "A", (2, "B"))

print(a)
print(b)
print(c)
print(d)
print(e)
print()

# 튜플은 변하지 않는다.
a = 1, 2, 3, 4
print(a[0])
print(a[0:2])
print()

#a[0] = -1
#del(a[0])

# 덧셈, 곱셈 연산 가능
a = 1, 2, 3, 4
b = 6, 7, 8, 9
c = a + b
print(c)
print(c * 2)












