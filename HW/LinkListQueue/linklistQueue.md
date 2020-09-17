# Queue implementation using linked list
---
> 參考資料：
>> https://www.geeksforgeeks.org/queue-linked-list-implementation/<br>
>> https://hackmd.io/@Zero871015/B1DYRkeaQ?type=view#Implementation-for-Queue-by-Linked-List<br>
>> https://hackmd.io/@Zero871015/H12vTu8aX?type=view

## 鏈結串列的性質
* 火車，每節車廂(節點)都有乘客(資料)跟連結下個車廂的勾勾(指標)

## 佇列的性質
* FIFO：先進先出(first in first out)

## 實作~
* 先做出 `節點` ~
    ```
    class node:
    def __init__(self, data):
        self.data = data
        self.next = None
    ```

* 然後是基本的 `queue` ~
    ```
    class queue:
    def __init__(self):
        self.front = self.rear = None
    ```
    * `front`：紀錄刪除節點時的位置
    * `rear`：紀錄增加節點的位置

* 然後是基本queue的功能之 `新增節點` ~
    ```
    def enQueue(self, item):
        tmp = node(item)
        if self.rear == None:
            self.front = self.rear = tmp
            return
        self.rear.next = tmp
        self.rear = tmp
    ```
    * 第三到第五行的程式碼是因應要在一個空的佇列中新增節點的情況，這時front跟rear都會指向同一個節點
    * 六、七行就是其他情況下的新增節點

* 然後是基本queue的功能之 `刪除節點` ~
    ```
    def deQueue(self):
        if self.front == None:
            return
        temp = self.front
        self.front = temp.next
        if self.front == None:
            self.rear = None
    ```
    * ```
        if self.front == None:
            return
        ```
      用來判斷佇列484空的，4的話就什麼都不做
    * ```
        temp = self.front
        self.front = temp.next
        ```
        94一般的從queue中移除front指向的節點
    * 移除節點的時候有一種情況是：佇列中的節點只剩下1個。這種情況下如果我只有做2~5行的話，只有front會清掉節點，rear還是會繼續指向那個被清掉的節點，所以在這種狀況下用
        ```if self.front == None:
            self.rear = None
        ```
        來將rear也清乾淨

* 最後呢~ 我新增了一個印出當前佇列成員的函式
    ```
    def showQueue(self):
        tmp = self.front
        queue = []
        while tmp.data:
            queue.append(tmp.data)
            tmpp = tmp
            if tmpp.next == None:
                break
            tmp = tmpp.next
        print("queue ->", queue)
    ```
    * 在做這個函式的時候有遇到一點問題，一開始在`while`迴圈中我並沒有寫
        ```
        if tmpp.next == None:
            break
        ```
        這段程式碼，所以程式跑著跑著跑到最後一個node的時候，會因為最後一個節點指向`None`，而導致跑下一次迴圈時，出現
        `AttributeError: 'NoneType' object has no attribute 'data'`的錯誤。

* 最後的結果 ~
    ```
    PS C:\Users\ldhsi\Desktop\se109a\HW\LinkListQueue> py .\linklistQueue.py
    q.front.data 4
    q.rear.data 7
    queue -> [4, 8, 7]
    ```