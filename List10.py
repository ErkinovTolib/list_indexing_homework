def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    i = 0
    while i<len(list_num):
        if list_num[i]>list_num[i-1]:
            c = list_num[i]
        else:
            c = list_num[i-1]
        i += 1
    return c
print(main([1,8,9,5]))
        