def get_strings():
    try:
        str1 = input("Enter string: ").lower()
        return str1
    except Exception as e:
        print("An error occurred:", e)
        exit()

def longest_palindromic_String(str1):
    max_len = 0
    result = ""

    for i in range(len(str1)):
        # Odd-length palindrome (centered at i)
        left, right = i, i
        while left >= 0 and right < len(str1) and str1[left] == str1[right]:
            if (right - left + 1) > max_len:
                max_len = right - left + 1
                result = str1[left:right+1]
            left -= 1
            right += 1

        # Even-length palindrome (centered between i and i+1)
        left, right = i, i + 1
        while left >= 0 and right < len(str1) and str1[left] == str1[right]:
            if (right - left + 1) > max_len:
                max_len = right - left + 1
                result = str1[left:right+1]
            left -= 1
            right += 1

    return result

s1 = get_strings()
print("Longest Palindromic Substring:", longest_palindromic_String(s1))
