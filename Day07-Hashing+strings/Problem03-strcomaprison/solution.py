def GetData():
    try:
        s = input("Enter the string: ")
        return s
    except ValueError:
        print("Invalid input. Please enter a string with characters.")
        exit()


def compress_string(s):
    comparison = []
    n = len(s)
    i = 0

    while i < n:
        count = 1
        current_char = s[i]

       
        while i + 1 < n and s[i] == s[i + 1]:
            count += 1
            i += 1

        comparison.append(current_char)
        if count > 1:
            comparison.append(str(count))

        i += 1

  
    compressed = ''.join(comparison)
    print("Compressed String:", compressed)
    return compressed



user_input = GetData()
compress_string(user_input)

