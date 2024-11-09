# navid ebadi
# 401222093

import random

def randList(seed, n):
  random.seed(seed)
  return [random.randint(0,1000) for x in range(n)]


def BlockSwap(A, p, q):
    for i in range(0, q-p):
        (A[p+i], A[q+i]) = (A[q+i], A[p+i])


def StableRBA(A, p, q, r):
    n0 = r-q
    n1 = q-p
    if n1 == 0:
        return r
    while n0 > 0:
        if n1 > n0:
            p = q-n0
            BlockSwap(A, p, q)
            n1 = n1-n0
            q = p
            p = p-n1
        else:
            BlockSwap(A, p, q)
            n0 = n0-n1
            p = q
            q = q+n1
    return p


def BinaryStableSort(A, p, r):
    if r-p > 1:
        q = (p+r)//2
        p = BinaryStableSort(A, p, q)
        r = BinaryStableSort(A, q, r)
        p = StableRBA(A, p, q, r)
    elif radixkey(A[p])==0 :
        return r
    return p


mask = 1
def radixkey(x):
    return x & mask

def inplaceRadixSort(x, n):
    global mask
    mask = 1
    for _ in range(32):
        BinaryStableSort(x, 0, n)
        mask <<= 1


A = randList(1401, 100)

inplaceRadixSort(A , len(A) )
print(A)