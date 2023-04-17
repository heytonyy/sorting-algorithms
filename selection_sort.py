import numpy as np
from tqdm import tqdm
import time


def selection_sort(numbers: list) -> list:
    for i in tqdm(range(len(numbers))):
        min_index = i
        for j in range(i+1, len(numbers)):
            if numbers[min_index] > numbers[j]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers


if __name__ == "__main__":
    # list of X random numbers between 0 and 10000
    arr = np.random.randint(0, 10000, 10000)
    startTime = time.time()
    selection_sort(arr)
    executionTime = (time.time() - startTime)
    print(f"Done! Time taken: {executionTime:.2f} seconds.")
