# Quick sort in Python
import random
import sys
import time
import matplotlib.pyplot as plt

sys.setrecursionlimit(10000)

def randList(seed, n):
  random.seed(seed)
  return [random.randint(0,1000000000) for x in range(n)]

def worst_case_gen(n):
  best_case = []
  for i in range(1,n+1):
    best_case.append(i)
  return best_case


# function to find the partition position
def partition_r(array, low, high):

  # choose the rightmost element as pivot
  pivot = (array[random.randint(low,high-1)] + array[random.randint(low,high-1)] + array[random.randint(low,high-1)])/3

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high+1):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  #(array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i

# function to perform quicksort
def quickSort_r(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition_r(array, low, high)

    # recursive call on the left of pivot
    quickSort_r(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort_r(array, pi + 1, high)



def partition_w(array, low, high):

  pivot = array[high]


  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high+1):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  #(array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i

# function to perform quicksort
def quickSort_w(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition_w(array, low, high)

    # recursive call on the left of pivot
    quickSort_w(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort_w(array, pi + 1, high)

#random
times_ran = []
num_r = []

for i in range (100000,1000001,100000):

  num_r.append(i)

  data = randList(1401,i)
  size = len(data)
  start_time=time.time()
  quickSort_r(data, 0, size - 1)
  t = time.time() - start_time
  print("---Random %s seconds ---" % (t))

  times_ran.append(t)

#worst
times_worst= []
num_w=[]

for i in range (1000,10001,1000):

  num_w.append(i)

  data = worst_case_gen(i)
  size = len(data)
  start_time=time.time()
  quickSort_w(data, 0, size - 1)
  t = time.time() - start_time
  print("---worst %s seconds ---" % (t))
  
plt.plot(num_r, times_ran, marker='o', linestyle='-')
    
# Add labels and a title
plt.xlabel('n-size of input')
plt.ylabel('time taken(in seconds)')
plt.title('Running time for random-case scenario of Insertion Sort')
    
# Show the
plt.show()
