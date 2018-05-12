# Original problem
# https://www.programcreek.com/2014/04/leetcode-count-primes-java/
# GPL v3
import sys
import os
import numpy as np

def getprimes(n):
    idarr = np.ones(n, dtype=int)
    idarr[0] = 0 # 1 is not a prime number
    output = []
    for j in range(n):
        k = j+1
        if idarr[j] == 1: # all multiples of k are not prime
            idarr[j+k::k] = 0
    idx = 0
    while idx < n :
        if idarr[idx] == 1 :
            output.append(idx+1)
        idx += 1
    return output

if __name__ == '__main__':
    a = [30,50]
    narr = len(a)
    for i in range(narr):
        output = getprimes(a[i])
        print(output)
        del output
