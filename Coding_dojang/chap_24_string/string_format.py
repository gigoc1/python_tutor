print('- 서식 지정자')
print('I am %s.' % 'james')
print('I am %d years old.' % 20)
print('%.2f' % 2.3)
print('Today is %d %s.' % (3, 'April'))

print('\n- format 메서드')
print('Hello, {0} {2} {1}'.format('Python', 'Script', 3.6))
print('{0:0<10}'.format('python')) #'{인덱스:[[채우기]정렬][길이][.자릿수][자료형]}'
print('{0:->10}'.format('python'))
print('{0:08.2f}'.format(150.37))