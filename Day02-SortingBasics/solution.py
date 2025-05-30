def GetData():
    array = []
    try:
        while True:
            num_elements = int(input("Enter the number of elements in array: "))
            if num_elements > 1:
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


def Bubblesorting(array, num_elements):
    try:
        for index in range(num_elements):
            swapped = False
            for j in range(0, num_elements-index-1):
                if array[j] > array[j+1]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
                    swapped = True
            if not swapped:
                break
        print("Sorted Array is:", array)   
        return array
    except ValueError:
        print("Invalid input. Please enter a numerical value.")


# Run the program
array, num_elements = GetData()
Bubblesorting(array, num_elements)
