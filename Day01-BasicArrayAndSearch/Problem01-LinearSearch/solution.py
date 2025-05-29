#to find the exact length of array
n = int(input("enter the number of elements in array:"))
arr = []

#setting target value as 3(u can set any target value)
#target = 3
target = int(input("enter the target value needed to search:"))

#to take input in array
def linearsearch():
    for i in range(0,n):
        element = int(input())
        arr.append(element)
        
        if(arr[i] == target):
            print("Index is ",arr[i])
            
    #if element not found
    return -1

# calling the function
result = linearsearch()

if(result == -1):
    print("Index" ,result)

print(arr)






