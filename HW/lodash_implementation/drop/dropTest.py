from drop import drop
"""Creates a slice of array with n elements dropped from the beginning.


Arguments
    array (Array): The array to query.
    [n=1] (number): The number of elements to drop.
    Returns
    (Array): Returns the slice of array.

Example
    _.drop([1, 2, 3]);
    => [2, 3]
    
    _.drop([1, 2, 3], 2);
    => [3]
    
    _.drop([1, 2, 3], 5);
    => []
    
    _.drop([1, 2, 3], 0);
    => [1, 2, 3]
"""


assert drop([1, 2, 3]) == [2, 3], 'drop([1, 2, 3]) != [2, 3]'

assert drop([1, 2, 3], 2) == [3], 'drop([1, 2, 3], 2) != [3]'

assert drop([1, 2, 3], 5) == [], ' drop([1, 2, 3], 5) != []'

assert drop([1, 2, 3], 0) == [1, 2, 3], 'drop([1, 2, 3], 0) != [1, 2, 3]'
