python = "Python is Amazing"
print(python.lower())
print(python.isupper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n")) # find는 원하는 값이 없을 때 -1 을 반환
# print(python.index("Java")) # index는 원하는 값이 없을 때 error 발생

print(python.count("n"))