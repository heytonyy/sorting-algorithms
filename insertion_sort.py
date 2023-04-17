import numpy as np
from tqdm import tqdm
import time


def insertion_sort(numbers: list[int]) -> list[int]:
    for i in tqdm(range(1, len(numbers))):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = key
    return numbers


if __name__ == "__main__":
    # list of X random numbers between 0 and 10000
    arr = np.random.randint(0, 10000, 10000)
    startTime = time.time()
    insertion_sort(arr)
    executionTime = (time.time() - startTime)
    print(f"Done! Time taken: {executionTime:.2f} seconds.")
