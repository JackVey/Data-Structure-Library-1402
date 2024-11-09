# navid ebadi
# 401222093

import random


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
    elif A[p].key == 0:
        return r
    return p


class aclass:
    def __init__(self, key, data):
        self.key = key
        self.satellite = data

    def __str__(self):
        return f'({self.key},{self.satellite})'


A = [aclass(random.randint(0, 1), chr(i+97)) for i in range(30)]
# A=[aclass(*x) for x in [(0,'a'),(0,'b'),(0,'c'),(0,'d'),(0,'e'),(0,'f')]]
print(*A)
print()
BinaryStableSort(A, 0, len(A))
print(*A)
