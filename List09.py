from multiprocessing.connection import answer_challenge


def main(list1):
    """
    A list of several elements is given. True if all items are the same,
     otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    i = 0
    ans = 0
    while i<len(list1):
        if list1[0] == list1[i]:
            ans = True
        else:
            ans = False
        i += 1
    return ans
print(main([0,0,0,0,1]))