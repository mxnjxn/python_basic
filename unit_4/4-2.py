# 슬라이싱
# 슬라이싱을 통해 데이터를 원하는 만큼 잘라서 가져올 수 있다.

# index(인덱스) --> 0부터 카운트
words = "Hello, my name is Tony"
print(words[0])
print(words[4])

# 슬라이싱: 변수명[시작인덱스:종료인덱스] --> 종료 인덱스 전까지
# [3:7] --> 3 부터 6까지 인덱스
words = "Hello, my name is Tony"

print(words[0:5])
print(words[7:9])
print(words[10:14])
print(words[15:17])
print(words[18:])

# 변수명 [:인덱스] --> 처음부터 슬라이스 바로 직전까지
# 변수명 [:] --> 처음부터 끝까지
# 변수명 [인덱스:] --> 인덱스 부터 끝까지

# 맨 뒤 인덱스는 -1 부터 시작
words = "Hello, my name is Tony"
print(words[-1])
print(words[15:-1])  # is Ton
print(words[15:])  # is Tony
