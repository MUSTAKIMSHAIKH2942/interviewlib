# core.py
"""
Python Interview Questions Library
Author: Your Name
License: MIT
"""

# ===============================
# 🟢 EASY LEVEL FUNCTIONS
# ===============================

def reverse_string(s: str) -> str:
    return s[::-1]

def char_frequency(s: str) -> dict:
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# ===============================
# 🟡 MEDIUM LEVEL FUNCTIONS
# ===============================

def second_largest(nums: list) -> int:
    unique = list(set(nums))
    unique.sort()
    return unique[-2] if len(unique) >= 2 else None

def find_duplicates(lst: list) -> list:
    seen = set()
    dupes = set()
    for item in lst:
        if item in seen:
            dupes.add(item)
        seen.add(item)
    return list(dupes)

def is_anagram(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)

def two_sum(nums: list, target: int) -> list:
    seen = {}
    for i, num in enumerate(nums):
        rem = target - num
        if rem in seen:
            return [seen[rem], i]
        seen[num] = i
    return []

def merge_sorted_lists(a: list, b: list) -> list:
    i = j = 0
    merged = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged += a[i:] + b[j:]
    return merged

# ===============================
# 🔴 HARD LEVEL FUNCTIONS
# ===============================

def permutations(s: str) -> list:
    if len(s) <= 1:
        return [s]
    result = []
    for i, ch in enumerate(s):
        for perm in permutations(s[:i] + s[i+1:]):
            result.append(ch + perm)
    return result

def merge_intervals(intervals: list) -> list:
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    return merged

def rotate_matrix_90(matrix: list) -> list:
    return [list(row)[::-1] for row in zip(*matrix)]

def balanced_parentheses(expr: str) -> bool:
    stack = []
    pair = {')': '(', ']': '[', '}': '{'}
    for char in expr:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pair[char]:
                return False
            stack.pop()
    return not stack
