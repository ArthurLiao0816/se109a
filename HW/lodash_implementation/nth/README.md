# _.nth ( BDD )
---

* BDD (Behavior-driven development)：先寫規格，再寫測試，最後寫程式

## 一、寫規格
1. 安裝環境
    ```
    pip install behave
    ```

2. 定義feature場景
    ```
    Feature: Gets the element at index n of array. If n is negative, the nth element from the end is returned
    
    Scenario: run a test
        Given we have an array and two integers
        When we implement a test
        Then behave will test for us
    ```

## 二、創建steps資料夾並設計測資
    ```
    from behave import *
    import nth
    use_step_matcher('re')

    @given(u'we have an array and two integers')
    def step_impl(context):
        context.array = ['a', 'b', 'c', 'd']
        context.a = 1
        context.b = -2
    
    @when(u'we implement a test')
    def step_impl(context):
        context.result1 = nth.nth(context.array, context.a)
        context.result2 = nth.nth(context.array, context.b)

    @then(u'behave will test for us')
    def step_impl(context):
        assert (context.result1 == 'b')
        assert (context.result2 == 'c')
    ```

## 三、設計nth函式
    ```
    def nth(array, n=0):
    l = len(array)
    if n >= 0:
        return array[n]
    else:
        return array[l+n]
    ```

## 四、測試
* 結果
    ```
    PS C:\Users\ldhsi\Desktop\se109a\HW\lodash_implementation\nth> behave .\nthTest.feature
    Feature: Gets the element at index n of array. If n is negative, the nth element from the end is returned # nthTest.feature:1

    Scenario: run a test                      # nthTest.feature:3  
        Given we have an array and two integers # steps/nthTest.py:5 
        When we implement a test                # steps/nthTest.py:11
        Then behave will test for us            # steps/nthTest.py:16

    1 feature passed, 0 failed, 0 skipped
    1 scenario passed, 0 failed, 0 skipped
    3 steps passed, 0 failed, 0 skipped, 0 undefined
    Took 0m0.001s
    ```