# generators are controlled iterators, callable by loops
def read_alt(f):
	for line in f:
		yield line # yeilding for a line in the file & returning that line

def double(x):
	return x*2

double = lambda x: x*2 #useful as argument to a function

double(5) # 10


