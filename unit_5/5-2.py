# Dictionary {Key1: Value1, Key2: Value2} --> 중 괄호 통해 // 리스트는 [] --> 대괄호를 사용
# key --> 중복을 허용하지 않는 유일한 값.
# value --> 중복할 수 있음

cabinet = {3: "유재석", 100: "김태호"}
cabinet2 = {"A-3": "유재석", "B-100": "김태호"}

# Dictionary[key] --> value 값이 나옴. ---> 대괄호 안에 값 확인
print(cabinet[3])
print(cabinet[100])
print(cabinet2["A-3"])
print(cabinet2["B-100"])

# get(key ,default value) --> 기본 값을 지정할 수 있음.
print(cabinet.get(3))
print(cabinet.get(100))
print(cabinet2.get("A-3"))
print(cabinet2.get("B-100"))

# ***********get() 과 [key]의 차이
# [key]를 사용할 때는 value 값이 지정되어 있지 않는 key 값을 사용할 경우 에러가 나면서 프로그램이 종료됨 -->뒤에 있는 코드가 실행되지 않움
# get()을 사용할 때는 value 값이 지정되어 있지 않는 key 값을 사용하게 되면 에러가 발생하지 않고 "none 반환" --> 프로그램 계속 실행

print(cabinet.get(5))
print("hi")

# print(cabinet[5])
# print("hi")


# *********** get(key, default value) --> 기본 값을 지정할 수 있음 --> key에 해당하는 value 가 없을 때 default value가 나온다.
print(cabinet.get(5, "사용가능"))


# *********** in --> key 값에 value가 있는지 없는지 확인할 수 있음
print(3 in cabinet)
print(5 in cabinet)
print(100 in cabinet)


# key의 value 값을 업데이트 또는 추가
print(cabinet2)
cabinet2["A-3"] = "김종국"
cabinet2["C-20"] = "조세호"
print(cabinet2)

# del dictionary[key] --> key, value 삭제
del cabinet2["A-3"]  # key A-3에 해당하는 데이터 삭제
print(cabinet2)

# dictionary.keys() --> key 값을 모두 확인 할 수 있음.
print(cabinet2.keys())

# dictionary.values() --> value 값을 모두 확인 할 수 있음
print(cabinet2.values())

# dictionary.items() --> key 와 value를 동시에 확인
print(cabinet2.items())

# dictionary.clear() --> 전체 삭제
cabinet2.clear()
print(cabinet2)
