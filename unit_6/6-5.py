# 한 줄 for
# 반복 대상을 하나 씩 순회하면서 변수에 저장하고 그 변수를 사용자가 원하는 동작을 수행하는 방식이며 생김새는 이렇습니다.

# [변수로 어떤 동작 for 변수 in 반복 대상(sequence)] --> 대괄호로 감싸져 있음 --> 리스트임

students = [1, 2, 3, 4, 5]
print(students)

students = [i + 100 for i in students]
print(students)


students_1 = ["Iron man", "Thor", "I am groot"]
print(students_1)

students_1 = [len(i) for i in students_1]
print(students_1)

students_2 = [a.upper() for a in students_1]
print(students_2)


# 한 줄 for 사용하지 않고 해보기
