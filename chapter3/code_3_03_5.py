N = int(input())
A = list(map(int, input().split()))
answer = 0
for i in range(1, 50000):
  cnt_i = A.count(i)
  cnt_100000_i = A.count(100000 - i)
  answer += cnt_i * cnt_100000_i
answer += A.count(50000)
print(answer)
