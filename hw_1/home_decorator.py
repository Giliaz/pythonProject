import functools
from collections import OrderedDict
import requests as requests

# декоратор на основе дополнительного параметра в **kwargs
def cache(max_limit=64):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))
            # обрабатываем элемент присутствующий в словаре
            if cache_key in deco._cache:
                # увеличиваем счетчик обращений к url в словаре (аргумент **kwargs)
                value_count = list(deco._cache[cache_key])
                value_count[1] += 1
                deco._cache[cache_key] = tuple(value_count)
                return deco._cache[cache_key]
            # обрабатываем новый элемент словаря
            result = f(*args, **kwargs)
            # видаляємо якшо досягли ліміта
            if len(deco._cache) >= max_limit:
                #сортируем словарь по значению счетчика (аргумент **kwargs)
                deco._cache = OrderedDict(sorted(deco._cache.items(), key=lambda x: x[1][1]))
                # видаляємо перший(непопулярній) елемент
                deco._cache.popitem(last=False)
            # вносим новый єлемент в словарь
            deco._cache[cache_key] = result
            return result
        deco._cache = OrderedDict()
        return deco
    return internal

count = 1
@cache(max_limit=5)
def fetch_url(url, first_n=10):
    """Fetch a given url"""
    res = requests.get(url)
    print('adfsdfsdf')
    return (res.content[:first_n], count) if first_n else  (res.content, count)

# контрольніе url
if __name__ == '__main__':
    fetch_url('https://ithillel.ua')
    fetch_url('https://ithillel.ua')
    fetch_url('https://google.com')
    fetch_url('https://ithillel.ua')
    fetch_url('https://dou.ua')
    fetch_url('https://ain.ua')
    fetch_url('https://google.com')
    fetch_url('https://google.com')
    fetch_url('https://dou.ua')
    fetch_url('https://ain.ua')
    fetch_url('https://youtube.com')
    fetch_url('https://dou.ua')
    fetch_url('https://stepic.org')