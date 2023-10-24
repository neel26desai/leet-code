def binary_cardinality(n):
    return bin(n).count('1')
def sort_by_binary_cardinality(arr):
    return sorted(arr, key=binary_cardinality)

nums = [31,15,7,3,2]
print(sort_by_binary_cardinality(nums))