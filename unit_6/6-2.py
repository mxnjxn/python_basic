# for 문
# for 변수 in sequence

for waiting_no in range(1, 6):
    print("대기번호: {0}" .format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]  # 손님 리스트
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다".format(customer))
