# a = int(input('첫 번째 숫자를 입력하세요: '))
# b = int(input('두 번째 숫자를 입력하세요: '))
 
# print(a + b)
# a, b = input('문자열 입력하세요: ').split()    # 입력받은 값을 공백을 기준으로 분리
 
# print(a)
# print(b)

# a, b = map(int, input('숫자 두 개를 입력하세요: ').split())
 
# print(a + b)

a, b = map(int, input('숫자 두 개를 입력하세요: ').split(',')) # 입력받은 값을 콤마를 기준으로 분리
 
print(a + b)