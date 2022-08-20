N = int(input())
B = list(map(int, input().split()))
R = list(map(int, input().split()))
print(int((sum(B) + sum(R)) / N))
