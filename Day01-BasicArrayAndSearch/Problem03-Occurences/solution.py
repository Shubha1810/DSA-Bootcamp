def GetData():
    array = []
    try:
        while True:
            num_elements = int(input("Enter the number of elements in array: "))
            if num_elements > 0:
                try:
                    for i in range(num_elements):
                        element = int(input("Enter the element:"))
                        array.append(element)
                    print("Array entered:", array)
                    break
                except ValueError:
                    print("Enter numerical values only for array elements.")
            else:
                print("Number of elements must be greater than 0. Try again.")
        return array, num_elements
    except ValueError:
        print("Invalid input. Please enter only integers.")
        exit()


def CountTargetOccurrences(array, num_elements):
    try:
        target = int(input("Enter the target number to count: "))
        count = 0
        for num in array:
            if num == target:
                count += 1
        print("Count:", count)
        return count
    except ValueError:
        print("Invalid input. Please enter a valid target number.")
        return 0


# Run the program
array, num_elements = GetData()
CountTargetOccurrences(array, num_elements)
