# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/sam-and-substrings/problem?isFullScreen=true
# Problem     Sam and substrings
# Difficulty  Medium
# Subdomain   Dynamic Programming
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-20, 02:59 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3
import sys

def substrings(s):
    # HackerRank requires the result modulo 10^9 + 7
    MOD = 10**9 + 7
    
    total_sum = 0
    current_substring_sum = 0
    
    # Iterate through each digit in the string
    for i, char in enumerate(s):
        digit = int(char)
        
        # Calculate the sum of all substrings ending at the current digit
        current_substring_sum = (current_substring_sum * 10 + (i + 1) * digit) % MOD
        
        # Add the current subset sum to our total answer
        total_sum = (total_sum + current_substring_sum) % MOD
        
    return total_sum

if __name__ == '__main__':
    # Using sys.stdin.read to quickly read the input string
    s = sys.stdin.read().strip()
    if s:
        print(substrings(s))
