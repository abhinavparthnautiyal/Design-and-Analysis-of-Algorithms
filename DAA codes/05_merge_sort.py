# MERGE SORT   (divide and conquer)
# Idea : split the list in half, sort each half, merge the two sorted halves.
# Time : always O(n log n).   Extra space: O(n) (new lists are created).

def merge_sort(a):
    if len(a) <= 1:                       # 0 or 1 element is already sorted
        return a

    mid = len(a) // 2
    left = merge_sort(a[:mid])            # sort left half
    right = merge_sort(a[mid:])           # sort right half

    result = []                           # merge: always take the smaller front element
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]                    # one side is finished, copy the rest of the other
    result += right[j:]
    return result

a = list(map(int, input("Enter numbers: ").split()))
print("Sorted:", merge_sort(a))
