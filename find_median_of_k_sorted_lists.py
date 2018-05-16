# Original problem
# https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/
# GPL v3
import os
import sys
import heapq
import numpy as np

def get_median(a):
    size = len(a)
    ni = np.zeros(size, dtype = int)
    n = 0
    for i in range(size):
        ni[i] = len(a[i])
        if ni[i] == 0:
            raise ValueError('Empty array given at index '+str(i)+'.')
        n += ni[i]
    if n == 0:
        raise ValueError('Input arrays are empty.')
    if n % 2 == 0:
        k1 = n/2
        k2 = k1 + 1
    else:
        k1 = (n + 1)/2
        k2 = k1
        
    minhp = []
    for i in range(size):
        aitem = (a[i][0], [i,0])
        heapq.heappush(minhp, aitem)
    count = 1
    # keep median in heap
    while count < k2:
        minitem = heapq.heappop(minhp)
        aid, eid = minitem[1]
        cid = eid + 1
        aitem = (a[aid][cid], [aid, cid])
        heapq.heappush(minhp, aitem)
        count += 1
    median = minhp[0][0]
    del minhp
    if k1 != k2:
        median = (median + a[aid][eid])/2
    return median

if __name__ == '__main__':
    a = [[1,5,8,9], [2,3,7,10], 
#          [4,6,11,15], [9,14,16,19], [2,4,6,9], 
         [12]]

    median = get_median(a)
    print(median)
    
