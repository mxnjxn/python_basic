# quiz
Naver = "http://naver.com"

first_slash_index = Naver.find("/")
second_slash_index = Naver.find("/", first_slash_index + 1)  # +1 까먹지 않기.
period_index = Naver.find(".")

character = Naver[second_slash_index+1: period_index]
three_character = Naver[second_slash_index+1:second_slash_index+4]
number_character = len(Naver[second_slash_index+1:period_index])
number_e = character.count("e")
password = three_character + \
    str(number_character) + str(number_e) + "!"

# 다양한 포맷
print("생성된 비밀번호: %s" % password)

print("생성된 비밀번호: %s%s%s%s" %
      (three_character, number_character, number_e, "!"))

print(f"생성된 비밀번호는 {three_character}{number_character}{number_e}!")

print("생성된 비밀번호: {}{}{}{}" .format(
    three_character, number_character, number_e, "!"))

# ************************************************************************

Daum = "http://daum.net"
D_first_slash_index = Daum.find("/")
D_sec_slash_index = Daum.find("/", D_first_slash_index+1)
D_period_index = Daum.find(".")

D_character = Daum[D_sec_slash_index+1:D_period_index]
D_three_character = Daum[second_slash_index+1: second_slash_index+4]
D_character_len = len(D_character)
# Daum.count("e") --> daum.net 에서 net 의 e 도 count 함
D_number_e = D_character.count("e")

password = D_three_character + str(len(D_character)) + str(D_number_e) + "!"

print("생성된 비밀번호는: %s" % password)

# *****************************************************************
# 복습 --> 더 간단한 방법으로 해보기
# 5줄로 끝내기
google = "http://google.com"

character = google.replace("http://", "")
character = character[0:character.index(".")]
# character = character[0:6] --> 주소가 다를 때에는 성립 x --> 일반화 시켜보자.

print("생성된 비밀번호는: {}{}{}{}" .format(
    character[0:3], len(character), character.count("e"), "!"))


youtube = "http://youtube.com"

character = youtube.replace("http://", "")
character = character[:-4]  # index 이용하기
character = character[:youtube.index(".")]
print("dfaf %s" % character)

print("생성된 비밀번호는 {}{}{}{}" .format(
    character[0:3], len(character), character.count("e"), "!"))
