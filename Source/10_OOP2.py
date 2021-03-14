# 10_OOP2.py

'''
    상속
        - 무언가를 물려받는다.
        - 클래스의 상속
            기존에 정의해놓은 클래스의 기능을 그대로 물려받는 새로운 클래스를 정의한다.

        - 기반클래스 : 부모클래스, 슈퍼클래스
        - 파생클래스 : 자식클래스, 서브클래스

        - 자식클래스에서는 부모클래스의 변수, 메서드를 사용할 수 있다.

        [오버라이딩] (재정의)
            - 부모클래스에 정의된 메서드를 무시하고
              자식클래스에서 같은 이름으로 다시 정의한다.
'''
# 부모클래스
class Person:
    def __init__(self, name, age):
        print("Person, 생성자")
        self.name = name
        self.age = age

    def print_info(self):
        print("Person, print_info")
        print("이름 :", self.name)
        print("나이 :", self.age)

    def sleep(self):
        print("Person, sleep")
        print(self.name + "님은 8시간 잡니다.")

# 자식클래스1
class Student(Person): # 상속받을 클래스를 ()안에 적는다.
    def study(self):
        print("Student, study")
        print(self.name + "학생은 6시간 공부합니다.")

    def sleep(self):
        print("Student, sleep")
        print(self.name + "학생은 7시간 잡니다.")

# 부모클래스 인스턴스 생성
person = Person("홍길동", 20)
person.print_info()
person.sleep()        
print()

# 자식클래스 인스턴스 생성
student = Student("아이유", 25)
student.print_info()
student.sleep()
# 자식클래스에 똑같은 이름의 메서드가 있다면 (오버라이딩)
# 부모의 것이 아닌 자식의 메서드가 호출
print()

# 자식클래스2
# super().메서드() --> 부모클래스의 메서드 호출
class Teacher(Person):
    def __init__(self, name, age):
        print("Teacher, 생성자")
        super().__init__(name, age) # 부모클래스 생성자 호출 

    def sleep(self):
        print("Teacher, sleep")
        super().sleep()

    def work(self):
        print("Teacher, work")
        print(self.name + "선생님은 9시간 일합니다.")

teacher = Teacher("이몽룡", 30)
teacher.print_info()
teacher.sleep()
teacher.work()
print()

'''
    추상 클래스
        추상적이다!
            동물이라는 클래스를 정의하며
            동물은 '운다'라는 추상적인 개념만 정의해놓고
            각 동물들이 실제로 어떻게 우는지는 각자 정의하도록 하는것 (자식클래스)

            - 운다 라는 메서드를 추상메서드라고 한다.

            - 추상메서드는 자식클래스가 '반드시'정의해야 한다. (강제)

    [사용방법]
    abc 필요 (abstract base class)
    from abc import *

    class 추상클래스명(metaclass=ABCMeta):
        @abstractmethod
        def 메서드명(self):
            pass

'''

from abc import *

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def Cry(self):
        pass

class Dog(Animal):
    def Cry(self):
        print("멍멍!")

dog = Dog()
dog.Cry()
            

















































































































