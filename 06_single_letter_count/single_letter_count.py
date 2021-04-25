def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    
    counter = 0
    for l in word.lower():
        if l is letter:
            counter = counter + 1
            
    return counter
            
            
print(single_letter_count("Hello World", 'l'))
print(single_letter_count('Hello World', 'z'))
print(single_letter_count('Hello World', 'h'))