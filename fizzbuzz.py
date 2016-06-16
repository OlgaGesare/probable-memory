def fizz_buzz():
	""" return fizz when divisible by 3
	return buzz when diviisible by 5
	return fizzbuzz when divisible by both 3 and 5
	"""
	if n % 3 == 0 and n % 5 == 0:
		return 'fizzbuzz'
	elif n % 3 == 0:
		return 'fizz'
	elif n % 5 == 0:
	    return 'buzz'