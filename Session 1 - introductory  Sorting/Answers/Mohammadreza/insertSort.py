# Insertion sort in Python
import pickle
import time


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


# here we import the data we have saved before
saved_data = []
with open("my_list.pkl", "rb") as f:
  saved_data = pickle.load(f)

# here we start the time
start = time.process_time()

insertionSort(saved_data)

# and here we stop our time
end = time.process_time()

print(f'Process time: {end - start}')
