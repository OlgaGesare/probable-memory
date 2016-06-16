def hello(name):
	return "Hello {}".format(name)

def search(A, s):
	return res, index

for name in ['Jane', 'Joe', 'James']:
	print hello(name)

x, y = search()

x = [20, 5, 6, 7, 20, 8, 10, 20]
'''
20 => [0, 4, 7]
0 => []
'''
def search(A, s):
	f = []
	for i, n in enumerate(A):
		if n == s:
			f.append(i)
	return f

print hello('Paul')
