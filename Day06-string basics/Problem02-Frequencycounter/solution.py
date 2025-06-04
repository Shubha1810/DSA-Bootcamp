def GetData():
    array = []
    
    try:
        while True:
            num_elements = int(input("Enter the Length of Array = "))
            if num_elements > 1:
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
        
def Frequency_Counter(array, num_elements):
        counter = {}
    
        for i in range(num_elements):
            if array[i] not in counter: 
                count = 1
                for j in range(i+1,num_elements):
                    if array[i] == array[j]:
                        count = count + 1

                counter[array[i]] = count

        print("Frequncy Number= ",counter)
        
array,num = GetData()
Frequency_Counter(array, num)

