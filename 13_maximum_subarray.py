# MAXIMUM SUBARRAY SUM   (divide and conquer)
# Idea : the best subarray is in one of 3 places:
#        1) completely in the LEFT half      -> recursion
#        2) completely in the RIGHT half     -> recursion
#        3) CROSSING the middle              -> best sum ending at mid + best sum starting at mid+1
#        Answer = biggest of the three.
# Time : T(n) = 2T(n/2) + n  ->  O(n log n).

def max_crossing(a, lo, mid, hi):
    best_left = float("-inf")
    total = 0
    for i in range(mid, lo - 1, -1):      # go left from the middle
        total += a[i]
        if total > best_left:
            best_left = total

    best_right = float("-inf")
    total = 0
    for j in range(mid + 1, hi + 1):      # go right from the middle
        total += a[j]
        if total > best_right:
            best_right = total

    return best_left + best_right

def max_subarray(a, lo, hi):
    if lo == hi:                          # one element: it is the answer
        return a[lo]
    mid = (lo + hi) // 2
    left = max_subarray(a, lo, mid)
    right = max_subarray(a, mid + 1, hi)
    cross = max_crossing(a, lo, mid, hi)
    return max(left, right, cross)

a = list(map(int, input("Enter numbers: ").split()))
print("Maximum subarray sum =", max_subarray(a, 0, len(a) - 1))
