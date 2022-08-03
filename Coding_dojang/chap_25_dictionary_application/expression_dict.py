keys = ['a', 'b', 'c', 'd']
x = {key: value for key, value in dict.fromkeys(keys).items()}
print(x)

# 딕셔너리에서 특정값 찾아 삭제- 딕셔너리 표현식에서 if 사용
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x = {key: value for key, value in x.items() if value != 20}
print(x)
