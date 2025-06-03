def GetData():
    arr = []
    
    try:
        while True:
            arr_length = int(input("Enter the Length of Array = "))
            if arr_length > 1:
                try:
                    print("Enter elements in the array:\n")
                    for i in range(arr_length):
                        val = int(input())
                        arr.append(val)
                    print("Array =", arr)
                    break
                except:
                    print("Enter Numerical values only")
            else:
                print("Length must be a positive number and greater than 1. Please try again.")
            
        return arr, arr_length

    except:
        print("Enter only numerical values")
        
def TwoSum(arr, arr_length):
        try:
           
            target_value = int(input("Enter the Target Value = "))
            for j in range(arr_length):
                for k in range(j+1,arr_length):
                    if (target_value == (arr[j]+arr[k])):
                        print(True)
                        return
            else:
                print(False)
        
        except:
            print("Type only numerical values")

arr, arr_length = GetData()
TwoSum(arr, arr_length)