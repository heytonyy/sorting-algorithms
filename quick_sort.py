import numpy as np
import time


def quick_sort(numbers: list[int]) -> list[int]:
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = numbers.pop()

    items_greater = []
    items_lower = []

    for item in numbers:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


if __name__ == "__main__":
    # list of X random numbers between 0 and 10000
    arr = np.random.randint(0, 10000, 10000)
    startTime = time.time()
    quick_sort(arr)
    executionTime = (time.time() - startTime)
    print(f"Done! Time taken: {executionTime:.2f} seconds.")
