N = int(input())
for i in range(2, N + 1):
  cnt = 0
  for j in range(2, N + 1):
    if i % j == 0:
      cnt += 1
  if cnt == 1:
    print(i)
