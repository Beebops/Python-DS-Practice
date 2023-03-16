def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    # if any item in lst is not a list, return false
    for item in lst:
        if not isinstance(item, list):
            return False
    return True



        
print(list_check([[1], [2, 3]]))      
print(list_check([[1], "nope"]))  