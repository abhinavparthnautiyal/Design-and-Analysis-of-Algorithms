# LINEAR SEARCH
# Idea : check every element one by one from the start.
# Time : best O(1) (key is first), worst O(n) (key is last or missing).
# Works on any list - it does NOT need to be sorted.

a = list(map(int, input("Enter numbers: ").split()))
key = int(input("Enter number to search: "))

position = -1
for i in range(len(a)):
    if a[i] == key:
        position = i
        break                             # stop as soon as it is found

if position == -1:
    print("Not found")
else:
    print("Found at index", position)
