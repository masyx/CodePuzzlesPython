# O(n) time | O(1) space
def find_key(given_dict, given_value):
    for key, value in given_dict.items():
        if value == given_value:
            return key
    return None

def main():
    my_dict = {'key1':"aaa", 'key2': "bbb", 'key3': "aaa"}
    key = find_key(my_dict, "aaa")
    print(key)
    
    keys = [k for k, v in my_dict.items() if v == 'aaa']
    print(keys)
    
    

if __name__ == "__main__":
    main()