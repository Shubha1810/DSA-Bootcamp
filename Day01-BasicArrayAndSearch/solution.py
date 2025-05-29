def binarysearch():
    # to find the exact length of array
    n = int(input("Enter the number of elements in array: "))
    arr = []
    for i in range(n):
        element = int(input())
        arr.append(element)
        
    # sorting it
    arr.sort()
    print("Sorted array:", arr)  
    
    # finding the targeted value
    target = int(input("Enter the target value to search: "))

    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            print("Target found at index:", mid)
            return mid
        
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    print("Target not found in array.")
    return -1

result = binarysearch()
