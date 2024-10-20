import random
import pickle

def randList(seed, n):
  random.seed(seed)
  return [random.randint(0,10000000) for x in range(n)]


# here we save it to .pkl file using pickle library
def saveToFile(filename, list):
  with open(filename, 'wb') as file:
    pickle.dump(list, file)


n = 6000000
# print(randList(1401,n))
for i in range(5):
    arr = randList(1401, n)
    # here we save the rand case
    saveToFile("my_list_rand_" + str(i) + ".pkl", arr)
# merge_sort(arr, 0, len(arr) - 1)
# # here we save the best case
# saveToFile("my_list_best.pkl", arr)
# arr.reverse()
# # here we save the worst case
# saveToFile("my_list_worst.pkl", arr)
