print('- 문자열 바꾸기')
s = 'Hello, world!'
print(s.replace('world','word'))
s = s.replace('world!', 'Python')
print(s)

print('- 문자 바꾸기')
table = str.maketrans('aeiou', '12345')
print('apple'.translate(table))

print('- 문자열 분리하기')
print('apple, pear, grape, pineapple, orange'.split(', '))

print('- 구분자 문자열과 문자열 리스트 연결하기')
print(' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))

print('- 소문자<->대문자로 바꾸기')
print('python'.upper())
print('PYTHON'.lower())
