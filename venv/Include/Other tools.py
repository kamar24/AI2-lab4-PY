import operator
from functools import reduce

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(*args):
    return reduce(lambda x, y: x * y / gcd(x, y), args)

#GCD=NWD
#LCM=NWW
def fact(n):
    return reduce(operator.mul, range(1,n+1)) #silnia

print(lcm(3,5))
print(operator.add(1, 2)) #DODAWANIE
print(operator.mul(3, 10)) #MNOŻENIE
print(operator.pow(2, 3) ) #PIERWIASTEK
print(operator.itemgetter(1)([1, 2, 3])) #Zwraca element tablicy


print(fact(3))  # => 6
print(fact(7))  # => 5040

def alpha_score(upper_letters):
    """Computers the alphanumeric sum of letters in a string.
    Prerequisite: upper_letters is composed entirely of capital letters.
    """
    return sum(map(lambda l: 1 + ord(l) - ord('A'), upper_letters))

print(alpha_score('ABC'))  # => 6 = 1 ('A') + 2 ('B') + 3 ('C')

def two_best(words):
    words.sort(key=lambda word: alpha_score(filter(str.isupper, word)), reverse=True)
    return words[:2]

print(two_best(['hEllO', 'wOrLD', 'i', 'aM', 'PyThOn']))