# 装饰器实现计算时间的函数
import time

def timer(func):
    def wrapper():
        start = time.clock()
        func()
        print(time.clock()-start)
    return wrapper

@timer
def test():
    time.sleep(1)

if __name__ == '__main__':
    test()
