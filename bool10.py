import math
def main(a):
    """
    Check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    x = math.sqrt(a)%1
    return x==0
print(main(15))
print(main(121))