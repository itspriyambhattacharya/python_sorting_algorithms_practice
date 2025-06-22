def display(arr):
    for element in arr:
        print(element, end='\t')
    print()


# Heapify a subtree rooted at index i
def heapify(arr, n, i):
    largest = i
    lc = (2 * i) + 1
    rc = (2 * i) + 2

    if lc < n and arr[lc] > arr[largest]:
        largest = lc

    if rc < n and arr[rc] > arr[largest]:
        largest = rc

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Step 1: Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap max to end
        heapify(arr, i, 0)  # Heapify the reduced heap


def main():
    lst = []

    print("Enter elements in array:\n")
    while (True):
        try:
            elem = int(input("\nEnter a number:\t"))
        except ValueError:
            break
        lst.append(elem)
    n = len(lst)
    print("\nThe Array is:")
    print(lst)
    print("\nThe sorted list is:")
    heapSort(lst)
    print(lst)


if __name__ == "__main__":
    main()
