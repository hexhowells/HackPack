import math
 
def is_square(n: int) -> bool:
    """Checks if a number is a perfect square
    
    Args:
        n (int): value to check
    """
    return n == math.isqrt(n) ** 2
