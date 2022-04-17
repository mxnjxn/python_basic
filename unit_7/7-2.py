# 전달 값 과 반환 값 또한 2개 이상이 될 수 도 있음
# return을 통해 반환해주면 함수를 호출하는 곳에서 반환값을 받아서 변수에 저장할 수 있게 된다.

# def 함수이름(전달값1 , 전달값 2)
# 실행 명령문1
# 실행 명령문 2
# 실행 명령문 3
# return 반환값1, 반환값2

def deposit(balance, money):
    print("Money has been successfully transferred. Remaining balance is {}" .format(
        balance + money))
    return balance + money


balance = 0
balance = deposit(balance, 1000)
print(balance)

#


def withdraw(balance, money):
    if balance >= money:
        print("Withdrawal has been successfully processed. Remaining balance is {}" .format(
            balance - money))
        return balance - money

    else:
        print("Withdrawal has been declined. Remaining balance is {} " .format(balance))
        return balance


    # 입금
balance = 0
balance = deposit(balance, 1000)

# 출금
balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)
print(balance)

# 저녁에 출금해서 수수료 붙을 때


def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission  # 튜플 형식으로 반환


balance = 0
balance = deposit(balance, 1000)

# 저녁에 출금 시도
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액 {1} 원입니다." .format(commission, balance))
