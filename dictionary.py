# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# # print(cabinet[5]) 그냥 조회 시 없으면 error 발생!

# print(cabinet.get(5)) # get을 통해 조회해서 없으면 None 반환

# print(3 in cabinet) # True
# print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국" #update 
cabinet["C-20"] = "조세호" #add
print(cabinet)

#간 손님
del cabinet["A-3"] #delete
print(cabinet)

# key 들만 출력
print(cabinet.keys())

#value 들만 출력
print(cabinet.values())

#key,value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)

