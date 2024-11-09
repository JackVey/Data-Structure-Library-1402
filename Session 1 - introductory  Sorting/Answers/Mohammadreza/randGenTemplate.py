import random
import pickle

def randList(seed, n):
  random.seed(seed)
  return [random.randint(0,100000) for x in range(n)]

n = 25000
# print(randList(1401,n))
# here we save it to .pkl file using pickle library
with open('my_list.pkl', 'wb') as file:
  pickle.dump(randList(1401, n), file)

