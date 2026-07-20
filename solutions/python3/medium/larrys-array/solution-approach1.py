# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/larrys-array/problem?isFullScreen=true
# Problem     Larry's Array
# Difficulty  Medium
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-20, 03:02 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#

def larrysArray(A):
    # Initialize inversion counter
    inversions = 0
    n = len(A)
    
    # Compare each pair of elements
    for i in range(n):
        for j in range(i + 1, n):
            # If a larger number comes before a smaller number, it's an inversion
            if A[i] > A[j]:
                inversions += 1
                
    # If total inversions are even, it can be sorted
    if inversions % 2 == 0:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
