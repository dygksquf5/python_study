def func(n):
  print(n)
  if n == 1:
    return n
  if n % 2 == 0:
    return func(n//2)
  elif n % 2 ==1:
    return func(3*n+1)


func(3)