def bubbleSort(arr, n):
    low, high = 0, n-1

    for i in range(0, n-1):
        fl = False
        for j in range(0, n-i-1):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                fl = True

        if (fl == False):
            break


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
    bubbleSort(arr, n)
    print(arr)


if __name__ == '__main__':
    main()
