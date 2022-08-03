# setdefault: 키-값 쌍 추가
# update: 키의 값 수정, 키가 없으면 키-값 쌍 추가
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.setdefault('e'))
print(x)

x.update(a=90) #update(키=값)은 키가 문자열일때만 사용 가능
print(x)
x.update(a=10, e=50, f=60)
print(x)
# 키가 숫자일 경우, update(딕셔너리)로 처리
x.update({1:'ONE',3:'THREE'})
print(x)

#딕셔너리 키-값 삭제
print(x.pop('a'))
print(x)
x.update(a=10)
print(x)
del x['a']
print(x)
x.update(a=10)

#딕셔너리 임의의 키-값 삭제
print(x.popitem()) #파이썬 3.6이상에서는 마지막 키-값 삭제
print(x)

#딕셔너리 모든 키-값 삭제
x.clear()

#딕셔너리 키의 값 가져오기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.get('a'))

#딕셔너리 모든 키-값 가져오기
# items: 키-값 쌍을 모두 가져옴
# keys: 키를 모두 가져옴
# values: 값을 모두 가져옴
print(x.items())
print(x.keys())
print(x.values())

#리스트/튜플로 딕셔너리 만들기
keys = ['a','b','c','d']
x=dict.fromkeys(keys,100)
print(x)

#defaultdict 사용하기
from collections import defaultdict # collections 모듈에서 defaultdict를 가져옴
y = defaultdict(int)    # int로 기본값 생성
print(y['z'])
y = defaultdict(lambda: 'python')    # 0이 아닌 다른값으로 생성
print(y['z'])