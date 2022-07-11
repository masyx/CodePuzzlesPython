class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
        
def removeDuplicatesFromLinkedList(linkedList):
    return 




def main():
    head = LinkedList(1)
    head.next = LinkedList(1)
    head.next.next = LinkedList(3)
    head.next.next.next = LinkedList(4)
    head.next.next.next.next = LinkedList(4)
    head.next.next.next.next.next = LinkedList(5)
    head.next.next.next.next.next.next = LinkedList(6)
    head.next.next.next.next.next.next.next = LinkedList(6)
    print(removeDuplicatesFromLinkedList())
    
if __name__ == "__main__":
    main()