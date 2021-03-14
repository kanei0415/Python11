# 11_module_package.py

'''
    [모듈과 패키지]
        모듈(module)
            - 변수, 함수, 클래스 등을 모아 놓은 소스파일
            - 간단한 기능을 담을 때 사용
            - 다른 파이썬 프로그램에서 불러와 사용할 수 있도록 만들어진 소스 파일

        패키지(package)
            - 여러 모듈을 묶은 것
            - 코드가 많고 복잡할 때 사용
            - 관련모듈들 끼리 한 폴더에 넣어놓은 형태 (폴더 = 패키지)

            - 폴더 안에 __init__.py 파일이 있어야 패키지가 됐었다.
              파이썬 3.3버전 부터는 없어도 패키지로 인식
'''

#import sys
#print(sys.path)
# sys.path.append("C:\\test\\test1\\test2") 형태로 경로 추가

# 패키지의 모듈 사용 - 그외 as, from 등의 사용은 동일
'''
import koreais.koreais_module
print(koreais.koreais_module.my_str)
'''

# __init__.py 파일을 이용한 import
# 패키지의 __init__.py 파일이 가장 먼저 수행된다.

# 1. 현재폴더에서 koreais_module을 import
'''
import koreais
print(koreais.koreais_module.my_str)
'''

# 2. 현재폴더의 koreais_module에서 모두 import
# 모듈명 생략
'''
import koreais
print(koreais.my_str)
'''

'''
from koreais import *
print(my_str)
'''

# 3. __all__ 사용
'''
import koreais
print(koreais.my_str)
print(koreais.mul(10, 4))
'''
from koreais import *
print(my_str)
print(add(10, 3))
print(mul(1, 2))



















































            
