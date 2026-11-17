# BINARY SEARCH (iterative)
# Idea : the list must be SORTED. Look at the middle element:
#        equal -> found | key smaller -> search left half | key bigger -> search right half.
# Time : best O(1) (key in the middle), worst O(log n).   Extra space: O(1).

a = list(map(int, input("Enter numbers: ").split()))
a.sort()                                  # binary search needs a sorted list
print("Sorted list:", a)
key = int(input("Enter number to search: "))

low = 0
high = len(a) - 1
position = -1

while low <= high:
    mid = (low + high) // 2
    if a[mid] == key:
        position = mid
        break
    elif key < a[mid]:
        high = mid - 1                    # throw away the right half
    else:
        low = mid + 1                     # throw away the left half

if position == -1:
    print("Not found")
else:
    print("Found at index", position)
