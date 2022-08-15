import module

print(module.base)
print(module.square(10))

# 모듈.클래스()로 person 모듈의 클래스 사용
maria = module.Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()