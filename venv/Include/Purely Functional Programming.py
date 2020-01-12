def replacing_Control_Flow(score = None):
    return (score == 1 and "Winner") or (score == -1 and "Loser") or "Tied"
print(replacing_Control_Flow())
print(replacing_Control_Flow(1))
print(replacing_Control_Flow(-1))
print()

def dot_product(u, v):
    return sum(list(map(lambda x: x[0] * x[1],zip(u,v))))

print(dot_product([1, 3, 5], [2, 4, 6]))
print()
def transpose(m):
    return tuple(zip(*m))


matrix = (
    (1, 2, 3, 4),
    (5, 6, 7, 8),
    (9,10,11,12)
)
print(transpose(matrix))


def matmul(m1, m2):
    return tuple(map(lambda row: tuple(dot_product(row, col) for col in transpose(m2)), m1))

matrix1 = (
    (1, 2, 3, 4),
    (5, 6, 7, 8),
    (9,10,11,12)
)

print(matmul(matrix,matrix1))