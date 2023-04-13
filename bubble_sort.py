import numpy as np
from tqdm import tqdm


def bubble_sort(numbers):
    for i in tqdm(range(len(numbers))):
        for j in range(len(numbers)-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


if __name__ == "__main__":
    # X random numbers between 0 and 10000
    arr = np.random.randint(0, 10000, 10000)
    print(bubble_sort(arr))
    print("Done!")
