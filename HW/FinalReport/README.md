# 軟體工程與演算法 期末報告

---

## 二元搜尋樹 ( binary search tree )

### 介紹

- 定義

  - 若任意節點的左子樹不空，則左子樹上所有節點的值均小於它的根節點的值

  * 若任意節點的右子樹不空，則右子樹上所有節點的值均大於或等於它的根節點的值

  * 任意節點的左、右子樹也分別為二元搜尋樹

  - 不存在任何鍵值相等的節點

* 複雜度

  - 插入 Insertion : O ( log n )

  - 刪除 Deletion : O ( log n )

  - 搜尋 Search : O ( log n )

  - 空間複雜度 : O ( n )

### 實作 ( TDD, 100% 原創, 大部分函式使用遞迴撰寫 ( •̀ ω •́ )✧ )

- [測試](test.py) :

  - 對插入資料進行的測試，分別對 : `在空的 BST 中插入資料`、`向右子樹插入資料`、`向左子樹插入資料` 設計測資

    ```
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
    ```

  * 對刪除資料進行的測試，分別對 : `有左右子節點的情況下刪除根節點`、`只有左子節點的情況下刪除根節點`、`只有右子節點的情況下刪除根節點`、`沒有子節點的情況下刪除節點` 設計測資

    ```
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
    ```

  * 對搜尋資料進行測試，分別對 : `搜尋根節點`、`搜尋子節點` 設計測資

    ```
    def searchTest():
        bst = BST()

        bst.insert(1)
        assert bst.search(1).data == 1, 'fail to search root data'
        bst.insert(2)
        assert bst.search(2).data == 2, 'fail to search data'
        bst.deleteTree()

        print("search test pass!")
    ```

  * 對`前序`、`中序`、`後序`走訪設計測資

    ```
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
    ```

* [BST](BST.py)

  - 定義節點
    ```
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
    ```

  * 定義二元搜尋樹
    ```
    class BST:
        def __init__(self):
            self.root = None
    ```
  * Insertion

    - 較大的值放左子樹，小的放右子樹

    * 不可插入已經在樹中存在的鍵值

    ```
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
    ```

  * Deletion

    1. 在有左右子節點的情況下刪除根節點時，需以左子樹中有最大鍵值的節點取代根節點
    2. 在只有左子節點的情況下刪除根節點時，需以左子樹中有最大鍵值的節點取代根節點
    3. 在只有右子節點的情況下刪除根節點時，直接刪除即可
    4. 在沒有子樹的情況下，可以直接刪除根節點

    - 需設計找最大值的函式輔助 `1.` `2.` 的刪除動作

    ```
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
    ```

  * Search

    - 回傳目標節點，設計方向和 Insert 類似，都是大的放右邊，小的放左邊

    ```
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

    ```

  * Pre-order

    - 根節點 -> 左子樹 -> 右子樹

    ```
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
    ```

  * In-order

    - 左子樹 -> 根節點 -> 右子樹

    ```
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
    ```

  * Post-order

    - 左子樹 -> 右子樹 -> 根節點

    ```
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
    ```

* 測試結果

  ```
  PS C:\Users\ldhsi\Desktop\se109a\HW\FinalReport> py .\test.py
  insert test pass!
  delete test pass!
  search test pass!
  preorder =  [0, -2, -3, -1, 2, 1, 3]
  preorder test pass!
  inorder =  [-3, -2, -1, 0, 1, 2, 3]
  inorder test pass!
  postorder =  [-3, -1, -2, 1, 3, 2, 0]
  postorder test pass!
  ```

### References

- [維基百科定義](https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9)

* [Python 物件語法](https://www.learncodewithmike.com/2020/01/python-class.html)

* [二元樹走訪](https://ithelp.ithome.com.tw/articles/10205571)

* [Python 底線小知識](https://aji.tw/python%E4%BD%A0%E5%88%B0%E5%BA%95%E6%98%AF%E5%9C%A8__%E5%BA%95%E7%B7%9A__%E4%BB%80%E9%BA%BC%E5%95%A6/)
