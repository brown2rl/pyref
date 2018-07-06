def fn(a, b=0):
	return a*b

multiple = fn(2) # 0

multiple2 = fun(2,1) # 2

def var_args(a, *args): # arbitrary arguments list
	print(a)
	print(args)

def var_kwargs(a, **kwargs): # arbitrary arguments dictionary
	print(a) # a
	print(kwargs["akey"]) # whoo

b= var_kwargs(akey="whoo", 2, 23)
var_args('a',b)

c=var_args1("whoo",23,1)
var_args('a',c)

aninputvar = input("Prompt for input: ")

# commandline args
import sys
command = sys.argv[1]

# postscript for main.py module scripting
some_initial_action(arg): #for importing
	arg.dosomething()

if __name__ == '__main__':
  # for argv scripting
	some_initial_action(sys.argv[1])

# references vs identities (value of reference is copied, not value of object)
f = [1,2,3]
def replace(g):
	g = [3,2,1]
	print(f"g = {g}") # [3,2,1]

replace(f) # g = [3,2,1]
f # [1,2,3]
