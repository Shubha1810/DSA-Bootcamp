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

def Sumzero(array,num_elements):
    
    for k in range(num_elements):
        if (array[k]==0):
            print(True)
            break

    else:
        for j in range(num_elements):
            for i in range(j+1,num_elements):
                temp = 0
                for k in range(j, i):
                    temp += array[k]
                if (temp == 0):
                    print(array[j:i])
                    print(True)
                    return
        else:
            print(False)



array, num_elements = GetData()
Sumzero(array, num_elements)





