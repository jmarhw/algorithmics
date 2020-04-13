import numpy as np
import matplotlib.pyplot as plt


def QuickSelect(A, k):
    return QS(A, 0, len(A) - 1, k)

count = 0
clist = []
def counter():
    global count, clist
    count=count+1

def QS(A,start,end,k):
    pivotIndex = partition(A,start,end)
    left = pivotIndex - start + 1                   #length of the part with smaller numbers
    if k == left:
        return A[pivotIndex]
    elif k < left:
        counter()
        return QS(A,start,pivotIndex - 1,k)
    else:
        counter()
        return QS(A,pivotIndex + 1,end, k-left)

def partition(A,start,end):
    pivot = A[end]
    index = start
    for i in range(start,end):
        if A[i] < pivot:
            A[index], A[i] = A[i], A[index]         #if current value < pivot, goes to the left
            index+=1
    A[end], A[index] = A[index], A[end]             #pivot goes into its place
    return index



for N in range(100,10100,100):
    for x in range(1,500):
        A = np.random.choice(10000,size=N,replace=False)
        QuickSelect(A, 7)
    clist.append(count/500)
    Nlist.append(N)


plt.plot(Nlist, clist,'.')
plt.xlabel("Size of the table")
plt.ylabel("Number of comparisons")
plt.ylim((0,1000))
plt.grid()
plt.show()