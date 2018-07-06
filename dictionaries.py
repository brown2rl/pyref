s = {
	"a" : "lov",
	"b" : 1,
	"c" : True
}

s["b"] # 1

s.values() # ['lov',1,True]

del s["c"] # s == {"a":"lov","b":1}

s["c"] = True #s == {'a':'lov','b':1,'c':True}
