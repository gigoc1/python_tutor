#합집합 연산: |
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)
print(set.union(a, b))

#교집합 연산: &
print(a & b)
print(set.intersection(a, b))

#차집합 연산: -
print(a - b)
print(set.difference(a, b))

#대칭차집합(symmetric difference): ^(XOR)
print(a ^ b)
print(set.symmetric_difference(a, b))

#집합 연산 후 할당
  # 세트1 |= 세트2, 세트1.update(세트2)
  # 세트1 &= 세트2, 세트1.intersection_update(세트2)
  # 세트1 -= 세트2, 세트1.difference_update(세트2)
  # 세트1 ^= 세트2, 세트1.symmetric_difference_update(세트2)

#부분집합, 상위집합 확인
  # 부분집합 확인
    # 세트1 <= 세트2, 세트1.issubset(세트2)
  # 상위집합 확인
    # 세트1 >= 세트2, 세트1.issuperset(세트2)

# 같은지 확인
  # ==, !=
# 겹치는지 확인
  # 세트1.isdisjoint(세트2)