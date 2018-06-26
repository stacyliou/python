# Original problem
# https://www.programcreek.com/2014/05/leetcode-meeting-rooms-ii-java/
# AGPL v3

import os
import sys
import heapq

def min_rooms(arr):
  starthp = []
  endhp = []
  for s, e in arr:
    heapq.heappush(starthp,s)
    heapq.heappush(endhp,e)
# model the problem as matching brackets with time as priority
  while starthp and endhp:
    if starthp[0] < endhp[0]:
        heapq.heappop(starthp)
    elif starthp[0] >= endhp[0]:
        heapq.heappop(endhp)
  count = len(endhp)
  del endhp
  return count
  
a = [[0, 30],[5, 10],[25, 40],[10, 15]] # => count = 2
num_rooms = min_rooms(a)
print(num_rooms)
