# Original problem
# https://www.programcreek.com/2012/12/leetcode-median-of-two-sorted-arrays-java/
# GPL v3
import os
import sys
import heapq

def get_median(a):
    na = len(a[0])
    nb = len(a[1])
    if na == 0 and nb == 0:
        raise ValueError('Input arrays are empty.')
    n = na + nb
    if n % 2 == 0:
        k1 = (na + nb)/2
        k2 = k1 + 1
    else:
        k1 = (na + nb + 1)/2
        k2 = k1
        
    minhp = []
    if na > 0:
        aitem = (a[0][0], [0,0])
        heapq.heappush(minhp, aitem)
    if nb > 0:
        aitem = (a[1][0], [1,0])
        heapq.heappush(minhp, aitem)
    count = max(1, len(minhp) - 1)
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
    a = [[[1,5,6,8,9], [2,3,4,7,10]],
         [[], [5,7,11,16,20]],
         [[43, 47, 51, 57, 61, 67], []]]
    for i in range(len(a)):
        median = get_median(a[i])
        print('median = '+str(median))
     
