def map_task():
    print(list(map(int,['12', '-2', '0'])))
    print(list(map(len,['hello', 'world'])))
    print(list(map(lambda word: word[::-1],['hello', 'world']))) # od końca słowa
    print(list(map(lambda r: (r, r * 2, r * 3),range(2, 6))))
    print(list(map(lambda l: l[0]*l[1] ,zip(range(2, 5), range(3, 9, 2)))))

map_task()