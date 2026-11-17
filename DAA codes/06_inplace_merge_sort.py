# IN-PLACE MERGE SORT
# Idea : same as merge sort, but merging is done INSIDE the same list (no extra list).
#        If a right-half element is smaller, shift the elements in between one step
#        right and insert it.
# Time : O(n^2) worst case (shifting is costly).   Extra space: O(1) (besides recursion).

def merge(a, lo, mid, hi):
    i = lo                                # front of left half
    j = mid + 1                           # front of right half
    while i <= mid and j <= hi:
        if a[i] <= a[j]:
            i += 1                        # already in the right place
        else:
            value = a[j]                  # a[j] must go to position i
            k = j
            while k > i:                  # shift a[i..j-1] one step right
                a[k] = a[k - 1]
                k -= 1
            a[i] = value
            i += 1
            mid += 1                      # left half grew by one
            j += 1

def merge_sort(a, lo, hi):
    if lo >= hi:
        return
    mid = (lo + hi) // 2
    merge_sort(a, lo, mid)
    merge_sort(a, mid + 1, hi)
    merge(a, lo, mid, hi)

a = list(map(int, input("Enter numbers: ").split()))
merge_sort(a, 0, len(a) - 1)
print("Sorted:", a)
