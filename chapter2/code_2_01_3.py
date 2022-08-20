from functools import reduce

A = list(map(int, input().split()))
print(reduce(lambda x, y: x + y, A))
