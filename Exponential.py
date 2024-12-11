def binary_search(arr, low, high, target):

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  
def exponential_search(arr, target):

    if arr[0] == target:
        return 0

  
    index = 1
    while index < len(arr) and arr[index] <= target:
        index *= 2


    return binary_search(arr, index // 2, min(index, len(arr) - 1), target)

# Example usage
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
target = int(input("Enter the number to search: "))

index = exponential_search(array, target)

if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the array.")
