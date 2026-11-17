# INSERTION SORT
# Idea : like sorting playing cards in your hand. Take the next card (key),
#        shift bigger cards right, drop the key into the gap.
# Time : best O(n) (already sorted), worst O(n^2) (reversed).

a = list(map(int, input("Enter numbers: ").split()))
n = len(a)

for i in range(1, n):
    key = a[i]                            # card to insert
    j = i - 1
    while j >= 0 and a[j] > key:          # bigger cards on the left...
        a[j + 1] = a[j]                   # ...move one step right
        j -= 1
    a[j + 1] = key                        # put the key in the gap

print("Sorted:", a)
