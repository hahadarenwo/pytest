#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name,self.__score))

#但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
#如果又要允许外部代码修改score怎么办？可以再给Student类增加set_score方法：c
#你也许会问，原先那种直接通过bart.score = 99
#也可以修改啊，为什么要定义一个方法大费周折？因为在方法中，可以对参数做检查，避免传入无效的参数：
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

bart = Student('Hello', 59)
# print(bart.__name)

#练习
#请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        self.__gender = gender

bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')