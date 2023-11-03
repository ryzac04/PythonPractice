def last_element(lst):
    """Return last item in list (None if list is empty.

    >>> last_element([1, 2, 3])
    3

    >>> last_element([]) is None
    True
    """
    for i in lst:
        if i in lst:
            return lst[-1]
        else:
            return None
