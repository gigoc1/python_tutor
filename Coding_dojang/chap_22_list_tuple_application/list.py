#추가하기
l = [10, 20, 30]
l.append(500)
print(l)

l.extend([600, 700])
print(l)

l.insert(2, 33)
print(l)

#삭제하기
l.pop() #리스트의 마지막 요소 삭제
print(l)
print(l.pop(1)) #pop는 인덱스 요소를 삭제하고 삭제한 요소를 반환
                #del l[1]과 동일함
print(l)

l.remove(500) #리스트에서 처음 찾은 값을 삭제
print(l)

#특정 값의 인덱스 구하기
print(l.index(33)) #가장 먼저 찾은 인덱스 반환

#특정 값의 개수 구하기
print(l.count(33))

#리스트의 순서 뒤집기
l.reverse()
print(l)

#리스트 요소 정렬하기
    #sort() 또는 sort(reverse=False): 오름차순 정렬
    #sort(reverse=True): 내림차순 정렬

#리스트 모든요소 삭제
    #l.clear(): 빈 리스트 생성