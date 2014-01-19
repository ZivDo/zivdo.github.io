class movies:
	movieName = "none"
	movieDirector = "none"
	movieYear = 0
	newInfo = 0
	def __init__( self, _name, _director, _year ):
		print( "movies init" )
		self.name = _name
		self.director = _director
		self.year = _year

	def showMovieInfo( self ):
		print( "showMovieInfo" )
		print( "movie name is "+ self.name +" and director is " + self.director + " and year is " + str(self.year) )
		print( self.newInfo )

	def addNewInfo( self, _movieLen ):
		self.newInfo = _movieLen

newMovie = movies( "0","0", 0 )
newMovie.showMovieInfo()
newMovie.addNewInfo( 120 )
newMovie.showMovieInfo()

