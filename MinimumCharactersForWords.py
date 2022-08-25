def minimumCharactersForWords(words):
    total_chars = {}
    for word in words:
        curr_chars = {}
        for char in word:
            if char not in curr_chars:
                curr_chars[char] = 0
            curr_chars[char] += 1
        compare_chars(curr_chars, total_chars)
    return dict_to_array(total_chars)


def compare_chars(curr_chars, total_chars):
    for key in curr_chars:
        if key in total_chars:
            if curr_chars[key] > total_chars[key]:
                total_chars[key] = curr_chars[key]
        else:
            total_chars[key] = curr_chars[key]
            
def dict_to_array(dict):
    array = []
    for key, value in dict.items():
        for _ in range(value):
            array.append(key)
    return array

def main():
    words = ["this", "that", "did", "deed", "them!", "a"]
    #words = ["did", "deed"]
    print(minimumCharactersForWords(words))
    
    
if __name__ == "__main__":
    main()