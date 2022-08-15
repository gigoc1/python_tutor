#__init__.py 파일은내용을 비워 둘수 있음
# from . import operation    # 현재 패키지에서 operation 모듈을 가져옴
# from . import geometry     # 현재 패키지에서 geometry 모듈을 가져옴

#__all__는 모든것(*)을 가져갈 때의 목록을 정함
__all__ = ['add', 'triangle_area']    # calcpkg 패키지에서 add, triangle_area 함수만 공개

from .operation import *
from .geometry import *

