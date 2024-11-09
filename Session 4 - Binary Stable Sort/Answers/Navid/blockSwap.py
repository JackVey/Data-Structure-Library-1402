# navid ebadi
# 401222093


def BlockSwap(A, p, q):
    for i in range(0, q-p):
        (A[p+i], A[q+i]) = (A[q+i], A[p+i])


A = [2, 3, 4, 1, 5, 7, 23, 78, 23, 56, 16, 34]

BlockSwap(A, 2, 5)

print(A)
