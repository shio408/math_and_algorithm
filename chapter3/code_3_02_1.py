A, B = map(int, input().split())

while A != 0 and B != 0:
  mod = max(A, B) % min(A, B)
  if max(A, B) == A:
    A = mod
  else:
    B = mod
if A == 0:
  print(B)
if B == 0:
  print(A)
