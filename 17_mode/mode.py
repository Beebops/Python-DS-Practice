def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    
   
    counts = {}
    # loop through list
    # create a dictionary to keep track of counts {1: 2, 2: 1} or {2: 3, 3: 2}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
     # find the key with the maximum value from the dictionary values  
    highest_val = max(counts.values())
    print(highest_val)  # 2
    print(counts.items()) # [(1, 2), (2, 1)]
    for(num, freq) in counts.items():
        if freq == highest_val:
            return num
        
print(mode([1, 2, 1]))
print(mode([2, 2, 3, 3, 2]))