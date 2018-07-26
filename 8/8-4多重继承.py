#https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318680104044a55f4a9dbf8452caf71e8dc68b75a18000
#正确的做法是采用多重继承。首先，主要的类层次仍按照哺乳类和鸟类设计：
class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

#现在，我们要给动物再加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类：
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

# 各种动物:
class Dog(Mammal,Runnable):
    pass

class Bat(Mammal,Flyable):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass


#这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类