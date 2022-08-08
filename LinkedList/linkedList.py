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
    
    def extend(self, data):
        n = len(data)
        if n < 1:
            return 
        tempHeadNode = tempTailNode = Node(data[0], None)
        for i in data[1:]:
            tempTailNode.nextNode = Node(i, None)
            tempTailNode = tempTailNode.nextNode

        if self.headNode == None:
            self.headNode = tempHeadNode
            return

        tailNode = self.headNode
        while tailNode.nextNode != None:
            tailNode = tailNode.nextNode

        tailNode.nextNode = tempHeadNode

    def insertAfterValue(self, dataAfter, dataToInsert):
        tailNode = self.headNode
        while tailNode.nextNode != None or tailNode.data == dataAfter:
            tailNode = tailNode.nextNode
        nodeAfterNewNode = tailNode.nextNode

        tailNode.nextNode = Node(dataToInsert, nodeAfterNewNode)


            

if __name__ == "__main__":
    ll = LinkedList(data = [2, 34])
    print("I just created a linked list.")
    ll.printItems()
    ll.extend([56])
    ll.printItems()