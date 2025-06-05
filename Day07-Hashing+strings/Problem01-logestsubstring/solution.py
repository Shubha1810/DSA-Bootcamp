def GetData():
        
    input_str1 = input("Enter the String: ").lower()
    s1 = list(input_str1)
    
    return s1

        
def Rem_Duplicates(s1):
    
        for j in range(len(s1)):
            for k in range(len(s1)-1):
                if (s1[k]>s1[k+1]):
                    s1[k], s1[k + 1] = s1[k + 1], s1[k]

        unique_arr = []

        for i in range(len(s1)):
            is_duplicate = False
            for j in range(i):
                if s1[i] == s1[j]:
                    is_duplicate = True
                    break
            if not is_duplicate:
                unique_arr.append(s1[i])

        
        print("Longest Subtring without Repeating Characters = ",len(unique_arr))

s1 = GetData()
Rem_Duplicates(s1)