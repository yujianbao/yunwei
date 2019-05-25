import re
import json


s = 'abcd.ef12'
s = s.split('.')
# print(s)


#with open('aa', 'r') as f:
#    for line in f.readlines():
#        print(line)



# help(re)


# while 'a' < 0:
#     a + 5 < b - 7
#     break


import re
# reg = re.compile('\d+')
# print(reg.search('dsfee32ui').group())


# this is copyright()

# help(tuple)



# d = list(['a', 'b', 'c'])
# print(d)

# count = 0
# while d is not None:
#     d.append('d')
#     if len(d) == 3:
#         d.extend(['e', 'f'])
#     elif len(d) == 6:
#         d.pop(0)
#     if count >= 15:
#         break
#     count += 1
# print(d)
#
#
# class Man:
#     def eat(self):
#         print('eating......')
#         return 'abc'
#     def __call__(self, *args, **kwargs):
#         print('callable......')

# delattr(Man, 'eat')
# print(dir(Man))
# print([str(d) for d in dir(Man) if not d.startswith('__')])

# m = Man()
# m()
#
#
# class Entity:
#     '''调用实体来改变实体的位置。'''
#
#     # def __init__(self, size, x, y):
#     #     self.x, self.y = x, y
#     #     self.size = size
#
#     def __call__(self, x, y):
#         '''改变实体的位置'''
#         print('calling')
#         # self.x, self.y = x, y
#
# # e = Entity(1, 2, 3) # 创建实例
# e = Entity()
# e(4, 5) #实例可以象函数那样执行，并传入x y值，修改对象的x y



# def my_length_check(form, field):
#     if len(field.data) > 50:
#         raise ValidationError('Field must be less than 50 characters')
#
# class MyForm(Form):
#     name = StringField('Name', [InputRequired(), my_length_check])

# def length(min=-1, max=-1, message=None):
#     if not message:
#         message = 'Must be between %d and %d characters long.' % (min, max)
#
#     def _length(form, field):
#         l = field.data and len(field.data) or 0
#         if l < min or max != -1 and l > max:
#             raise ValidationError(message)
#
#     return _length
#
# class MyForm(Form):
#     name = StringField('Name', [InputRequired(), length(max=50)])


# class ClassA:
#
#     def __call__(self, *args, **kwargs):
#         print('call ClassA instance')
#
#
# if __name__ == '__main__':
#     # ClassA实现了__call__方法
#     a = ClassA()
#     '''
#     这个时候，ClassA的实例a，就变成可调用对象
#     调用a()，输出call ClassA instance，说明是调用了
#     __call__函数
#     '''
#     a()
#     # 其实a()等同于a.__call__()，它本质上就是后者的缩写
#     a.__call__()
#     # 判断是否可调用，输出True
#     print(callable(a))

class Singleton(type):

    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    # __call__ 是对于类实例有效，比如说Spam类，是type类的实例
    def __call__(cls, *args, **kwargs):
        print('Singleton __call__ running')
        if cls.__instance is None:
            '''
            元类定义__call__方法，可以抢在类运行 __new__ 和 __init__ 之前执行，
            也就是创建单例模式的前提，在类实例化前拦截掉。
            type的__call__实际上是调用了type的__new__和__init__
            '''
            cls.__instance = super().__call__(*args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance


class Spam(metaclass=Singleton):

    def __new__(cls):
        print('Spam __new__ running')
        return super().__new__(cls)    # 返回值才会执行init方法

    def __init__(self):
        print('Spam __init__ running')

# 单例模式
if __name__ == '__main__':
    a = Spam()
    b = Spam()
    print(a is b)
    c = Spam()
    print(a is c)


