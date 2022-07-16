class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n log n) time | O(k) space        
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

# O(n) time | O(1) space
def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList
    while currentNode is not None:
        nextNode = currentNode.next
        while nextNode is not None and currentNode.value == nextNode.value:
            nextNode = nextNode.next

        currentNode.next = nextNode
        currentNode = nextNode
        
    return linkedList




def main():
    # 1 -> 1 -> 3 -> 4 -> 4 -> 5 -> 6 -> 6
    head = LinkedList(1)
    head.next = LinkedList(1)
    head.next.next = LinkedList(3)
    head.next.next.next = LinkedList(4)
    head.next.next.next.next = LinkedList(4)
    head.next.next.next.next.next = LinkedList(5)
    head.next.next.next.next.next.next = LinkedList(6)
    head.next.next.next.next.next.next.next = LinkedList(6)
    head.next.next.next.next.next.next.next.next = LinkedList(6)
    ll = removeDuplicatesFromLinkedList(head)
    print()
    
if __name__ == "__main__":
    main()