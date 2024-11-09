import random
import pickle

def randList(seed, n):
  random.seed(seed)
  return [random.randint(0,1000000) for x in range(n)]

def merge_sort(arr, left, right):
  if left < right:
    mid = (left + right) // 2

    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)
    merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
      L[i] = arr[left + i]
    for j in range(n2):
      R[j] = arr[mid + 1 + j]

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    # Merge the temp arrays back
    # into arr[left..right]
    while i < n1 and j < n2:
      if L[i] <= R[j]:
        arr[k] = L[i]
        i += 1
      else:
        arr[k] = R[j]
        j += 1
      k += 1

    # Copy the remaining elements of L[],
    # if there are any
    while i < n1:
      arr[k] = L[i]
      i += 1
      k += 1

    # Copy the remaining elements of R[],
    # if there are any
    while j < n2:
      arr[k] = R[j]
      j += 1
      k += 1

# here we save it to .pkl file using pickle library
def saveToFile(filename, list):
  with open(filename, 'wb') as file:
    pickle.dump(list, file)


n = 400000
# print(randList(1401,n))
arr = randList(1401, n)
# here we save the rand case
saveToFile("my_list_rand.pkl", arr)
merge_sort(arr, 0, len(arr) - 1)
# here we save the best case
saveToFile("my_list_best.pkl", arr)
arr.reverse()
# here we save the worst case
saveToFile("my_list_worst.pkl", arr)
