# Algorithm Binary Search


def binarySearch(myArr, item):
    low = 0
    high = len(myArr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_numb = myArr[mid]

        if mid_numb == item:
            return mid
        elif mid_numb > item:
            high = mid - 1
        elif mid_numb < item:
            low = mid + 1

    return None

def main():
    my_list = [int(numb) for numb in input().split()]
    number = int(input())

    print(binarySearch(my_list, number))


if __name__ == '__main__':
    main()