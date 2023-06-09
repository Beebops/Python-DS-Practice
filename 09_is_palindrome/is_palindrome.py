def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    # reverse the phrase and see if it is equal to the original argument
    
    new_phrase = phrase.lower().replace(' ', '')
    return new_phrase == new_phrase[::-1] 

print(is_palindrome('taco cat'))
print(is_palindrome('noon'))
print(is_palindrome('robert'))