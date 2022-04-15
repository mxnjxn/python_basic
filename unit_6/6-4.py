# continue 와 break
# 반복문의 흐름을 제어한다.

# continue --> 더 이상 아래 명령들을 실행하지 않고 다음 반복 대상으로 넘어갈 때 사용함
# break --> 즉시, 반복문을 탈출하는데 사용함.

absent = [2, 5]

for student in range(1, 11):
    if student in absent:
        continue  # 아래 명령을 실행하지 않음./ 다음 반복 대상으로 넘어감.
    print("{0}, 책을 읽어봐" .format(student))


#
absent_n = [3, 4]
no_book = [7]  # 책을 가져오지 않은 학생 출석번호

for student in range(1, 11):
    if student in absent_n:
        continue
    elif student in no_book:  # 책을 가져오지 않았으면 바로 수업 종료(반복문 탈출 --> break)
        print("오늘 수업은 여기까지야. {0}는 교무실로 따라와" .format(student))
        break
    print("{0}, 책을 읽어봐." .format(student))
