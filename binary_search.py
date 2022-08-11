import random


def binary_search(data, target, low, high):
    if low > high:
        return False
    
    mid = (low + high) // 2
    
    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search(data, target, low, mid - 1)
    else:
        return binary_search(data, target, mid + 1, high)


def binary_search_with_while(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target >= data[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False


if __name__ == '__main__':
    data = [random.randint(0,100) for i in range(10)]
    
    data.sort()
    
    print(data)
    
    target = int(input("What number would you like to find? "))
    #found = binary_search(data, target, 0, len(data) - 1)
    found = binary_search_with_while(data, target)
    
    print(found, target)