from collections import deque

# Creating a deque
dll = deque()

# Adding elements to the end
dll.append('a')
dll.append('b')

# Adding elements to the beginning
dll.appendleft('z')

# Removing elements from the end
tail_element = dll.pop()

# Removing elements from the beginning
head_element = dll.popleft()

# Iterate through the deque
for elem in dll:
    print(elem)

            
def main():
    list1 = [0,4,0,3,2]
    print()


if __name__ == "__main__":
    main()