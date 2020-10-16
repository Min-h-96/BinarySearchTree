class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.insertNode(self.root, data)

    def insertNode(self, currentNode, data):
        if data > currentNode.data:
            if currentNode.right:
                self.insertNode(currentNode.right, data)
            else:
                currentNode.right = Node(data)
        else:
            if currentNode.left:
                self.insertNode(currentNode.left, data)
            else:
                currentNode.left = Node(data)

    def print(self):
        print('루트 노드:', self.root.data)
        self.printChild(self.root)

    def printChild(self, currentNode):
        if currentNode.right:
            print(currentNode.data, '의 오른쪽 자식 노드 :', currentNode.right.data)
            self.printChild(currentNode.right)
        if currentNode.left:
            print(currentNode.data, '의 왼쪽 자식 노드 :', currentNode.left.data)
            self.printChild(currentNode.left)


if __name__ == "__main__":
    arr = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

    bst = BinarySearchTree()
    for i in arr:
        bst.insert(i)
    bst.print()
