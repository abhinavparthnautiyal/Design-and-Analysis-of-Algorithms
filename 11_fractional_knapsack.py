# FRACTIONAL KNAPSACK   (greedy)
# Idea : items can be broken into pieces. Best item = highest profit/weight.
#        Take items in that order; if the next one does not fit completely,
#        take only the fraction that fits and stop.
# Time : O(n log n) because of sorting.

n = int(input("Number of items: "))
profit = list(map(float, input("Profits: ").split()))
weight = list(map(float, input("Weights: ").split()))
capacity = float(input("Knapsack capacity: "))

items = []                                # each item = (profit/weight, profit, weight)
for i in range(n):
    items.append((profit[i] / weight[i], profit[i], weight[i]))

items.sort(reverse=True)                  # highest profit/weight first

total_profit = 0
for ratio, p, w in items:
    if capacity >= w:                     # whole item fits
        total_profit += p
        capacity -= w
    else:                                 # take only the fraction that fits
        total_profit += ratio * capacity
        break

print("Maximum profit =", round(total_profit, 2))
