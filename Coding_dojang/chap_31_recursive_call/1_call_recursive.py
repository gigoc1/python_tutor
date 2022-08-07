""" def hello():
    print('Hello, world!')
    hello()

hello() """
# 재귀호출 종료 조건 만들기
def hello(count):
    if count == 0:    # 종료 조건을 만듦. count가 0이면 다시 hello 함수를 호출하지 않고 끝냄
        return
    print('Hello, world!', count)
    count -= 1      # count를 1 감소시킨 뒤
    hello(count)    # 다시 hello에 넣음
 
hello(5)