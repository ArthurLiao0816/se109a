# _.drop ( TDD )
---

> 參考資料：<br>https://medium.com/@yurenju/%E8%87%AA%E5%8B%95%E8%BB%9F%E9%AB%94%E6%B8%AC%E8%A9%A6-tdd-%E8%88%87-bdd-464519672ac5

* TDD (Test-Driven Development)：先寫測試再寫程式

## 過程
### 一、寫測試 (dropTest.py)
1. 由 `lodash` 網站敘述中得知函式所需的參數
    ```
    Arguments
        array (Array): The array to query.
        [n=1] (number): The number of elements to drop.
        Returns
        (Array): Returns the slice of array.
    ```

2. 拿 `lodash` 網站上的 `sample` 當測資
    ```
    Example
        _.drop([1, 2, 3]);
        => [2, 3]
        
        _.drop([1, 2, 3], 2);
        => [3]
        
        _.drop([1, 2, 3], 5);
        => []
        
        _.drop([1, 2, 3], 0);
        => [1, 2, 3]
    ```

3. 長醬 ~
    ```
    from drop import drop


    assert drop([1, 2, 3]) == [2, 3], 'drop([1, 2, 3]) != [2, 3]'

    assert drop([1, 2, 3], 2) == [3], 'drop([1, 2, 3], 2) != [3]'

    assert drop([1, 2, 3], 5) == [], 'drop([1, 2, 3], 5) != []'

    assert drop([1, 2, 3], 0) == [1, 2, 3], 'drop([1, 2, 3], 0) != [1, 2, 3]'

    ```

### 二、寫程式
1. 根據測資裡定義的參數進行設計
    ```
    def drop(array, n=1):
        for i in range(0, n):
            array.pop(0)
        return array
    ```

### 三、測試
* Round 1：
    ```
    PS C:\Users\ldhsi\Desktop\se109a\HW\lodash_implementation\drop> py .\dropTest.py
    Traceback (most recent call last):
    File ".\dropTest.py", line 30, in <module>
        assert drop([1, 2, 3], 5) == [], ' drop([1, 2, 3], 5) != []'
    File "C:\Users\ldhsi\Desktop\se109a\HW\lodash_implementation\drop\drop.py", line 3, in drop
        array.pop(0)
    IndexError: pop from empty list
    ```
    * 上面的錯誤是：你想要從array中drop掉5個元素，但是array裡面卻只有3個元素。所以新增一個變數存取array的長度，當n大於array的長度時，就將array中的元素全部drop掉。
        ```
        l = len(array)
        if n > l:
            n = l
        ```

* Round 2：
    ```
    PS C:\Users\ldhsi\Desktop\se109a\HW\lodash_implementation\drop> py .\dropTest.py
    PS C:\Users\ldhsi\Desktop\se109a\HW\lodash_implementation\drop> 
    ```
    * 通過測試了 ~