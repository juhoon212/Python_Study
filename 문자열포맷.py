print("나는 %d살 입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")

print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란 ", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

print("나는 {age}살 이며, {color}색을 좋아해요".format(age = 20, color = "빨간"))

age = 20
color = "빨간"
print(f"나는 {age}살이며 , {color}색을 좋아해요")

address = "http://naver.com"

my_str = address.replace("http://", "")
# 
my_str = my_str[:my_str.index(".")]
# print(my_str)

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1}입니다.".format(address, password))

