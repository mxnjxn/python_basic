# 탈출 문자 aka. back slash (\)

print("백문이 불여일견 백견이 불여일타")
print("백문이 불여일견 \n 백견이 불여일타")


# \\ --> \가 출력됨.
print("C:\\Users\\Nadocoding\\Desktop\\PythonWorkspace>")

# 문자열을 그대로 출력하고 싶을때는 문자열 앞에 r(raw)를 넣는다.
print(r"C:\Users\Nadocoding\Desktop\PythonWorkspace>")


# \r --> 커서를 맨 앞으로 이동해라 --> 앞에서 부터 덮어쓰기
print("Red Apple \rPine")

# \b --> 키보드 백스페이스 역활--> 앞 글자 삭제
print("Redd\bApple")
# \t --> tab --> 4칸 띄어쓰기
print("Red\tApple")
