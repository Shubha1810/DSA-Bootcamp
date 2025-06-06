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


def LinearSearch(array, num_elements):
    try:
        target = int(input("Enter the target value needed to search: "))
        for index in range(num_elements):
            if array[index] == target:
                print("Index =", index)
                break
        else:
            print("Index = -1")
    except ValueError:
        print("Invalid input. Please enter a numerical target value.")


# Run the program
array, num_elements = GetData()
LinearSearch(array, num_elements)
