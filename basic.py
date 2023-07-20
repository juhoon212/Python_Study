from random import *

# sentence = "나는 소년입니다";
# print(sentence);

# sentence2 = "파이썬은 쉬워요";

# print(sentence2);
# sentence3 = """
# 나는 소년이고, 
# 파이썬은 쉬워요
# """
# print(sentence3);

# 문자열
s1 = "I Love Python";

print(s1[0].isupper());

print(int(random() * 45) + 1);

index= s1.index("e");

print(index);

index = s1.index("t", index+1);
#index와 find()의 차이점 => index를 사용하여 없는 문자열을 찾을 시 ValueError(Excepiton)발생
print(s1.find("e")); 

#문자열 자르기

item1 = "apple"

print(item1[:3]) #app




age = 20
color = "빨강"

print(f"나는 {age}살이며, {color}색을 좋아해요");


# List(stack)
subway = ["유재석", "노홍철", "하하", "정형돈"]

subway.pop();
print(subway)


subway.append("전진");

print(subway);

train = ["길", "박명수"];

subway.extend(train);

print(subway);


#Dictionary(key, value)
cabinet = {"A-3":"유재석", "B-100":"김태호"};
cabinet["C-20"] = "조세호";
print(cabinet)
del cabinet["A-3"]
print(cabinet);

#key
print(cabinet.keys())

#value
print(cabinet.values())

#key, value 쌍
print(cabinet.items())

cabinet.clear()
print(cabinet)

#Tuple(데이터 변경 불가능)

menu = ("돈까스", "치즈까스");
print(menu[0])

# menu.add("생선까스")

(name, age, hobby) = ("김종국", 20, "코딩")

print(name, age, hobby)

# Set
# 중복 x. 순서 x
my_set = {1,2,3,3,3}
print(my_set);

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합
print(java & python);
print(java.intersection(python))

#합집합(Java 할 수 있거나 python 할 수 있는 개발자)
print(java | python);
print(java.union(python));

#차집합(Java 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python);
print(java.difference(python));

# python 할줄 아는 사람이 늘어남
python.add("김태호");
print(python); 

#Java 를 잊었어요
java.remove("김태호");
print(java);




