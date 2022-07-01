import functools
import sys

# декоратор для измерения использования памяти:
# 1. sys.getsizeof(),
# 2. get_size (рекурсивная),
# 3. @profile from memory_profiler. (закомменченно)

# 3) декоратор memory_profiler, выводит таблицу используемой памяти декоратором test_mem(f): (для использования раскомментить)
#@profile
def test_mem(f):
    @functools.wraps(f)
    def deco(*args, **kwargs):
        result = f(*args, **kwargs)
        # измерение и вывод используемой памяти при помощи системной функции sys.getsizeof()
        mem_getsize = sys.getsizeof(f)
        print(f'1) Working sys.getsizeof() in decorator. Usage memory:', mem_getsize)
        # рекурсивная get_size функция измерение в используемой памяти c GitHub
        def get_size(obj, seen=None):
            # From https://goshippo.com/blog/measure-real-size-any-python-object/
            # Recursively finds size of objects
            size = sys.getsizeof(obj)
            if seen is None:
                seen = set()
            obj_id = id(obj)
            if obj_id in seen:
                return 0
            # Important mark as seen *before* entering recursion to gracefully handle
            # self-referential objects
            seen.add(obj_id)
            if isinstance(obj, dict):
                size += sum([get_size(v, seen) for v in obj.values()])
                size += sum([get_size(k, seen) for k in obj.keys()])
            elif hasattr(obj, '__dict__'):
                size += get_size(obj.__dict__, seen)
            elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
                size += sum([get_size(i, seen) for i in obj])
            return size
        print('2) Working recursion function from GitHub in decorator. Usage memory:', get_size(f))
        return result
    return deco

# декоратор функции memory_test():
@test_mem
# 3) декоратор memory_profiler, выводит таблицу используемой памяти функцией memory_test(): (для использования раскомментить)
#@profile
def memory_test():
    test_list = [i**2 for i in range(100)]
    return test_list

memory_test()
#print(f'Print returned arguments from ({memory_test.__name__}): {memory_test()} \n')