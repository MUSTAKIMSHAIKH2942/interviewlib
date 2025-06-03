from core import *

print("🔁 Reverse:", reverse_string("hello"))
print("🔢 Prime check:", is_prime(11))
print("🔍 Char Frequency:", char_frequency("banana"))
print("📈 Second Largest:", second_largest([1, 5, 2, 8, 4]))
print("➕ Two Sum:", two_sum([2, 7, 11, 15], 9))
print("🔁 Permutations:", permutations("abc"))
print("📦 Merge Intervals:", merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
print("🔄 Rotate Matrix:")
for row in rotate_matrix_90([[1,2,3],[4,5,6],[7,8,9]]):
    print(row)
print("🔐 Balanced:", balanced_parentheses("{[()]}"))
