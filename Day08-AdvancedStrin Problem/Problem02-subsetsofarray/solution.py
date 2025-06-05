def get_input():
    try:
        user_input = input("Enter elements separated by space: ")
        elements = user_input.strip().split()
        return elements
    except Exception as e:
        print("Invalid input:", e)
        return []

def generate_subsets_recursive(nums):
    result = []

    def backtrack(start, path):
        result.append(path[:])  
        for i in range(start, len(nums)):
            path.append(nums[i])      
            backtrack(i + 1, path)     
            path.pop()             


    backtrack(0, [])
    return result


arr = get_input()
subsets = generate_subsets_recursive(arr)
print("All Subsets (Power Set):", subsets)
