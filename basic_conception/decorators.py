# -*- coding:UTF-8 -*-

'''
装饰器基本用法
'''
from functools import wraps
import time
def runtime(func):
    @wraps(func)
    def wrapper():
        start = time.time()
        f = func()     # 原函数
        end = time.time()
        print("运行时长：%.4f 秒" % (end-start))
        return f
    return wrapper
    
@runtime
def func_a():
    print("hello")
    time.sleep(0.5)

@runtime
def func_b():
    print("world")
    time.sleep(0.8)
    


def a_decorator(f):
    def additional_function(*args):
        print("No. of input args is", len(args))
        contain_zero = any([x == 0 for x in args])
        print("Input arguments contain 0:", contain_zero)
        f(*args)
    return additional_function

@a_decorator
def my_sum_function(*args):
    print("The sum is", sum(args))

@a_decorator
def my_product_function(*args):
    res = 1
    for x in args:
        res *= x
    print("The product is", res)


if __name__ == '__main__':
    # func_a()
    # func_b()
    print(func_a.__name__)
    print(func_a.__dir__)
    my_sum_function(1, 2, 3, 4)
    my_product_function(0, 1, 2, 3, 4, 5)