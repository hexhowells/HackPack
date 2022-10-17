import math

def lcm(a: int, b: int) -> int:
	"""Calculates the LCM of two numbers without math.lcm for versions of Python <3.9

	Args:
		a (int): first value
		b (int): first value
	"""
	return (a * b) // math.gcd(a,b)
