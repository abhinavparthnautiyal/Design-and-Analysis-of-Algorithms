# ACTIVITY SELECTION   (greedy)
# Idea : we want the MAXIMUM NUMBER of activities that do not overlap.
#        Sort by FINISH time. Pick the first one, then keep picking the next
#        activity that starts at or after the finish of the last picked one.
# Time : O(n log n) because of sorting (the picking loop is only O(n)).

n = int(input("Number of activities: "))
start = list(map(int, input("Start times : ").split()))
finish = list(map(int, input("Finish times: ").split()))

activities = []                           # (finish, start, number) -> sorts by finish time
for i in range(n):
    activities.append((finish[i], start[i], i + 1))
activities.sort()

selected = [activities[0]]                # earliest finishing activity is always picked
last_finish = activities[0][0]

for f, s, number in activities[1:]:
    if s >= last_finish:                  # does not overlap with the last picked one
        selected.append((f, s, number))
        last_finish = f

print("Maximum activities =", len(selected))
for f, s, number in selected:
    print("Activity", number, "(", s, "to", f, ")")
