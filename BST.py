class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        # 루트 노드가 존재하지 않으면 루트 노드 생성
        if self.root == None:
            self.root = Node(data)
        else:
            self.insertNode(self.root, data)

    def insertNode(self, currentNode, data):
        # insert하고자 하는 값이 현재 노드의 값보다 크면 오른쪽
        if data > currentNode.data:
            # 오른쪽 자식 노드가 존재하면 재귀 호출
            if currentNode.right:
                self.insertNode(currentNode.right, data)
            else:
                currentNode.right = Node(data)
        # insert하고자 하는 값이 현재 노드의 값보다 작으면 왼쪽
        else:
            # 왼쪽 자식 노드가 존재하면 재귀 호출
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

    def search(self, data):
        # 찾고자 하는 값이 있으면 True, 없으면 False
        if self.searchNode(self.root, data) is False:
            return False
        else:
            return True

    def searchNode(self, currentNode, data):
        # 찾고자 하는 값이 현재 노드의 값과 비교해서 찾기
        if currentNode is None:
            return False
        else:
            if data == currentNode.data:
                return True
            elif data > currentNode.data:
                return self.searchNode(currentNode.right, data)
            else:
                return self.searchNode(currentNode.left, data)


if __name__ == "__main__":
    arr = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

    bst = BinarySearchTree()
    for i in arr:
        bst.insert(i)
    bst.print()
    print(bst.search(45))
    print(bst.search(35))
