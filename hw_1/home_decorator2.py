import functools
from collections import OrderedDict
import requests as requests

# декоратор на основе контрольного словаря без изменения функциональности
def cache(max_limit=64):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, count=1, **kwargs):
            cache_key = (args, tuple(kwargs.items()))
            # обрабатываем элемент присутствующий в словаре
            if cache_key in deco._cache:
                # увеличиваем счетчик обращений к url в контрольном словаре
                counted[cache_key] += 1
                return deco._cache[cache_key]
            # обрабатываем новый элемент
            result = f(*args, **kwargs)
            # вносим счетчик в контрольній словарь
            counted[cache_key] = count
            # видаляємо якшо досягли ліміта
            if len(deco._cache) >= max_limit:
                # ищем непопулярній елемент в контрольном словаре
                spis = sorted(counted.items(), key=lambda x: x[1])
                key_del = spis[0][0]
                # видаляємо непопулярній елемент и контрольный элемент
                counted.pop(key_del)
                deco._cache.pop(key_del)
            # вносим новый єлемент в словарь
            deco._cache[cache_key] = result
            return result
        deco._cache = OrderedDict()
        counted = dict()
        return deco
    return internal

@cache(max_limit=5)
def fetch_url(url, first_n=10):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content

# контрольніе url
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
