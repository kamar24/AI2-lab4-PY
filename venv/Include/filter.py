def filter_task():
    print(list(filter(lambda n : int(n) >= 0,['12', '-2', '0'])))
    print(list(filter(lambda n : n == 'world',['hello', 'world']))) #jak mapa, tylko
    print(list(filter(lambda n : n == 'Stanford',['Stanford', 'Cal', 'UCLA'])))
    print(list(filter(lambda n : n%3 == 0 or n%5 == 0,range(20))))
filter_task()