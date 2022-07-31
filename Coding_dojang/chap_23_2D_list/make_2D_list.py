#for반복문으로 2D 리스트 만들기(23.3)
a = []    # 빈 리스트 생성
for i in range(3):
    line = []              # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(2):
        line.append(0)     # 안쪽 리스트에 0 추가
    a.append(line)         # 전체 리스트에 안쪽 리스트를 추가
print(a)

#list 표현식으로 2D 리스트 만들기
a = [[0 for j in range(2)] for i in range(3)]
print(a)
a = [[0] * 2 for i in range(3)] # [0]*2 = [0,0]
print(a)

#톱니형 리스트 만들기
a = [3, 1, 3, 2, 5]    # 가로 크기를 저장한 리스트
b = []    # 빈 리스트 생성
 
for i in a:      # 가로 크기를 저장한 리스트로 반복
    line = []    # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(i):    # 리스트 a에 저장된 가로 크기만큼 반복
        line.append(0)
    b.append(line)        # 리스트 b에 안쪽 리스트를 추가
 
print(b)
a = [[0] * i for i in [3, 1, 3, 2, 5]]
print(a)

#2D 리스트 정렬하기
students = [
    ['john', 'C', 19],
    ['maria', 'A', 25],
    ['andrew', 'B', 7]
]
print(sorted(students, key=lambda student: student[1]))  # 안쪽 리스트의 인덱스 1을 기준으로 정렬
print(sorted(students, key=lambda student: student[2]))  # 안쪽 리스트의 인덱스 2를 기준으로 정렬