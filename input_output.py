# 표준 입출력
import sys

# print("Python", "Java", sep=" vs ") 문자열 중간에 삽입 가능
# print("무엇이 더 재미있을까요?")

# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# scores = {"수학":0, "영어":50, "코딩":100}

# print(type(scores))

# for subject, score in scores.items():
#     #print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

scores2 = {"국어": 80, "과학" : 70, "사회" : 50}

for subject, score in scores2.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    

# 은행 대기순번표
# 001, 002, 003

for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3))
 
    

    
