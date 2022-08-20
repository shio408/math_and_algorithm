A = list(range(10, 1001, 10))
N = len(A)
answer = 0
for i in range(N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      for l in range(k+1, N):
        for m in range(l+1, N):
          if (A[i] + A[j] + A[k] + A[l] + A[m] == 1000):
            answer += 1
print(answer)
