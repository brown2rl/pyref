'''
Access Modes:

'w' = make new or overwrite
'r' = reading
'a' = appending to file
'rb' = read binary
'wb' = write binary
'''


def write(info):
	try:
		f = open("filename.ext", "a") # append mode, will create file if none
		f.write(info + "\n")
		f.close()
	except Exception:
		print("no saving")

def read():
	n = "filename.ext"	
	try:
		f = open(n,"r") # read mode
		for info in f.readlines():
			some_action(info)
		f.close()
	except Excption:
		print(f"no reading or no file, {n}")
