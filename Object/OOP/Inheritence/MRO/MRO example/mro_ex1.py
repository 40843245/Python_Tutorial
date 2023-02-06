

class A:
	def rk(self):
		print(" In class A")
class B:
	def rk(self):
		print(" In class B")

# classes ordering
class C(A, B):
	def __init__(self):
		print("Constructor C")
        
class D(C):
    def __init__(self):
        print("Constructor D")
        
class E(B):
    def __init__(self):
        print("Constructor E")
        
class F(D,E):
    def __init__(self):
        print("Constructor F")
        
r = F()

# it prints the lookup order
print(F.__mro__) # return a list
print(F.mro())   # return a tuple
