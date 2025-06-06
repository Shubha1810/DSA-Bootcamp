def GetData():
    array = []
    while True:
        try:
            num_elements = int(input("Enter the number of elements in array: "))
            if num_elements > 1:
                for i in range(num_elements):
                    while True:
                        try:
                            element = int(input(f"Enter element {i+1}: "))
                            array.append(element)
                            break
                        except ValueError:
                            print("Enter a valid integer.")
                print("Array =", array)
                return array, num_elements
            else:
                print("Number of elements must be greater than 1. Try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def KadaneAlgo(array):
    max_current = max_global = array[0]
    for i in range(1, len(array)):
        max_current = max(array[i], max_current + array[i])
        max_global = max(max_current, max_global)
    return max_global


# Main Execution
array, num_elements = GetData()
print("Maximum subarray sum using Kadane's Algorithm:", KadaneAlgo(array))
