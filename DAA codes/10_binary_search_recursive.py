# BINARY SEARCH (recursive)
# Idea : same as the iterative version, but the function calls itself on the half
#        that can still contain the key. If low > high, the range is empty -> not found.
# Time : O(log n).   Recurrence: T(n) = T(n/2) + 1.   Extra space: O(log n) (call stack).

def binary_search(a, low, high, key):
    if low > high:                        # base case: nothing left to search
        return -1
    mid = (low + high) // 2
    if a[mid] == key:
        return mid
    elif key < a[mid]:
        return binary_search(a, low, mid - 1, key)    # left half
    else:
        return binary_search(a, mid + 1, high, key)   # right half

a = list(map(int, input("Enter numbers: ").split()))
a.sort()                                  # binary search needs a sorted list
print("Sorted list:", a)
key = int(input("Enter number to search: "))

position = binary_search(a, 0, len(a) - 1, key)
if position == -1:
    print("Not found")
else:
    print("Found at index", position)
