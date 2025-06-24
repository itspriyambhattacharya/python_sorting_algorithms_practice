def merge(arr, low, mid, high):
    n1, n2 = mid-low+1, high-mid
    l1 = []
    l2 = []

    l1 = arr[low:mid+1]
    l2 = arr[mid+1:high+1]
    i, j, k = 0, 0, low
    while (i < n1 and j < n2):
        if (l1[i] <= l2[j]):
            arr[k] = l1[i]
            k += 1
            i += 1
        else:
            arr[k] = l2[j]
            k += 1
            j += 1

    while (i < n1):
        arr[k] = l1[i]
        i += 1
        k += 1

    while (j < n2):
        arr[k] = l2[j]
        j += 1
        k += 1


def mergeSort(arr, low, high):
    if (low < high):
        mid = (high-low)//2 + low
        mergeSort(arr, low, mid)
        mergeSort(arr, mid+1, high)
        merge(arr, low, mid, high)


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
    mergeSort(arr, 0, n-1)
    print(arr)


if __name__ == '__main__':
    main()
