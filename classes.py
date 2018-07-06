'''
Importization

import CassLib
from ClassLib import (object, object2)
from ClassLib import object
'''

class A:
	pass

a = A() # instantiation
b = A()

b is a #False

class B:
	def add_char(self, char):
		char+"z"
		return char

	classchar = self.add_char("c")

	def class_char(self):
		return classchar

char = B()
char.add_char("a") # az
char.class_char # cz

class C:
'''
A class, C
:param char: String - a character
'''
	bang = "!"
# constructor method
	def __init__(self, char):
		self.char = char
		char+"z"+self.bang
		return char
	def class_char(self):
		return self.char+"z"+"c"

	def __str__(self): # return "C" in print(C)
		return "C"

char = C("a") # az!
char = C("a").class_char() # azc
print(C.bang) # !

class LowercaseChar(C): # C is parent
	bang = "."
	def LChar(self):
		original = super().class_char()
		return list(original)

print(LowercaseChar("a")) # az.
print(LowercaseChar("a").LChar()) # ['a','z','c']


