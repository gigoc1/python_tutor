# 딕셔너리 언패킹
#   함수(**딕셔너리)
def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**x) #함수 매개변수와 딕셔너리의 키 이름, 개수가 같아야 함

#키워드 인수 사용하는 가변 인수 함수 만들기
#def 함수이름(**매개변수):
#    코드
def personal_info_kw(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep='')

personal_info_kw(**x)

#위치 인수와 키워드 인수를 함께 사용하기
def custom_print(*args, **kwargs):
    print(*args, **kwargs)
custom_print(1,2,3, sep=':',end='')


