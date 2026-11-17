# MAXIMUM SUBARRAY SUM   (Kadane's algorithm)
# Idea : go left to right. At each element, either extend the previous subarray
#        or start a fresh subarray from this element, whichever is bigger.
# Time : O(n).   Extra space: O(1).

a = list(map(int, input("Enter numbers: ").split()))

current = a[0]                            # best sum of a subarray ENDING at this element
best = a[0]                               # best sum seen anywhere so far

for i in range(1, len(a)):
    current = max(a[i], current + a[i])   # extend the old one, or start fresh here
    best = max(best, current)             # update the overall best

print("Maximum subarray sum =", best)