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


def count_frequencies(array):
    frequency = {}  # Dictionary to store element: count
    
    for i in range(num_elements):
        if array[i] not in frequency:
            count = 1
        for j in range(i + 1, num_elements):
            if array[i] == array[j]:
                count += 1
        frequency[array[i]] = count  # Store count in dictionary

    print("\nFrequencies of elements:", frequency)

array, num_elements = GetData()
count_frequencies(array)

