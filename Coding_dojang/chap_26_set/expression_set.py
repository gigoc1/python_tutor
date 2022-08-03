# for 반복문을 통한 세트 생성
# {식 for 변수 in 반복가능한객체}
# set(식 for 변수 in 반복가능한객체)
a = {i for i in 'apple'}
print(a)

# 세트 표현식에 if 사용
# {식 for 변수 in 세트 if 조건식}
# set(식 for 변수 in 세트 if 조건식)
print({i for i in 'pineapple' if i not in 'apl'})