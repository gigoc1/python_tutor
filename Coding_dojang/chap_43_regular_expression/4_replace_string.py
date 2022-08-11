#re.sub('패턴', '바꿀문자열', '문자열', 바꿀횟수)
import re
print(re.sub('apple|orange', 'fruit', 'apple box orange tree'))    # apple 또는 orange를 fruit로 바꿈
print(re.sub('[0-9]+', 'n', '1 2 Fizz 4 Buzz Fizz 7 8'))    # 숫자만 찾아서 n으로 바꿈
