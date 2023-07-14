# == 과 is 의 차이
# == : 값 비교 , is : 주소값 비교

a = [1,2,3,]
b = a
c = [1,2,3,]

print(a == b) # True
print(a == c) # True  
print(a is c) # False 주소값이 다르다.