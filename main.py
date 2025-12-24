from timeit import timeit
from greedy_algorithm import find_coins_greedy
from dp_algorithm import find_min_coins


def benchmark(algorithm, amount, number):
    return timeit(lambda: algorithm(amount), number=number)


def main():
    amounts = [100, 1_000, 10_000, 100_000]
    reps = 100

    algorithms = [
        ("Greedy", find_coins_greedy),
        ("DP", find_min_coins),
    ]

    print(f"Repetitions per amount: {reps}")

    for name, fn in algorithms:
        print(f"\n=== Algorithm: {name} ===")

        for a in amounts:
            elapsed = benchmark(fn, a, reps)
            print(f"{a:>8} -> {elapsed:.6f} seconds")


if __name__ == "__main__":
    main()
