#세트에 요소 추가: add(요소)
a = {1, 2, 3, 4}
print(a, a.add(5))

#세트에서 특정요소 삭제: remove(요소), discard(요소)
print(a, a.remove(3))
print(a, a.discard(2))

#세트에서 임의의 요소 삭제: pop(), 삭제한 요소 반환
a = {1, 2, 3, 4}
print(a, a.pop())

#세트에서 모든 요소 삭제: clear()
print(a, a.clear())

#세트 요소 개수 구하기: len(세트)
a = {1, 2, 3, 4}
print(len(a))
