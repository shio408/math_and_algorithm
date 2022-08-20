N = int(input())

Answer = []
Limit = int(N ** 0.5)
for i in range(2, Limit + 1):
  while N % i == 0:
    N /= i
    Answer.append(i)
if N > 1:
  Answer.append(int(N))

print(*Answer)
