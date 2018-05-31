import random

classmates = ['hello','world','me']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[-1])
classmates.insert(1,'fucking')
print(classmates)
classmates.append('plz')
print(classmates)

text1 = [111,222,333] #可变数组
text2 = (111,222,333) #元组  不可变

t = ('a', 'b', ['A','B'])
t[2][0] = 'x'
t[2][1] = 'y'
print(t)

print(random.randint(1,2))
