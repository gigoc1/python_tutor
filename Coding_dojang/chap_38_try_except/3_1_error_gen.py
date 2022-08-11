#에러 발생시키기
# raise 예외('에러메시지')
def three_multiple():
    x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0:                                 # x가 3의 배수가 아니면
        raise Exception('3의 배수가 아닙니다.')    # 예외를 발생시킴
    print(x)                                       # 현재 함수 안에는 except가 없으므로
                                                   # 예외를 상위 코드 블록으로 넘김
 
try:
    three_multiple()
except Exception as e:  # 하위 코드 블록에서 예외가 발생해도 실행됨, except가 나올때까지 상위코드로 이동
    print('예외가 발생했습니다.', e)