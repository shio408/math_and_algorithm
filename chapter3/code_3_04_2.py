N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
answer = 0
for i in range(N):
  answer += Q[i] / P[i]
print(int(answer))
