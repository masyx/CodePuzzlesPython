
# O(n) time | O(n) space
def reverse_words(sentence):
    def reverse_list(lst):
        start = 0
        end = len(lst) - 1
        while start < end:
            lst[start], lst[end] == lst[end], lst[start]
            start += 1
            end -= 1
        return lst
    
    reversed_sentence = reverse_list(list(sentence))
    start = 0
    n = len(reversed_sentence)
    result = []
    while start < n:
        if reversed_sentence[start] == " ":
            start += 1
        else:
            end = start
            while end < n and reversed_sentence[end] != " ":
                end += 1
            word = "".join(reverse_list(reversed_sentence[start:end]))
            result.append(word)
            start = end

    final_sentence = " ".join(result)
    return final_sentence




if __name__ == "__main__":
    print(reverse_words(" reverse  this string.  "))