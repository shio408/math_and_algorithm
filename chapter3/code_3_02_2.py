def gcd(a, b):
  while a != 0 and b != 0:
    mod = max(a, b) % min(a, b)
    if max(a, b) == a:
      a = mod
    else:
      b = mod
  if b == 0:
    return a
  return b

A = list(map(int, input().split()))
result = A[0]
for i in A:
  result = gcd(result, i)
print(result)
