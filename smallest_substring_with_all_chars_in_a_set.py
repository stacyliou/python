# Original problem
# https://www.careercup.com/question?id=5092414932910080
# AGPL v3
import os
import sys

def get_shortest_unique_substring(arr, tstr):
  start = 0
  end = 0
  n = len(tstr)
  m = len(arr)
  found = 0
  check = {}
  minlen = n
  minstr = ''
  npass = 0
  if n < m:
    return minstr
  
  # npass; all elements in arr are unique
  for c in arr:
    check[c] = 0 
    
  while start <= end and end < n:
    # keep looking by extending the sub string
    if tstr[end] not in check: 
      end += 1
    elif check[tstr[end]] == npass:
      check[tstr[end]] = npass + 1
      found += 1
    # already found in this pass
    else: 
      end += 1
    if found == m:
      if end - start + 1 < minlen:
        minlen = end - start + 1
        minstr = tstr[start:end+1]
      start += 1
      end = start
      found = 0
      npass += 1
  return minstr

a = ['a','b','c']
test = 'abbcbcba'
sub = get_shortest_unique_substring(a, test)
print(sub)
