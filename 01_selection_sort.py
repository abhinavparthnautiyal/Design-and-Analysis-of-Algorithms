# SELECTION SORT
# Idea : find the smallest element in the unsorted part, put it at the front. Repeat.
# Time : always O(n^2) (best = worst), because it always scans the whole unsorted part.

a = list(map(int, input("Enter numbers: ").split()))
n = len(a)

for i in range(n - 1):
    smallest = i
    for j in range(i + 1, n):
        if a[j] < a[smallest]:
            smallest = j
    if smallest != i:
        a[i], a[smallest] = a[smallest], a[i]

print("Sorted:", a)