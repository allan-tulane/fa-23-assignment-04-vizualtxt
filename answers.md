# CMPS 2200 Assignment 4
## Answers

**Name:** Ali Sulehria


Place all written answers from `assignment-04.md` here for easier grading.

1a) For N dollars, the greedy algorithm would be similar to partial-sums division: choose the greatest value coin that is less than N minus the sum, then add that value to the sum and repeat.

b) Greedy choice property: the optimal solution is chosen by selecting the most optimal choice at every point (highest possible value without exceeding N)
The optimal solution is found by picking the most optimal choice at every point, so the optimal substructure property holds.

c) The work of this algorithm is W(n) = O(log n), as it is split with every step (at least in half), and it is not parallelized, so S = O(n) as well.

2a) For a total N = 50, and denominations of 1, 2, 4, 5, 8, and 30. The greedy algorithm would choose 30 + 8 + 5 + 4 + 2 + 1, yielding 50 when the ideal solution would be 30 + 5 (x4) = 50 or 30 + (8 x 2) + 4.

2b) This still has an optimal substructure property because at each point, i.e. for each subproblem, the algorithm is still taking into account the optimal solution and making its choice based on this. While the choice is no longer greedy, it is still optimal, leading to a globally optimal solution.

2c) An algorithm to solve this prolem could use memoization to store the optimal solutions for the possible subproblems, ie the possible remaining sums. For each denomination value up to N, the optimal solution from that value to 0 is calculated and stored in a list. To find the global optimal solution, at each point one would choose the coin with the shortest path to 0.