from BST import BST, Node


def insertTest():
    bst = BST()

    bst.insert(1)
    assert bst.root.data == 1, 'fail to insert data into an empty tree'
    bst.insert(2)
    assert bst.root.right.data == 2, 'fail to insert data into right subtree'
    bst.insert(-1)
    assert bst.root.left.data == -1, 'fail to insert data into left subtree'
    bst.deleteTree()

    print("insert test pass!")


def deleteTest():
    bst = BST()

    bst.insert(0)
    bst.delete(0)
    assert bst.root == None, 'fail to delete data while left and right nodes aren\'t extant'
    bst.deleteTree()

    bst.insert(0)
    bst.insert(1)
    bst.delete(0)
    assert bst.root.data == 1, 'fail to delete data while only right node exists'
    bst.deleteTree()

    bst.insert(0)
    bst.insert(-1)
    bst.delete(0)
    assert bst.root.data == -1, 'fail to delete data while only left node exists'
    bst.deleteTree()

    bst.insert(0)
    bst.insert(1)
    bst.insert(-1)
    bst.delete(0)
    assert bst.root.data == -1, 'fail to delete data while left and right nodes are extant'
    bst.deleteTree()

    print("delete test pass!")


def searchTest():
    bst = BST()

    bst.insert(1)
    assert bst.search(1).data == 1, 'fail to search root data'
    bst.insert(2)
    assert bst.search(2).data == 2, 'fail to search data'
    bst.deleteTree()

    print("search test pass!")


def preorderTest():
    bst = BST()

    bst.insert(0)
    bst.insert(2)
    bst.insert(-2)
    bst.insert(1)
    bst.insert(3)
    bst.insert(-1)
    bst.insert(-3)
    assert bst.preorder() == [0, -2, -3, -1, 2, 1, 3], 'fail to preorder tree'
    bst.deleteTree()

    print("preorder test pass!")


def inorderTest():
    bst = BST()
    bst.insert(0)
    bst.insert(2)
    bst.insert(-2)
    bst.insert(1)
    bst.insert(3)
    bst.insert(-1)
    bst.insert(-3)
    assert bst.inorder() == [-3, -2, -1, 0, 1, 2, 3], 'fail to inorder tree'
    bst.deleteTree()

    print("inorder test pass!")


def postorderTest():
    bst = BST()
    bst.insert(0)
    bst.insert(2)
    bst.insert(-2)
    bst.insert(1)
    bst.insert(3)
    bst.insert(-1)
    bst.insert(-3)
    assert bst.postorder() == [-3, -1, -2, 1, 3, 2,
                               0], 'fail to postorder tree'
    bst.deleteTree()

    print("postorder test pass!")


if __name__ == '__main__':
    insertTest()
    deleteTest()
    searchTest()
    preorderTest()
    inorderTest()
    postorderTest()
