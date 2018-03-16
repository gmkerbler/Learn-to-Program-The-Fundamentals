def return_first_recurring(word):
    '''
    (str) -> str
    
    Return the first recurring character in word. 
    

    >>> 'DBCABA'
    B
    >>> 'OCADGC'
    C
    '''
    
    counts = {}

    for char in word:
        if char in counts:
            return char
        else:
            counts[char] = 1
    return None
