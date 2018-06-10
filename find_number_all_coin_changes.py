# Original problem
# https://leetcode.com/problems/coin-change-2/description/
# AGPL v3

import os
import sys

from functools import wraps

def memoize(func):
    memo = {}
    @wraps(func)
    def helper(*args, **kwargs):
        key = (args[2], args[0])
        if key not in memo:
            memo[key] = func(*args, **kwargs)
        return memo[key]
    return helper

@memoize
def getWays(n, arr, m):
    if n < 0 or arr == None or m <= 0:
        return 0
    if n == 0:
        return 1
    coin = arr[m-1]
    # first search for subsets of coins w/o current coin sum to n;
    # then add solution for sum = (n - coin) for adding current coin
    return getWays(n, arr, m-1) + getWays(n-coin, arr, m)

if __name__ == '__main__':
    n = 3
    c = [8,3,1,2]
    m = len(c)
    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'
    ways = getWays(n, c, m)
    print(ways)
