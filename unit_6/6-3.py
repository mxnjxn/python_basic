# 조건이 만족하는 동안 끝 없이 반복한다.

customer = "토르"
index = 5

while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1} 한번 남았어요." .format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

customer_1 = "아이언맨"
person = "unkonwn"

while person != customer_1:
    print("커피가 준비 되었습니다.")
    person = input("이름이 어떻게 되세요??: ")
