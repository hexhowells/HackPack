import math
 
def is_square(n: int) -> bool:
    """Checks if a number is a perfect square
    
    Args:
        n (int): value to check
    """
    return n == math.isqrt(n) ** 2


def get_next_square(n: int) -> int:
     """Gets next perfect square starting at int n (inclusive)
        n=9 returns 9
        n=10 returns 16
        n=0 returns 0
    
    Args:
        n (int): value to start from
    """
    if n <= 0:
        return 0
    else:
        return (math.ceil(math.sqrt(n))) ** 2
