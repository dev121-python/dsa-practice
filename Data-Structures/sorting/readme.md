# Merge Sort

Merge sort is a **divide-and-conquer** sorting algorithm that sorts an array by
recursively dividing it into smaller subarrays, sorting them, and then merging
the sorted subarrays to produce the final sorted array.

---

## Algorithm Steps
1. Divide the array into two halves.
2. Recursively sort each half.
3. Merge the two sorted halves into a single sorted array.

---

## Time and Space Complexity

| Case    | Time Complexity |
|---------|-----------------|
| Best    | O(n log n)      |
| Average | O(n log n)      |
| Worst   | O(n log n)      |

- **Space Complexity:** O(n) auxiliary space (used during the merge step)

---

## Properties
- **Stable:** Yes
- **In-place:** No
- **Comparison-based:** Yes

---

## When to Use Merge Sort
- When guaranteed **O(n log n)** performance is required.
- When working with **linked lists**, where merge sort can be implemented efficiently.
- When **stability** (preserving relative order of equal elements) matters.

---

## Comparison
Merge sort is preferred over simpler algorithms like insertion sort for large
datasets due to its consistent O(n log n) time complexity, although it requires
additional memory.
