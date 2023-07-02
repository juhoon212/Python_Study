#자료구조 변경

from random import *

menu = {"커피", "우유", "주스"};

print(menu, type(menu));

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

first = [1,2,3,4,5]

#print(first)

shuffle(first)
print(first)

users = range(1, 21) # 1부터 21까지

#print(type(users)) range 타입이므로 list로 변환

users = list(users);

shuffle(users)

winners = sample(users, 4);

print("-- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))







