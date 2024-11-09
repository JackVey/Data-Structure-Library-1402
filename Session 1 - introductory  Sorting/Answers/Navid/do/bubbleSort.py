# Bubble sort in Python
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


def bubbleSort(array):
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

times_ran = []
times_best = []

for i in range(1000 , 10001 , 1000):
  data = randList(1401,i)

  start_time=time.time()
  bubbleSort(data)
  t = time.time() - start_time
  print("---Random %s seconds ---" % (t))

  times_ran.append(t)

  data = best_case_gen(i)
  start_time=time.time()
  bubbleSort(data)
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
