def partition(arr, low, high):
    x = low-1
    for i in range(low, high+1):
        if (arr[i] < arr[high]):
            x += 1
            arr[i], arr[x] = arr[x], arr[i]
    arr[x+1], arr[high] = arr[high], arr[x+1]
    return x+1


def quickSort(arr, low, high):
    if (low < high):
        p = partition(arr, low, high)
        quickSort(arr, low, p-1)
        quickSort(arr, p+1, high)


def main():
    arr = []
    print("\nEnter elements in array:")
    while (True):
        try:
            elem = int(input("\nEnter a number:\t"))
        except ValueError:
            break
        arr.append(elem)
    n = len(arr)
    print("\nThe Array is:")
    print(arr)
    print("\nThe sorted list is:")
    quickSort(arr, 0, n-1)
    print(arr)


if __name__ == '__main__':
    main()
