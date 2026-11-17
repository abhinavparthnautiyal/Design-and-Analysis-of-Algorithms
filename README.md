# Design and Analysis of Algorithms (DAA) - Lab Programs

Simple, beginner-friendly Python implementations of the core algorithms from the DAA course (Units 1-3).
Each program is a single standalone file with a short comment at the top explaining the **idea** and the **time complexity**, so the code is easy to read, trace by hand and explain.

## Contents

| # | Program | Technique | Best case | Worst case |
|---|---------|-----------|-----------|------------|
| 01 | [Selection Sort](python_codes/01_selection_sort.py) | Brute force | O(n²) | O(n²) |
| 02 | [Insertion Sort](python_codes/02_insertion_sort.py) | Incremental | O(n) | O(n²) |
| 03 | [Bubble Sort](python_codes/03_bubble_sort.py) | Brute force | O(n²) | O(n²) |
| 04 | [Optimised Bubble Sort](python_codes/04_optimised_bubble_sort.py) | Early-exit flag | O(n) | O(n²) |
| 05 | [Merge Sort](python_codes/05_merge_sort.py) | Divide & Conquer | O(n log n) | O(n log n) |
| 06 | [In-place Merge Sort](python_codes/06_inplace_merge_sort.py) | Divide & Conquer | O(n log n) | O(n²) |
| 07 | [Quick Sort](python_codes/07_quick_sort.py) | Divide & Conquer | O(n log n) | O(n²) |
| 08 | [Linear Search](python_codes/08_linear_search.py) | Brute force | O(1) | O(n) |
| 09 | [Binary Search (iterative)](python_codes/09_binary_search_iterative.py) | Divide & Conquer | O(1) | O(log n) |
| 10 | [Binary Search (recursive)](python_codes/10_binary_search_recursive.py) | Divide & Conquer | O(1) | O(log n) |
| 11 | [Fractional Knapsack](python_codes/11_fractional_knapsack.py) | Greedy | O(n log n) | O(n log n) |
| 12 | [Activity Selection](python_codes/12_activity_selection.py) | Greedy | O(n log n) | O(n log n) |
| 13 | [Maximum Subarray Sum](python_codes/13_maximum_subarray.py) | Divide & Conquer | O(n log n) | O(n log n) |

Notes on the table:
- Quick sort's worst case happens on already sorted or reverse-sorted input (first element is the pivot).
- Merge sort (05) uses list slicing, so it needs O(n) extra space. The in-place version (06) needs no extra array, but shifting elements makes a single merge cost up to O(n²).
- Sorting dominates the cost of the two greedy programs; the selection loop itself is O(n).

## Requirements

- Python 3.6 or newer
- No external libraries

## How to run

Every program reads its input from the keyboard. Run a file and type the input when prompted.

```bash
python python_codes/01_selection_sort.py
```

```
Enter numbers: 5 2 12 3 9 8
Sorted: [2, 3, 5, 8, 9, 12]
```

### Input formats

| Programs | Input |
|----------|-------|
| 01-07 (sorting) | One line of space-separated integers |
| 08-10 (searching) | A line of space-separated integers, then the key to search. Binary search sorts the list first, since it requires sorted input. |
| 11 (fractional knapsack) | Number of items, a line of profits, a line of weights, then the capacity |
| 12 (activity selection) | Number of activities, a line of start times, a line of finish times |
| 13 (maximum subarray) | One line of space-separated integers (may include negatives) |

### Examples

**Fractional knapsack**
```
Number of items: 7
Profits: 10 5 15 7 6 18 3
Weights: 2 3 5 7 1 4 1
Knapsack capacity: 15
Maximum profit = 55.33
```

**Activity selection**
```
Number of activities: 6
Start times : 1 3 0 5 8 5
Finish times: 2 4 6 7 9 9
Maximum activities = 4
```

**Maximum subarray**
```
Enter numbers: 12 -34 40 10 -57 17 20 45 -34 5
Maximum subarray sum = 82
```

## Key ideas in one line each

- **Selection sort** - repeatedly move the smallest remaining element to the front.
- **Insertion sort** - insert each element into its place in the sorted part on the left.
- **Bubble sort** - swap neighbours that are out of order; the largest value bubbles to the end each pass.
- **Merge sort** - split in half, sort each half, merge the two sorted halves.
- **Quick sort** - place a pivot at its final position, then sort the two sides.
- **Binary search** - compare with the middle element and discard half of the list each step.
- **Fractional knapsack** - take items by highest profit/weight; split the last item if needed.
- **Activity selection** - sort by finish time and always pick the next compatible activity.
- **Maximum subarray** - the best subarray lies in the left half, the right half, or crosses the middle.

## Testing

All programs were checked against reference results on randomly generated inputs:
the sorts and searches against Python's built-in `sorted()` and membership checks, maximum subarray and
activity selection against brute force over all possibilities, and fractional knapsack against an independent greedy
calculation. The worked examples from the course practice sheets give the expected answers.

## Repository structure

```
.
├── README.md
└── python_codes/
    ├── 01_selection_sort.py
    ├── 02_insertion_sort.py
    ├── 03_bubble_sort.py
    ├── 04_optimised_bubble_sort.py
    ├── 05_merge_sort.py
    ├── 06_inplace_merge_sort.py
    ├── 07_quick_sort.py
    ├── 08_linear_search.py
    ├── 09_binary_search_iterative.py
    ├── 10_binary_search_recursive.py
    ├── 11_fractional_knapsack.py
    ├── 12_activity_selection.py
    └── 13_maximum_subarray.py
```

## Author

<your name> - <your course / roll number>
