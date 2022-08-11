#정규표현식은 re 모듈을 가져와서 사용
#re.match('패턴', '문자열')
import re
print(re.match('Hello', 'Hello, world!'))     # 문자열이 있으므로 정규표현식 매치 객체가 반환됨
print(re.match('Python', 'Hello, world!'))    # 문자열이 없으므로 아무것도 반환되지 않음

#문자열 맨앞에 오는지 맨뒤에 오는지 판단하기
print(re.search('^Hello', 'Hello, world!'))     # Hello로 시작하므로 패턴에 매칭됨
print(re.search('world!$', 'Hello, world!'))    # world!로 끝나므로 패턴에 매칭됨

#지정된 문자열이 하나라도 포함되는지 판단하기
print(re.match('hello|world', 'hello'))    # hello 또는 world가 있으므로 패턴에 매칭됨)