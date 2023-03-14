def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letters_dict = {}
    for ltr in phrase:
        keys = letters_dict.keys()
        if ltr in keys:
            letters_dict[ltr] += 1
        else:
            letters_dict[ltr] = 1        
    return letters_dict
          
print(multiple_letter_count('yay'))
print(multiple_letter_count('Yay'))
