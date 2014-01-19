class Dog:
	name = ""
	age = 0
	category = "A"

	def __init__( self, _name, _age, _category ):
		self.name = _name
		self.age = _age
		self.category = _category

	def dogInfo( self ):
		print( self.name, self.age, self.category )

	def function1( self ):
		pass




dog1 = Dog( "Bajie", 4, "B")
# print( isinstance( dog1, Dog ) )
dog1.dogInfo()



