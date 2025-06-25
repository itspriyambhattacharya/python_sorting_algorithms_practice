def insertionSort(arr, n):
    low, high = 0, n-1
    for i in range(low+1, high+1):
        j = i
        while (j > low and arr[j] < arr[j-1]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    pass


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
    insertionSort(lst, n)
    print(lst)


if __name__ == '__main__':
    main()
