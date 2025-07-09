def GetData():
    arr = []
    
    try:
        while True:
            arr_length = int(input("Enter the Length of Array = "))
            if arr_length > 0:
                try:
                    print("Enter elements in the array:")
                    for i in range(arr_length):
                        val = int(input(f"Element {i+1}: "))
                        arr.append(val)
                    print("Array =", arr)
                    break
                except:
                    print("Enter numerical values only.")
            else:
                print("Length must be a positive number.")
        return arr
    except:
        print("Enter only numerical values.")


def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in nums:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest = max(longest, current_streak)

    return longest

if __name__ == "__main__":
    nums = GetData()
    if nums:
        result = longestConsecutive(nums)
        print("\nLength of Longest Consecutive Sequence:", result)