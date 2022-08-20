N, X, Y = map(int, input().split())
print(int(N / X) + int(N / Y) - int(N / (X * Y)))
