def get_strings():
    try:
        str1 = input("Enter string 1: ")
        str2 = input("Enter string 2: ")

        if not str1 or not str2:
            print("Error: Both strings must be non-empty.")
            exit()

        sorted_str1 = sorted(str1.lower())
        sorted_str2 = sorted(str2.lower())

        print("String 1 after sorting:", sorted_str1)
        print("String 2 after sorting:", sorted_str2)

        return sorted_str1, sorted_str2
    except Exception as e:
        print("An error occurred")
        exit()

def is_anagram(str1, str2):
    if str1 == str2:
        return True
    else:
        return False



s1, s2 = get_strings()
print(is_anagram(s1, s2))
