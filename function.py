def open_account():
    print("새로운 계좌가 생성되었습니다")

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다."
          .format(balance + money))
    
    return balance + money

def withdraw(balance, money): #출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다."
              .format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다."
              .format(balance))
        return balance

balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다."
      .format(commission, balance))

# def profile(name,age, main_lang):
#     print("이름 : {0} \t 나이: {1}\t주 사용 언어: {2}".format(name,age,main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 수업
# 함수 기본 값 작성

# def profile(name, age=17, main_lang="파이썬"):
#      print("이름 : {0} \t 나이: {1}\t주 사용 언어: {2}".format(name,age,main_lang))

# profile("유재석")

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name = "유재석",main_lang = "파이썬", age = 20) 
# profile(main_lang="자바", age=25, name="김태호")

#가변인자

def profile(name, age, *language): # *문법은 가변인자로 유연하게 매개변수를 받을 수 있다. 
    print("이름 : {0}\t 나이: {1}\t".format(name,age) ,end="")
    for lang in language: # => lang은 변수다.
        print(lang, end=" ")
    print() # => 줄바꿈
    
profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin","Swift", "", "", "")



