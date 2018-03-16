def num_vowels(s):
    '''(str) -> int
    num_vowels("Apple")
    2
    num_vowels("mxtwrr")
    0
    '''
    char_count = 0
    
    for char in s:
        if char in "aeiouAEIOU":
            char_count += 1

    return char_count
