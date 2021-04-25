def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    
    # counter = 0
    # for item in lst:
    #     if search_term == item:
    #         counter = counter + 1
            
    # return counter
    
    return lst.count(search_term)