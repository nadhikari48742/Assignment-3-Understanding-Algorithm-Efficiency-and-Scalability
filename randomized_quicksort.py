# Quicksort Implementations and Empirical Comparison

import random
import time
from statistics import median

def randomized_quicksort(a):
    if len(a) <= 1:
        return a
    pivot = a[random.randrange(len(a))]
    left = [x for x in a if x < pivot]
    mid = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return randomized_quicksort(left) + mid + randomized_quicksort(right)

def deterministic_quicksort(a):
    out = list(a)
    if len(out) <= 1:
        return out

    stack = [(0, len(out) - 1)]
    while stack:
        lo, hi = stack.pop()
        if lo >= hi:
            continue

        pivot = out[lo]
        lt = lo
        i = lo
        gt = hi
        while i <= gt:
            if out[i] < pivot:
                out[lt], out[i] = out[i], out[lt]
                lt += 1
                i += 1
            elif out[i] > pivot:
                out[i], out[gt] = out[gt], out[i]
                gt -= 1
            else:
                i += 1

        left_lo, left_hi = lo, lt - 1
        right_lo, right_hi = gt + 1, hi

        left_size = left_hi - left_lo
        right_size = right_hi - right_lo
        if left_size > right_size:
            if left_lo < left_hi:
                stack.append((left_lo, left_hi))
            if right_lo < right_hi:
                stack.append((right_lo, right_hi))
        else:
            if right_lo < right_hi:
                stack.append((right_lo, right_hi))
            if left_lo < left_hi:
                stack.append((left_lo, left_hi))

    return out

def _time_one(sort_fn, data):
    t0 = time.perf_counter()
    sort_fn(list(data))
    return time.perf_counter() - t0

def benchmark(sort_fn, data, trials=7):
    times = []
    for _ in range(trials):
        times.append(_time_one(sort_fn, data))
    return median(times)

def make_inputs(n, repeated_k=10):
    rnd = list(range(n))
    random.shuffle(rnd)
    sorted_arr = list(range(n))
    rev = list(range(n - 1, -1, -1))
    rep = [random.randrange(repeated_k) for _ in range(n)]
    return {
        "random": rnd,
        "sorted": sorted_arr,
        "reverse": rev,
        "repeated": rep,
    }

if __name__ == "__main__":
    random.seed(0)
    sizes = [1000, 5000, 10000]
    trials = 7

    for n in sizes:
        inputs = make_inputs(n)
        print(f"\n=== n={n} (median of {trials} trials) ===")
        for name, arr in inputs.items():
            print(f"\n[{name}]")
            print("randomized:", benchmark(randomized_quicksort, arr, trials))
            print("deterministic:", benchmark(deterministic_quicksort, arr, trials))
