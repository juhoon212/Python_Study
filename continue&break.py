from random import *

absent = [2,5] #결석
no_book = [7] # 책을 깜빡했음
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
      print("오늘 수업은 여기까지, {0}는 교무실로 따라와".format(student))
      break
    print("{0}, 책을 읽어봐".format(student))

students = [1,2,3,4,5]
print(students)
students = [i + 100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

#학생 이름을 대문자로 변환

students = ["iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

count = 0

for i in range(1, 51):
    time = randrange(5,51) #5분 ~ 50분 소요 시간
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1})".format(i, time))
        count += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1})".format(i, time))

print("총 승객 인원 수 {0}명".format(count))

      


