def drop(array, n=1):
    l = len(array)
    if n > l:
        n = l
    for i in range(0, n):
        array.pop(0)
    return array