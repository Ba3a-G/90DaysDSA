class Node():
    dataType = "A node object with link to next node"

    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode

class LinkedList():
    dataType = "Linked list"

    def __init__(self, **kwargs):
        self.headNode = None

        if kwargs.get('data'):
            data = kwargs.get('data')
            if type(data) == str or type(data) == int:
                LinkedList.append(self, data)
            elif type(data) == list or type(data) == tuple:
                for i in data:
                    LinkedList.append(self, i)

    def printItems(self):
        if self.headNode == None:
            print(f"Empty linked list")
            return

        selectedNode = self.headNode
        while selectedNode.nextNode != None:
            print(selectedNode.data)
            selectedNode = selectedNode.nextNode
        print(selectedNode.data)

    def append(self, data):
        if self.headNode == None:
            node = Node(data, None)
            self.headNode = node
            return

        tailNode = self.headNode
        
        while tailNode.nextNode != None:
            tailNode = tailNode.nextNode

        tailNode.nextNode = Node(data, None)

if __name__ == "__main__":
    ll = LinkedList()
    print("I just created a linked list.")
    ll.printItems()