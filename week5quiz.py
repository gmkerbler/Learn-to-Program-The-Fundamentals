def secret(s):
    i = 0
    result = ''

    while s[i].isdigit():
        result = result + s[i]
        i = i + 1
   
    return result


def example(L):
    """ (list) -> list
    """
    i = 0
    result = []
    while i < len(L):
        result.append(L[i])
        i = i + 3
    return result

def compress_list(L):
    """ (list of str) -> list of str

    Return a new list with adjacent pairs of string elements
    from L concatenated together, starting with indices 0 and
    1, 2 and 3,and so on.

    Precondition: len(L) >= 2 and len(L) % 2 == 0

    >>> compress_list(['a', 'b', 'c', 'd'])
    ['ab', 'cd']
    """ 
    compressed_list = []
    i = 0

    while i < len(L):
        compressed_list.append(L[i] + L[i + 1])
        i = i + 2

    return compressed_list

def sum_even_new(start, end):
    """ (str, str) -> str

    Return a sum of all the even numbers from start to end, inclusive.

    >>> sum_even(0, 10)    
    30
    >>> sum_even(4, 10)
    28
    """

    i = start
    sum = 0

    while i < end + 1:
        sum = sum + i
        i = i + 2

    return sum

def sum_even_forloop(start, end):

    """ (str, str) -> str

    Return a sum of all the even numbers from start to end, inclusive.

    >>> sum_even_forloop(0, 10)    
    30
    >>> sum_even_forloop(4, 10)
    28
    """

    sum = 0
    
    for num in range(start, end + 1, 2):

        sum = sum + num

    return sum

# QUESTION 6

def while_version(L):
    """ (list of number) -> number
    """
    i = 0
    total = 0

    while i < len(L) and L[i] % 2 != 0:
        total = total + L[i]
        i = i + 1

    return total

def for_version(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0 and not found_even:
            total = total + num
        else:
            found_even = True
 
    return total

def cap_song_repetition(playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.

    '''
    while playlist.count(song) > 3:
        playlist.pop(playlist.index(song))

def cap_song_repetition2(playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.

    '''
    while playlist.count(song) > 3:
        playlist.remove(song)

def increment_items(L, increment):
    i = 0
    while i < len(L):
        L[i] = L[i] + increment
        i = i + 1

