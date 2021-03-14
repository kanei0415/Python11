# koreais_main.py           (koreais 폴더 안 저장)

# 모듈 불러오기 (1) - 모듈명 그대로 사용
'''
import koreais_module
print(koreais_module.my_str)
print(koreais_module.add(1, 20))

import random
print(random.randint(1, 10))
'''

# 모듈 불러오기 (2) - as 별칭주기
'''
import koreais_module as km
print(km.my_str)
print(km.add(10, 2))
'''

# 모듈 불러오기 (3) - 모듈에서 일부만 사용
'''
from koreais_module import my_str, add, mul
print(my_str)
print(add(10, 2))
print(mul(2, 2))
'''

# 모듈 불러오기 (4) - 전체 사용
'''
from koreais_module import *
print(my_str)
print(mul(10, 4))
dog = Dog("바둑이")
dog.cry()
'''

import koreais_module








































































