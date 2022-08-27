def groupAnagrams(words):
    result = []
    used_idx = []
    for idx, word in enumerate(words):
        if idx not in used_idx:
            current_word_dict = create_word_dict(word)
            words_anagrams = find_word_anagrams(current_word_dict, words, idx, used_idx)
            result.append(words_anagrams)
    return result


def find_word_anagrams(main_word_dict, words, idx, used_idx):
    main_word_anagrams = [words[idx]]
    for i in range(idx + 1, len(words)):
        if is_words_anagrams(main_word_dict, words[i]):
            main_word_anagrams.append(words[i])
            used_idx.append(i)
    return main_word_anagrams
        
        
def create_word_dict(word):
    word_dict_char_count = {}
    for char in word:
        word_dict_char_count[char] = word_dict_char_count.get(char, 0) + 1
    return word_dict_char_count
        
        
def is_words_anagrams(dict_1, word):
    dict_2 = create_word_dict(word)
    for key in dict_1:
        if key not in dict_2:
            return False
        elif dict_1[key] != dict_2[key]:
            return False
    return True

def main():
    # ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
    words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
    print(groupAnagrams(words))
    
    
if __name__ == "__main__":
    main()