"""
import 패키지.모듈
import 패키지.모듈1, 패키지.모듈2
패키지.모듈.변수
패키지.모듈.함수()
패키지.모듈.클래스()
"""
import urllib.request
response = urllib.request.urlopen('http://www.google.co.kr')
print(response.status)

# import 패키지.모듈 as 이름

"""
from 패키지.모듈 import 변수
from 패키지.모듈 import 함수
from 패키지.모듈 import 클래스
from 패키지.모듈 import 변수, 함수, 클래스
"""

"""
from 패키지.모듈 import 변수 as 이름
from 패키지.모듈 import 변수 as 이름, 함수 as 이름, 클래스 as 이름
"""