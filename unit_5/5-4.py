# 세트 (집합)
# 중복을 허용하지 않으며 데이터 순서도 보장하지 않는다.
# 중괄호를 써서 선언할 수 있다.
# 같은 값을 여러번 적어도 한번만 들어감

my_set = {1, 2, 3, 3, 3}
print(my_set)

# set([리스트])
java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# &, set_name.intersection(set_name) --> 교집합
print(java & python)
print(java.intersection(python))

# |, set_name.union(set_name) --> 합 집합
print(java | python)
print(java.union(python))
# 집합은 순서를 보장하지 않으므오 집합 내 데이터들의 출력 순서는 실행 할때마다 다를 수 있다.

# -, set_name.difference(set_name)
print(java-python)
print(java.difference(python))

# set_name.add(value) --> set_name 집합에 value 더하기
python.add("김태호")
print(python)

# set_name.remove(value) --> set_name 에서 value 빼기
java.remove("김태호")
print(java)
