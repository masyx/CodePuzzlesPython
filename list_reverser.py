class ListReverser:
    # O(n) time
    # O(n) space
    @staticmethod
    def reverse_list_static(list):
        l = 0
        r = len(list) - 1
        while l < r:
            list[l], list[r] = list[r], list[l]
            l += 1
            r -= 1
    
    def __init__(self, list):
        self.list = list
        
    def reverse_list_instance(self):
        return self.reverse_list_static(self.list)
    
    
    

def main():
    my_list = [1, 3, 5, 'seven']
    ListReverser.reverse_list_static(my_list)
    print(my_list)
    re = ListReverser(my_list)
    re.reverse_list_instance()
    print(my_list)


if __name__ == "__main__":
    main()