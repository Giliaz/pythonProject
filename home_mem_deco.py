import functools
import sys
import psutil
from memory_profiler import profile
from memory_profiler import memory_usage

# декоратор для измерения использования памяти:
# 1. sys.getsizeof(),
# 2. memory_usage() from memory_profiler,
# 3. psutil memory_info(),
# 4. @profile from memory_profiler. (закомменченно)

# 4) декоратор memory_profiler, выводит таблицу используемой памяти декоратором test_mem(f): (для использования раскомментить)
#@profile
def test_mem(f):
    @functools.wraps(f)
    def deco(*args, **kwargs):
        result = f(*args, **kwargs)
        # измерение и вывод используемой памяти при помощи системной функции sys.getsizeof()
        mem_getsize = sys.getsizeof(result)
        print(f'1) Working sys.getsizeof() in decorator. Usage memory:', mem_getsize)
        # измерение и вывод используемой памяти при  функции memory_usage() библиотеки memory_profiler
        mem_usage = memory_usage()
        print('2) Working memory_usage in decorator. Usage memory:', *mem_usage)
        # измерение в используемой памяти при помощи  функции библиотеки psutil memory_info()
        mem_psutil = psutil.Process().memory_info()
        print('3) Working psutil memory_info() in decorator. Usage memory:', mem_psutil, '\n')
        return result
    return deco

# декоратор функции memory_test():
@test_mem
# 4) декоратор memory_profiler, выводит таблицу используемой памяти функцией memory_test(): (для использования раскомментить)
#@profile
def memory_test():
    test_list = [i**2 for i in range(100)]
    return test_list

memory_test()
#print(f'Print returned arguments from ({memory_test.__name__}): {memory_test()} \n')