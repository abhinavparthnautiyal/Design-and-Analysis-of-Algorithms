# OPTIMISED BUBBLE SORT
# Idea : same as bubble sort, but if a whole pass makes NO swap the list is
#        already sorted, so stop.
# Time : best O(n) (sorted list, one pass), worst O(n^2).

a = list(map(int, input("Enter numbers: ").split()))
n = len(a)

for i in range(n - 1):
    swapped = False
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            swapped = True
    if not swapped:                       # no swap in this pass -> sorted
        break

print("Sorted:", a)
