# O(w * n * log(n)) time | O(w * n) space, where 'w' is number of words, 
# 'n' is the length of the longest word
def groupAnagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return list(anagrams.values())


def main():
    # ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
    words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
    print(groupAnagrams(words))
    
    
if __name__ == "__main__":
    main()