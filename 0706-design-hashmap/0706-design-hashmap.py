class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:
    def __init__(self):
        self.head = None

    def put(self, key: int, val: int) -> None:

        # Check if key already exists
        temp = self.head

        while temp != None:
            if temp.key == key:
                temp.val = val
                return
            temp = temp.next

        # Key doesn't exist, create new node
        newNode = Node(key, val)

        if self.head == None:
            self.head = newNode
        else:
            temp = self.head

            while temp.next != None:
                temp = temp.next

            temp.next = newNode

    def get(self, key: int) -> int:

        temp = self.head

        while temp != None:
            if temp.key == key:
                return temp.val

            temp = temp.next

        return -1

    def remove(self, key: int) -> None:

        # If key is at head
        if self.head != None and self.head.key == key:
            self.head = self.head.next
            return

        temp = self.head

        while temp != None and temp.next != None:

            if temp.next.key == key:
                temp.next = temp.next.next
                return

            temp = temp.next