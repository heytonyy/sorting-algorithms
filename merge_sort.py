import numpy as np


def merge_sort(numbers):
    if len(numbers) > 1:
        mid = len(numbers) // 2
        left = numbers[:mid]
        right = numbers[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                numbers[k] = left[i]
                i += 1
            else:
                numbers[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            numbers[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            numbers[k] = right[j]
            j += 1
            k += 1

    return numbers


if __name__ == "__main__":
    # X random numbers between 0 and 10000
    arr = np.random.randint(0, 10000, 100000)
    print(merge_sort(arr))
    print("Done!")
