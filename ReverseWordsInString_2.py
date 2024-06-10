
# O(n) time | O(n) space
def reverse_words(sentence):
    
    def reverse(s):
        start = 0
        end = len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return s
    
    # Step 1: Reverse the entire string
    s = reverse(list(sentence))

    # Step 2: Reverse each word individually
    result = []
    start = 0
    n = len(s)

    while start < n:
        if s[start] != ' ':
            end = start
            while end < n and s[end] != ' ':
                end += 1
            # Extract the word and reverse it
            word = reverse(s[start:end])
            result.append("".join(word))
            start = end
        else:
            start += 1

    final_sentence = ' '.join(result)
    return final_sentence




if __name__ == "__main__":
    print(reverse_words(" reverse  this string.  "))