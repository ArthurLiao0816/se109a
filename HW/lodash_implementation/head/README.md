# _.head ( 傳統測試 )
---

* 傳統測試：先寫程式再寫測試

## 過程
### 一、寫程式
1. 由 `lodash` 網站敘述中得知函式的功能
    ```
    Gets the first element of array.
    ```

2. 寫程式
    ```
    def head(array):
        return array[0]
    ```

### 二、寫測試
    ```
    from head import head
    """
    Example
    _.head([1, 2, 3]);
    // => 1
    
    _.head([]);
    // => undefined
    """

    print('head([1, 2, 3]) = ', head([1, 2, 3]))
    print('head([]) = ', head([]))
    ```

### 三、測試
* Round 1
    ```
    PS C:\Users\ldhsi\Desktop\se109a\HW\lodash_implementation\head> py .\headTest.py
    head([1, 2, 3]) =  1
    Traceback (most recent call last):
    File ".\headTest.py", line 12, in <module>
        print('head([]) = ', head([]))
    File "C:\Users\ldhsi\Desktop\se109a\HW\lodash_implementation\head\head.py", line 5, in head
        return array[0]
    IndexError: list index out of range
    ```

* 改成醬
    ```
    def head(array):
        if len(array) == 0:
            return None
        else:
            return array[0]
    ```

* Round 2
    ```
    PS C:\Users\ldhsi\Desktop\se109a\HW\lodash_implementation\head> py .\headTest.py
    head([1, 2, 3]) =  1
    head([]) =  None
    ```