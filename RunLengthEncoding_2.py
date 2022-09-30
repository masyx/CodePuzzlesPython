# Problem: Compress a string such that 'AAABCCDDDD' becomes 'A3BC2D4'. 
# Only compress the string if it saves space.

def runLengthEncoding(string):
    if not string:
        return string
    result = ''
    prev_char = string[0]
    count = 0
    for char in string:
        if char == prev_char:
            count += 1
        else:
            result += f"{(str(count) if count > 1 else '') + prev_char}"
            prev_char = char
            count = 1
    result += f"{(str(count) if count > 1 else '') + prev_char}"
    return result if len(result) < len(string) else string

def runLengthEncoding_2(string):
    if not string:
        return string
    result = []
    prev_char = string[0]
    count = 0
    for char in string:
        if char == prev_char:
            count += 1
        else:
            result.append(f"{(str(count) if count > 1 else '') + prev_char}")
            prev_char = char
            count = 1
    result.append(f"{(str(count) if count > 1 else '') + prev_char}")
    return ''.join(result) if len(result) < len(string) else string


def main():
    string = '.............______=========AAAA   AAABBBB   BBB'
    print(runLengthEncoding(string))
    print(runLengthEncoding_2(string))
    
if __name__ == "__main__":
    main()