# 리스트 --> 변수에 하나 하나 지정해야 하는 값을 리스트는 여러개를 한꺼번에 저장 할 수 있다.
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 값의 위치(인덱스)를 확인할 수 있다.
#변수명.index() == 변수명.find()
print(subway.index("조세호"))


# 리스트에서 값을 추가하기 --> append() --> 맨 마지막에 추가 함
subway.append("하하")
print(subway)

# insert(삽입할 인덱스 숫자, 삽입할 인덱스 값)
# 리스트 마지막에 추가하는 append() 가 아닌 리스트 값 사이에 새로운 값을 삽입
subway.insert(1, "정형돈")
print(subway)

# pop() --> 맨 뒤에서 값을 하나씩 뺌
print(subway.pop())  # 어떤 값이 없어졌는지 보여줌.
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

#
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 숫자로 이루어진 리스트
num_list = [5, 2, 4, 3, 1]

# sort() --> 오름차순으로 정리
num_list.sort()
print(num_list)

# reverse() --> 순서를 거꾸로 뒤집기.
num_list.reverse()
print(num_list)

# clear() --> 모든 값을 없애기
num_list.clear()
print(num_list)


# 문자열에는 모든 자료형을 다 넣을 수 있음
mix_list = ["조세호", 20, True]

# 두 리스트를 합치기 --> extend()
num_list = [5, 2, 4, 3, 1]
num_list.extend(mix_list)  # num_list 에 mix_list를 합쳐라
print(num_list)
