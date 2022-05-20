# 문자열 처리함수

# function
# 변수명.lower() --> 소문자로 변환
# 변수명.upper() --> 대문자로 변환
# ***변수명[0].isupper() --> 대문자인지 확인
# ***변수명[0].islower() --> 소문자인지 확인
# 변수명.replace --> 문자역 바꾸기
# 변수명.index --> 찾으려는 문자열의 인덱스 (없으면 에러)
# 변수명.find --> 찾으려는 문자열의 인덱스 (없으면 -1)
# 변수명.count --> 문자열이 나온 횟수
python = "Python is Amazing"

print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))
print(python.replace("Amazing", "Sucks"))


index = python.index("n")  # 처음으로 발견된 n의 인덱스
print(index)
# 6번째 인덱스 이후에 처음으로 발견된 n의 인덱스
index = python.index("n", index+1)
print(index)

find = python.find("n")  # 처음으로 발견된 n의 인덱스
print(find)
# 6번째 인덱스 이후에 처음으로 발견된 n의 인덱스
find = python.find("n", find+1)
print(find)

# *******python.index 와 python.find의 차이 ********************
# 찾으려는 문자열이 없는 경우
# python.index() 사용시 에러 --> 이 후의 문장은 실행되지 않고 종료 됨
# python.find() 사용시 에러 --> -1을 반환

print(python.find("Java"))
print(python.find("is"))  # 단어를 입력할 시에는 제일 첫 번째 index 값이 출력 됨.

# print(python.index("Java"))
print(python.count("n"))  # 문자열 내에서 n이 나온 횟수

# ************************************************************************************************
name = "Hello, my name is Tony"
print(name.lower())
print(name.upper())
print(name.replace("Tony", "Dennis"))
print(name[0].isupper())
print(name[1].isupper())
print(name[0].islower())
print(name[1].islower())
print(len(name))
print(name.count("n"))

find = name.find("m")
print(find)

index = name.index("m")
print(index)

find = name.find("m", find+1)
print(find)

index = name.index("m", index+1)
print(index)
