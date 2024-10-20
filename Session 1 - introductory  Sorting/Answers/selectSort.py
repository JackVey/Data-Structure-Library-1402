# Selection sort in Python
import pickle
import time


def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])



# here we import the data we have saved before
saved_data = []

with open("my_list.pkl", "rb") as f:
  saved_data = pickle.load(f)

size = len(saved_data)
# here we start the time
start = time.process_time()

selectionSort(saved_data, size)

# and here we stop our time
end = time.process_time()

print(f'Process time: {end - start}')
