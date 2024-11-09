import random

def randList(seed, n):
  random.seed(seed)
  return [random.randint(0,1000000000) for x in range(n)]

n = 100
print(randList(1401,n))

