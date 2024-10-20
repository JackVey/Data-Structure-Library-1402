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


if __name__ == "__main__":
#     with open("my_list_best.pkl", "rb") as f:
#         arr_best = pickle.load(f)
# #         print(arr_best)
#         start = time.time()
#         insertionSort(arr_best)
#         end = time.time()
#         print(f'Process time of best case: {end - start}')
#
#     with open("my_list_worst.pkl", "rb") as f:
#         arr_worst = pickle.load(f)
# #         print(arr_worst)
#         start = time.time()
#         insertionSort(arr_worst)
#         end = time.time()
#         print(f'Process time of worst case: {end - start}')
    sum = 0
    for n in range(5):
        with open("my_list_rand_" + str(n) + ".pkl", "rb") as f:
            arr_rand = pickle.load(f)
        #         print(arr_rand)
            start = time.time()
            insertionSort(arr_rand)
            end = time.time()
            sum += end - start
    print(f'Process time of rand case: {sum/5.}')

