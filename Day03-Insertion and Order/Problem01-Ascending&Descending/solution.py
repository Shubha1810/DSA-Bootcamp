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


def SelectionsortingAscending(array, num_elements):
    try:
        for index in range(num_elements):
            min = index
            for j in range(index+1, num_elements):
                if (array[j] < array[min]):
                    min = j

                    temp = array[index]
                    array[index] = array[min]
                    array[min] = temp

        print("Sorted Arrayin Ascending Order is:", array)
        return array
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

def SelectionsortingDescending(array, num_elements):
    try:
        for index in range(num_elements):
            max = index
            for j in range(index+1, num_elements):
                if (array[j] > array[max]):
                    max = j

                    temp = array[index]
                    array[index] = array[max]
                    array[max] = temp

        print("Sorted Array in Descending Order is:", array)
        return array
    except ValueError:
        print("Invalid input. Please enter a numerical value.")


# Run the program
array, num_elements = GetData()
SelectionsortingAscending(array, num_elements)
SelectionsortingDescending(array, num_elements)


