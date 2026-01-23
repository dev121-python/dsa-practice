## Stack Problems

### P1. Build an Array With Stack Operations
- Idea: Simulate stack operations while iterating through numbers from 1 to n.
- Why stack: We need to push and conditionally pop to match the target array.
- Time Complexity: O(n)
- Space Complexity: O(n)

### P2. MinStack (LC 155)
- Idea: Maintain an additional stack to track minimum values at each step.
- Why stack: Stack allows constant-time access to the latest element and min.
- Time Complexity: O(1) per operation
- Space Complexity: O(n)

### P3. Maximum Frequency Stack (LC 895)
- Idea: Maintain a frequency map to track how often each element appears.
- Grouping: Use stacks grouped by frequency so elements with the same frequency are stored together.
- Pop logic: Always pop from the stack corresponding to the current maximum frequency.
- Time Complexity: O(1) per push and pop
- Space Complexity: O(n)


