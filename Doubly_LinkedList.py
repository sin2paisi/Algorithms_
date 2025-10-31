# ------------------------------------------
# Doubly Linked List Implementation in Python
# ------------------------------------------

# Node class represents a single node in the doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# DoublyLinkedList class encapsulates all operations
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head

        if self.head:
            self.head.prev = new_node

        self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    # Insert after a specific node value
    def insert_after(self, target_data, data):
        current = self.head
        while current and current.data != target_data:
            current = current.next

        if not current:
            print(f"Node with value {target_data} not found!")
            return

        new_node = Node(data)
        new_node.next = current.next
        new_node.prev = current

        if current.next:
            current.next.prev = new_node

        current.next = new_node

    # Delete a node by value
    def delete_node(self, key):
        current = self.head

        # If list is empty
        if not current:
            print("List is empty!")
            return

        # If head node is to be deleted
        if current.data == key:
            self.head = current.next
            if self.head:
                self.head.prev = None
            current = None
            return

        # Otherwise, search for the node
        while current and current.data != key:
            current = current.next

        if not current:
            print(f"Node with value {key} not found!")
            return

        # Adjust pointers
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next

        current = None

    # Search for a node
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    # Display the list (forward)
    def display_forward(self):
        current = self.head
        if not current:
            print("List is empty!")
            return

        print("Forward Traversal:")
        while current:
            print(current.data, end=" <-> " if current.next else "")
            current = current.next
        print()

    # Display the list (backward)
    def display_backward(self):
        current = self.head
        if not current:
            print("List is empty!")
            return

        # Go to the last node
        while current.next:
            current = current.next

        print("Backward Traversal:")
        while current:
            print(current.data, end=" <-> " if current.prev else "")
            current = current.prev
        print()

    # Find the length of the list
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


# ------------------------------------------
# Example Usage
# ------------------------------------------
if __name__ == "__main__":
    dll = DoublyLinkedList()

    # Insert elements
    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)
    dll.insert_at_beginning(5)
    dll.insert_after(20, 25)

    dll.display_forward()
    dll.display_backward()

    # Delete a node
    dll.delete_node(10)
    print("\nAfter deleting 10:")
    dll.display_forward()

    # Search operation
    print("\nSearching for 25:", dll.search(25))
    print("Searching for 100:", dll.search(100))

    # Length of the list
    print("\nLength of the list:", dll.length())
