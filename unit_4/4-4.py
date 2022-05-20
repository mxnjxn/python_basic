# 문자열포맷
print("a" + "b")  # 같은 자료형 끼리만 가능
print("a", "b")  # 자료형이 달라도 상관 없음.

# ********** 더 다양한 포맷
# %d --> 정수(decimal)
# %c --> 문자(character)
# %s --> 문자열(string) --> 정수, 문자, 문자열 상관없이 모든 값을 집어 넣을 수 있음.

'''
print("문자열 %d 문자열" % 정수)
print("문자열 %c 문자열" % 문자)
print("문자열 %s 문자열" % 문자열)
'''
# example
print("나는 %d 살입니다." % 20)
print("I like studying %s" % "python")
print("\"Apple\" starts with %c" % "A")

print("나는 %s 살입니다." % 20)  # %s로도 표현 가능

# 두개 이상의 값을 넣어야 할때는 뒤의 값들을 괄호로 감싸고 콤마로 구분
print("I like %s and %s and %s and %s so much" %
      ("blue", "red", "yellow", "black"))

# ******** .format(value1, value2,....)
# 문자열 내에 중괄호{}를 집어 넣으면 됨. 인덱스로 사용 가능
print("나는 {}살입니다." .format(20))
print("I like {} and {} color so much" .format("red", "blue"))
print("I like {0} and {1} color so much" .format("red", "blue"))
print("I like {1} and {0} color so much" .format("red", "blue"))

# *********.format(이름= value1 , 이름= value 2 , .....)
# 문자열 내에 {이름} 와 같이 넣어준다.
# 이 경우에 .format 뒤애 순서를 변경해도 괜찮다.
print("I am {age} years old, and I like {color} color" .format(
    age=20,  color="blue"))
print("I am {age} years old, and I like {color} color" .format(
    color="blue", age=20))

# ********** f-string
# 문자열 앞에 f 를 추가하면, 앞에서 선언된 변수 이름을 그대로 사용할 수 있음

age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

name = "Tony"
age = 39
print(f"His name is {name} and he is {age} years old. ")
