
from collections import Counter

# s1 = "ba", s2="koabjyuu"
def check_inclusion(s1, s2):
    #s1_dict = Counter(s1)
    s1_dict = {}
    for char in s1:
        s1_dict[char] = s1_dict.get(char, 0) + 1
    
    for i in range(len(s2)):


    return False


if __name__ == "__main__":
    s1 = "adc"
    s2="dcda"
    print(check_inclusion(s1, s2))