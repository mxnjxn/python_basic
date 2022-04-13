# 2-4변수 --> 쉽게 말하면 어떤 값을 저장하는 공간, 데이터를 저장할 수 있는 메모리 공간에 붙여진 이름.
# Introduce your dog
print("my dog name is Einstein")
print("the dog is a male, and he is 6years old. He also likes to walk")
# 변수를 선언하면 바꿀때 편함
print("And here comes a question. Is my dog,Einstein, an adult?, True")

animal = "cat"  # 문자열 ""
name = "Tony"
age = 2
hobby = "Sleeping"
is_adult = age >= 3
print("my " + animal + " name is " + name)  # "" 사이에 들어가는 띄어쓰기는 그대로 구현됨..
# 정수형의 변수인 경우는 +문을 포함한 프린트문내에(출력) 쓰이기 위해서는 "str"(문자열 자료형을 뜻함)로 앞 뒤를 감싸줘야한다 --> 정수형을 문자형으로 바꿔주는 역활(형 변환)
print("the " + animal + " is a male, and he is " +
      str(age) + "years old. He also likes "+hobby)
print("And here comes a question. Is my " + animal + "," + name +
      ", an adult?, " + str(is_adult))  # 변수가 맨 끝이나 앞에 올때는 "+, +" 생략

# 변수를 중간에 선언할 수 도 있다. 하지만 맨 앞에 선언하는게 제일 좋음 (변수의 가장 마지막에 저장된 값을 사용)

# +변수+ 형태로 변수를 사용했는데 쉼표,를 이용해도 할 수 있음
# 1. str와 같은 형변환을 사용하지 않아도 된다. 2. + 대신 ,를 사용하면 값과 값 사이에 공백이 하나 포함된다. 3. "(변수)"는 그대로 사용
print("my", animal, "name is", name)
print("the", animal, "is a male, and he is",
      age, "years old. He also likes", hobby)
print("And here comes a question. Is my",
      animal, ",", name, ",an adult?,", is_adult)
