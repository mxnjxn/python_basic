# random 모듈의 shuffle() 과 sample()
# shuffle() --> 리스트 안에 있는 데이터를 무작위로 썩어줌 --> 리스트에서만 사용 가능
# sample(리스트, 원하는 갯수) --> 리스트 내에서 원하는 갯수의 값을 뽑는 동작을 수행함.--> 한 번에 원하는 갯수 만큼의 번호를 중복없이 뽑을 수 있음

from random import *
n_list = [1, 2, 3, 4, 5]
print(n_list)

shuffle(n_list)
print(n_list)

print(sample(n_list, 1))  # 리스트 내에서 1개를 무작위로 뽑기

# 퀴즈
# 퀴즈 내에서는 아이디 값들을 가진 리스트를 shuffle() 함수를 이용하야 한번 뒤 섞고, sample() 함수를 이용해서 추첨을 하도록 만들어보세요

print("solution to quiz")


id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
shuffle(id)

chicken = sample(id, 1)  # 리스트 형태는 int가 될 수 없음 --> str이 될 수 는 있음
print(str(chicken))
del id[id.index(str(chicken))]  # index(숫자)

coffee = sample(id, 3)

print("-----당첨자 발표-----\n")
print("치킨 당첨자: %s" % chicken)
print("커피 당첨자: {}" .format(coffee))
print("-----축하합니다----- \n")


# 두 가지 방법
# method 1: 4명을 뽑고 그 중에서 한 명을 치킨, 세명을 커피로 지정
# range() 를 이용해서 리스트 만들기 --> 값이 커지면 일일이 입력할 수 없음
users = list(range(1, 21))
shuffle(users)

winners = sample(users, 4)
print("-----당첨자 발표-----\n")
print("치킨 당첨자: {}" .format(winners[0]))
print("커피 당첨자: {}" .format(winners[1:]))
print("-----축하합니다----- \n")

# method 2 : 1명 뽑고 나머지 1명을 제외한 3명 뽑기
print("#method2")
id_2 = list(range(1, 21))
shuffle(id_2)

chicken_winner = sample(id_2, 1)

remainers = list(set(id_2) - set(chicken_winner))
coffee_winners = sample(remainers, 3)

print("-----당첨자 발표-----\n")
print("치킨 당첨자: {}" .format(chicken_winner))
print("커피 당첨자: {}" .format(coffee_winners))
print("-----축하합니다----- \n")
