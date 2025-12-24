# Coin Change: Greedy vs Dynamic Programming

This homework compares two algorithms for the coin change problem using the following coin set:

`[50, 25, 10, 5, 2, 1]`

Algorithms:
- `find_coins_greedy(amount)` — greedy approach (largest coin first)
- `find_min_coins(amount)` — dynamic programming approach (minimum number of coins)

---

## Complexity Summary

Algorithm | Optimal (min coins) | Time Complexity | Space Complexity
---|---|---|---
Greedy | Not guaranteed for arbitrary coin sets | O(m) | O(k)
Dynamic Programming | Yes | O(amount · m) | O(amount)

Where:
- `m` — number of coin types (6)
- `k` — number of coin types used in the result

---

## Benchmark Setup

- Metric: execution time (seconds)
- Tool: `timeit`
- Repetitions per amount: **100**
- Tested amounts: 100, 1_000, 10_000, 100_000

---

## Measured Results

Total execution time (seconds) for 100 repetitions

Algorithm | 100 | 1_000 | 10_000 | 100_000
---|---:|---:|---:|---:
Greedy | 0.000033 | 0.000029 | 0.000029 | 0.000030
DP | 0.003596 | 0.032894 | 0.294072 | 2.956006

---

## Results Summary

- Greedy algorithm execution time remains almost constant for all tested amounts, since it iterates only over the fixed set of coin denominations.
- Dynamic programming execution time grows linearly with the amount, as it fills a DP table up to the target sum.
- For large sums, DP becomes significantly slower and requires much more memory due to its `O(amount)` space usage.

---

## Conclusion

- The greedy algorithm is extremely efficient for large amounts when the coin system is canonical, as in this task.
- The dynamic programming algorithm guarantees the minimum number of coins but scales poorly for large sums.
- In practice, greedy is preferable for performance, while DP is preferable when correctness must be guaranteed for any coin set.
