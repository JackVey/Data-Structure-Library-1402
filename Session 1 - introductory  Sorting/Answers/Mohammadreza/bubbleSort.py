# Bubble sort in Python
import pickle
import time


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

# here we import the data we have saved before
saved_data = []
with open("my_list.pkl", "rb") as f:
  saved_data = pickle.load(f)

# here we start the time
start = time.process_time()

bubbleSort(saved_data)

# and here we stop our time
end = time.process_time()

print(f'Process time: {end - start}')
