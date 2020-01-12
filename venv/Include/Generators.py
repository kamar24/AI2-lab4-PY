def generate_triangles():
    x = 0
    y = 0
    while True:
        x += y
        y += 1
        yield x


def triangles_under(x):
    for triangle in generate_triangles():
        if triangle >= x:
            break
        print(triangle)

triangles_under(20)