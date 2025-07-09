def GetData():
    arr = []
    try:
        while True:
            try:
                arr_length = int(input("Enter the Length of Array = "))
                if arr_length > 1:
                    print("Enter elements in the array:")
                    for i in range(arr_length):
                        while True:
                            try:
                                val = int(input(f"Element {i+1}: "))
                                arr.append(val)
                                break
                            except ValueError:
                                print("Invalid input. Please enter an integer.")
                    print("Array =", arr)
                    return arr, arr_length
                else:
                    print("Length must be a positive number and greater than 1. Please try again.")
            except ValueError:
                print("Enter a valid integer for array length.")
    except Exception as e:
        print("Unexpected error occurred:", e)
        return [], 0


def majorityElement(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate

if __name__ == "__main__":
    nums, length = GetData()
    if nums and length > 0:
        result = majorityElement(nums)
        print("\nMajority Element is:", result)
    else:
        print("Failed to get valid input.")
