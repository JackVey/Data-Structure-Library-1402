# Insertion sort in Python
#navid ebadi 401222093
import random
import time
import matplotlib.pyplot as plt

def randList(seed, n):
  random.seed(seed)
  return [random.randint(0,1000000000) for x in range(n)]

def best_case_gen(n):
  best_case = []
  for i in range(1,n+1):
    best_case.append(i)
  return best_case

def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key

times_ran = []
times_best = []

for i in range(1000 , 10001 , 1000):
  data = randList(1401,i)

  start_time=time.time()
  insertionSort(data)
  t = time.time() - start_time
  print("---Random %s seconds ---" % (t))

  times_ran.append(t)

  data = best_case_gen(i)
  start_time=time.time()
  insertionSort(data)
  t = time.time() - start_time
  print("---Best %s seconds ---" % (t))

  times_best.append(t)

x=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]

fig, ax = plt.subplots()
ax.plot( x ,times_best , label='best')
ax.plot(x ,times_ran, label='random')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Multiple Lines in One Plot')
ax.legend()

plt.show()


