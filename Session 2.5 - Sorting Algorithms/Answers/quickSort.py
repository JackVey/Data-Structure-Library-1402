import pickle
import time


def partition(arr, low, high):

    # Choose the pivot
    pivot = arr[(high + low) // 2]

    arr[low], arr[high]= arr[high], arr[low]

    i = low - 1
    
    # Traverse arr[low..high] and move all smaller
    # elements on the left side. Elements from low to 
    # i are smaller after every iteration
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Move pivot after smaller elements and
    # return its position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# The QuickSort function implementation
def quick_sort(arr, low, high):
    if low < high:
        # pi is the partition return index of pivot
        pi = partition(arr, low, high)

        # Recursion calls for smaller elements
        # and greater or equals elements
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Function to print an array
def print_array(arr):
    for i in arr:
        print(i, end=" ")
    print()

# Driver code

if __name__ == "__main__":
#
#     with open("my_list_best.pkl", "rb") as f:
#         arr_best = pickle.load(f)
# #         print(arr_best)
#         start = time.time()
#         quick_sort(arr_best, 0, len(arr_best) - 1)
#         end = time.time()
#         print(f'Process time of best case: {end - start}')
#
#     with open("my_list_worst.pkl", "rb") as f:
#         arr_worst = pickle.load(f)
# #         print(arr_worst)
#         start = time.time()
#         quick_sort(arr_worst, 0, len(arr_worst) - 1)
#         end = time.time()
#         print(f'Process time of worst case: {end - start}')
    sum = 0
    for i in range(5):
        with open("my_list_rand_" + str(i) + ".pkl", "rb") as f:
            arr_worst = pickle.load(f)
    #         print(arr_rand)
            start = time.time()
            quick_sort(arr_worst, 0, len(arr_worst) - 1)
            end = time.time()
            sum += end - start
    print(f'Process time of rand case: {sum / 5.}')
