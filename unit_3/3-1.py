# 3-1 연산자
# **=square, %=remaining, //=Quotient(몫)
# >, <, >=, <=,==(등호),
# != (좌항과 우항이 다르다) =/ 와 비슷

# 논리 연산자
# and= 두항 모두 참이면 참이다
# or= 둘 중 하나라도 참이면 참이다.
# not= ~의 반대
from math import *  # math library 안에 있는 모든 것을 import 하겠다는 뜻.
print(1+1)
print(3-2)
print(5*2)
print(4/3)  # 소숫점까지 계산이 되네????

print(2**4)
print(5 % 4)
print(5//3)
print(87//3)
print(87 % 3)

print(10 > 5)
print(57 <= 4)
print(3 < 23)
print(68 <= 5)

print(6 == 3)
print(9 == 9)

print(1 != 3)
print(2 != 2)

print(not(1 != 3))
print(not(2 != 2))

print((3 > 0) and (3 < 5))  # ()안 수식 넣어주기
print((2 > 0) & (3 < 5))  # and 대신에 &
print((3 > 5) or (8 < 3))
print((3 < 5) or (8 < 9))
print((4 < 5) or (9 < 8))
print((3 > 5) | (8 < 3))  # or 대신에 #shift, enter

print(5 > 3 > 2)
print(8 > 3 > 9)  # 앞이 거짓이라면 이후의 수식과 상관없이 항상 거짓이므로 그 뒤 수식은 수행하지 않는다
