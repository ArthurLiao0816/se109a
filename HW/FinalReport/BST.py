# 定義節點
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# 定義二元搜尋樹
class BST:
    def __init__(self):
        self.root = None

    def deleteTree(self):
        self.root = None

    def insert(self, data):
        self.root = self.__insert(self.root, data)

    def __insert(self, node, data):
        if node == None:
            node = Node(data)
        else:
            if node.data > data:
                node.left = self.__insert(node.left, data)
            elif node.data < data:
                node.right = self.__insert(node.right, data)
            else:
                print('<%s> already exists in the tree' % data)
                pass
        return node

    def delete(self, data):
        self.root = self.__delete(self.root, data)

    def __delete(self, node, data):
        if node == None:
            print("<%s> dosen't exist in the tree" % data)
        else:
            if node.data > data:
                node.left = self.__delete(node.left, data)
            elif node.data < data:
                node.right = self.__delete(node.right, data)
            else:
                if not node.right and not node.left:
                    node = None
                elif (node.right and node.left) or node.left:
                    max_left_child = self.__Max(node.left)
                    node = self.__delete(node, max_left_child)
                    node.data = max_left_child
                else:
                    node = node.right
        return node

    def __Max(self, node):
        if node.right == None:
            return node.data
        else:
            return self.__Max(node.right)

    def search(self, data):
        return self.__search(self.root, data)

    def __search(self, node, data):
        if node != None:
            if node.data > data:
                return self.__search(node.left, data)
            elif node.data < data:
                return self.__search(node.right, data)
            else:
                return node
        else:
            print("<%s> dosen't exist in the tree" % data)

    def preorder(self):
        rlt = []
        self.__preorder(self.root, rlt)
        print('preorder = ', rlt)
        return rlt

    def __preorder(self, node, List):
        if node == None:
            return
        else:
            List.append(node.data)
            self.__preorder(node.left, List)
            self.__preorder(node.right, List)
        return

    def inorder(self):
        rlt = []
        self.__inorder(self.root, rlt)
        print('inorder = ', rlt)
        return rlt

    def __inorder(self, node, List):
        if node == None:
            return
        else:
            self.__inorder(node.left, List)
            List.append(node.data)
            self.__inorder(node.right, List)
        return

    def postorder(self):
        rlt = []
        self.__postorder(self.root, rlt)
        print('postorder = ', rlt)
        return rlt

    def __postorder(self, node, List):
        if node == None:
            return
        else:
            self.__postorder(node.left, List)
            self.__postorder(node.right, List)
            List.append(node.data)
        return
