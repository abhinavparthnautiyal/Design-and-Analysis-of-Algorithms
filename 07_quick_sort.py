# QUICK SORT   (divide and conquer)
# Idea : pick the first element as PIVOT, place it at its correct position so that
#        smaller-or-equal elements are on its left and bigger ones on its right.
#        Then sort the left part and the right part the same way.
# Partition (as in class):
#   p moves RIGHT until it finds an element > pivot
#   q moves LEFT  until it finds an element <= pivot
#   if p is still left of q -> swap them and continue
#   otherwise (they crossed) -> swap pivot with a[q]; pivot is now in its final place
# Time : best/average O(n log n), worst O(n^2) (already sorted or reversed list).

def partition(a, lo, hi):
    pivot = a[lo]
    p = lo + 1
    q = hi
    while True:
        while p <= hi and a[p] <= pivot:  # move p right
            p += 1
        while a[q] > pivot:               # move q left
            q -= 1
        if p < q:
            a[p], a[q] = a[q], a[p]
        else:
            break
    a[lo], a[q] = a[q], a[lo]             # pivot goes to its final position
    return q

def quick_sort(a, lo, hi):
    if lo < hi:
        q = partition(a, lo, hi)
        quick_sort(a, lo, q - 1)          # left of pivot
        quick_sort(a, q + 1, hi)          # right of pivot

a = list(map(int, input("Enter numbers: ").split()))
quick_sort(a, 0, len(a) - 1)
print("Sorted:", a)
