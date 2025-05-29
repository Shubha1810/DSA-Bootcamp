def GetData():
    array = []
    try:
        while True:
            num_elements = int(input("Enter the number of elements in array: "))
            if num_elements > 0:
                try:
                    for i in range(num_elements):
                        element = int(input("Enter elements in array:"))
                        array.append(element)
                    print("Array =", array)
                    break
                except ValueError:
                    print("Enter numerical values only for array elements.")
            else:
                print("Number of elements must be greater than 0. Try again.")
        return array, num_elements
    except ValueError:
        print("Invalid input. Please enter only integers.")
        exit()


def BinarySearch(array, num_elements):
    try:
        array.sort()
        print("Sorted array:", array)

        target = int(input("Enter the target value to search: "))

        start = 0
        end = num_elements - 1

        while start <= end:
            mid = (start + end) // 2
            if array[mid] == target:
                print("Index =", mid)
                break
            elif array[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        else:
            print("Index = -1")
    except ValueError:
        print("Invalid input. Please enter a valid target number.")


array, num_elements = GetData()
BinarySearch(array, num_elements)
