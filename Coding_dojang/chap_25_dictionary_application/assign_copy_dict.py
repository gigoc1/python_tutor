# 리스트의 할당, 복사와 동일하나 중첩 딕셔너리는 다름
# 중첩 딕셔너리의 완전 복사는 copy 모듈의 deepcopy 함수 이용
x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
y = x.copy()
y['a']['python'] = '2.7.15'
print(x,y, sep='\n')

x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
import copy             # copy 모듈을 가져옴
y = copy.deepcopy(x)    # copy.deepcopy 함수를 사용하여 깊은 복사
y['a']['python'] = '2.7.15'
print(x,y,sep='\n')
