def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    counts = {}
    
    # Creates counter dictionary Ex. {2: 3, 3: 2}
    for num in nums:
        # each index of num is set up 
        counts[num] = counts.get(num, 0) + 1
        
    max_value = max(counts.values())
    
    for (num, freq) in counts.items():
        if freq == max_value:
            return num
        