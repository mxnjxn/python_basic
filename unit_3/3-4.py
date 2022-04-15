# random function(랜덤 함수) --> 난수
from random import *
print(random())  # 0.0 이상 1.0 미만의 임의의 값을 생성

print(random()*10)  # 0 ~ 10미만
print(int(random()*10))  # 0 ~ 10 미만의 정수
print(int(random()*10)+1)  # 1 ~ 11미만의 정수

print(int(random()*45)+1)  # 1부타 46미만

# 보다 쉽게 원하는 법위 내의 랜덤 함수를 뽑는 함수를 제공함. --> 정수
# randrange(1,45) --> 1부터 45미만
# randint(1,44) --> 1부타 44까지 --> 마지막 수 포함.
print(randrange(1, 46))
print(randint(1, 12))

# summary
# random()
# randrange(a,b)
# randint(a,b)

print(random()*20)  # 0에서 20미만 까지
print(int(random()*20))  # 0애서 20미만 까지의 정수를
print(int(random()*20)+1)  # 1에서 21미만 까지의 정수

print(randrange(0, 21))  # 0 에서 21미만의 정수
print(randrange(10, 21))  # 10애서 21미만의 정수
print(randint(0, 20))  # 0에서 20까지의 정수
print(randint(2, 3))  # 2에서 3까지 정수
