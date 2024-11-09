#navid ebadi
#401222093
#row major

def sift_down(arr, index, size):
    left_child_index = 2 * index + 1
    right_child_index = 2 * index + 2
    smallest = index

    if left_child_index < size and arr[left_child_index] < arr[smallest]:
        smallest = left_child_index

    if right_child_index < size and arr[right_child_index] < arr[smallest]:
        smallest = right_child_index

    if smallest != index:
        arr[index], arr[smallest] = arr[smallest], arr[index]
        sift_down(arr, smallest, size)



class myclass_row :
    def __init__(self , arr , row , col):
        self.arr = arr
        self.col = col
        self.row = row

    
    def show (self):
        for i in range(0,self.row):
            print(self.arr[i*self.col:(i*self.col)+self.col])

    def getAt(self , i , j):
        return self.arr[(i-1)*self.col + j-1]

    def setAt(self , i , j , x):
        self.arr[(i-1)*self.col + j-1] = x

    def index_to_ij(self , k):
        i = k // self.col +1
        j = k % self.col 

    def ij_to_index(self , i , j):
        return (i-1)*self.col + j-1
    
    def build_young (self):
        for i in range(self.row , 0 ,-1):
            for j in range(self.col , 0 ,-1):
                k = self.ij_to_index(i , j)
                sift_down(self.arr , k , len(self.arr))
    



arr = [1 ,3 ,2, 45, 194, 233, 34, 5, 8 ,48 ,23 ,56 ]

test = myclass_row(arr , 4 , 3)
test.show()
print("__________________________")
test.build_young()
test.show()