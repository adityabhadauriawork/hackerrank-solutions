# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true
# Problem     2D Array - DS
# Difficulty  Easy
# Subdomain   Arrays
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-20, 02:31 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Initialize max_sum to the lowest possible theoretical value
    # Minimum possible value per element is -9, and an hourglass has 7 elements: -9 * 7 = -63
    max_sum = -63 
    
    # Iterate through the rows (0 to 3)
    for i in range(4):
        # Iterate through the columns (0 to 3)
        for j in range(4):
            # Calculate the sum of the current hourglass
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            mid = arr[i+1][j+1]
            bot = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            
            current_sum = top + mid + bot
            
            # Update max_sum if the current hourglass sum is greater
            if current_sum > max_sum:
                max_sum = current_sum
                
    return max_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
