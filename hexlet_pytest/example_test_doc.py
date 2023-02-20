def invert_case(string):
    # BEGIN (write your solution here)
    """
    >>> invert_case('WOPasd')
    'wopASD'

    >>> invert_case('')
    ''

    >>> invert_case(invert_case('WOPasd'))
    'WOPasd'
    """
    # END

    result = ''
    for char in string:
        result += char.swapcase()
    return result


if __name__ == "__main__":
    import doctest
    failed, attempted = doctest.testmod()
    assert failed == 0
    assert attempted == 3