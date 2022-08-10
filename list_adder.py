def add_lists(list1, list2):
    """
    Args:
        list1 (list): List of ints and sub-lists with more ints
        list2 (list): An list with the same sub-list structure
    Returns list:
        A list where all ints are added together.
        for example:
            [[1,2],[4,4],[2,3]] + [[3,0],[1,2],[0,0]] = [[4,2],[5,6],[2,3]]
    """
    for a, b in zip(list1, list2):
        if type(a) == list:
            yield list(add_lists(a, b))
        else:
            yield a+b
