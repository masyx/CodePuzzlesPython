# O(n * l) time | O(k) space, where 'n' is the number of words in the array, and 'l' is
# the length of the longest word. 'k' is the number of unique characters
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



def minimum_characters_for_words(words):
    main_map = {}
    result = []
    for word in words:
        temp_map = {}
        for char in word:
            if char not in main_map:
                main_map[char] = main_map.get(char, 0) + 1
                result.append(char)
            temp_map[char] = temp_map.get(char, 0) + 1
            if temp_map[char] > main_map[char]:
                result.append(char)
                main_map[char] += 1
    return result

def main():
    #words = ["this", "that", "did", "deed", "them!", "a"]
    words = ["did", "deed"]
    print(minimum_characters_for_words(words))
    
    
if __name__ == "__main__":
    main()