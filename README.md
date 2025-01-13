# Day-13-BFS
Here's Python Program for BFS (Breadth First Search). Day 13 of Day 365.
- Initial Setup: Start with an array and a target value to find.
- Iterate Through Array: Begin from the first element of the array and check each element one by one.
- Comparison:
  - If the current element is equal to the target value, the search is successful, and the index of the element is returned.
  - If the current element is not equal to the target value, move to the next element.
- Completion:
  - If the target value is found, return its index.
  - If the target value is not found after checking all elements, return -1 (indicating that the element is not in the array).

Example: Array = [5, 3, 8, 4, 2], Target = 4

1. Initial Array: [5, 3, 8, 4, 2]
2. Target Check: 
   - 5 ≠ 4
   - 3 ≠ 4
   - 8 ≠ 4
   - 4 = 4 (Target found at index 3)

Result: Target value 4 is found at index 3. If the target was not found, it would return -1.
