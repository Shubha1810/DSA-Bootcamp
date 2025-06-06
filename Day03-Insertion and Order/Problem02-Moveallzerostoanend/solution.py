def GetData():
    array = []
    
    try:
        while True:
            num_elements = int(input("Enter the Length of Array = "))
            if num_elements> 1:
                try:
                    print("Enter elements in the array:\n")
                    for i in range(num_elements):
                        val = int(input())
                        array.append(val)
                    print("Array =", array)
                    break
                except:
                    print("Enter Numerical values only")
            else:
                print("Length must be a positive number and greater than 1. Please try again.")
            
        return array, num_elements

    except:
        print("Enter only numerical values")
        
def Moveallzerostoend(array, num_elements):
    non_zero_index = 0
    

    for i in range(num_elements):
        if(array[i] != 0):
            array[non_zero_index] = array[i]
            non_zero_index += 1

    #print("first loop array=")

    for i in range(non_zero_index, num_elements): 
        #if(array[i] == 0):
        array[i] = 0
            
            # zero_index = array[i]
            # array[zero_index] = 0
            #zero_index -= 1

                    
    print("After modification Array= ",array)

array, num_elements = GetData()
Moveallzerostoend(array, num_elements)
