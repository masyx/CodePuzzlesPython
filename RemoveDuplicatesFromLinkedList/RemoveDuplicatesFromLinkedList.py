class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
        
def removeDuplicatesFromLinkedListBruteForce(linkedList):
    used = {}
    currentNode = linkedList
    previous = None
    while currentNode != None:
        if currentNode.value in used:
            previous.next = currentNode.next
            currentNode = currentNode.next
            continue
        else:
            used[currentNode.value] = True
        previous = currentNode
        currentNode = currentNode.next
    return linkedList      




def main():
    head = LinkedList(1)
    head.next = LinkedList(1)
    head.next.next = LinkedList(3)
    head.next.next.next = LinkedList(4)
    head.next.next.next.next = LinkedList(4)
    head.next.next.next.next.next = LinkedList(5)
    head.next.next.next.next.next.next = LinkedList(6)
    head.next.next.next.next.next.next.next = LinkedList(6)
    print(removeDuplicatesFromLinkedList(head))
    
if __name__ == "__main__":
    main()