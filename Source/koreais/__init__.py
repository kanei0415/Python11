# __init__.py       (koreais 폴더 안 저장)

print("__init__.py 실행!")
# 이 파일이 실행되었을 때
# . --> 현재 폴더 (현재 위치)

# 1. 현재폴더에서 koreais_module을 import
#from . import koreais_module 

# 2. 현재폴더의 koreais_module에서 모두 import
# 모듈명 생략

#from .koreais_module import *

# 3. __all__ 사용
# import * 할 때 __all__이 들어간다.
# 내가 공개하고 싶은 항목만 추가

__all__ = ["my_str", "add", "mul"]
from .koreais_module import *


















