# 5-5 자료구조의 변경

# type() --> 자료형 확인 하는 and

# int()
# str()
# list()
# tuple()
# set()

menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

variable = 123445
print(variable, type(variable))

variable = str(variable)
print(variable, type(variable))
