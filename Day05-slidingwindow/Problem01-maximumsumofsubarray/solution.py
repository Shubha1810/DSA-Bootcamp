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

def Slidingwindow(array,num_elements):
    try:

        k =int(input("Enter the target:"))
        if k > num_elements:
            return "Window size k is larger than the array length."
        
        max_sum = sum(array[:k])

        
        for i in range(k, num_elements):
            max_sum = max_sum - array[k-i]
            return max_sum 

        print("sum = ",max_sum)

    except ValueError:
        return "Invalid input for window size k. Please enter a number."




array, num_elements = GetData()
result = Slidingwindow(array, num_elements)
print(result)





