#파일객체 = open(파일이름, 파일모드)
#파일객체.write('문자열')
#파일객체.close()
file = open('hello.txt', 'w')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
file.write('Hello, world!\n')      # 파일에 문자열 저장
file.write('hello, kdk')
file.close()

file = open('hello.txt', 'r')    # hello.txt 파일을 읽기 모드(r)로 열기. 파일 객체 반환
s = file.read()                  # 파일에서 문자열 읽기
print(s)                         # Hello, world!
file.close()

# 자동으로 파일 객체 닫기
# with open(파일이름, 파일모드) as 파일객체:
#    코드

with open('hello.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    s = file.read()                     # 파일에서 문자열 읽기
    print(s)