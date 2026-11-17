# BUBBLE SORT
# Idea : compare neighbours, swap if out of order. After each pass the biggest
#        element "bubbles" to the end.
# Time : always O(n^2) here, because it never stops early.

a = list(map(int, input("Enter numbers: ").split()))
n = len(a)

for i in range(n - 1):                    # n-1 passes
    for j in range(n - 1 - i):            # last i elements are already in place
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print("Sorted:", a)
