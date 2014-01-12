Django = [ "Quentin Tarantino", "Django Unchained", 2012 ]
Basterds = [ "Quentin Tarantino", "Inglourious Basterds", 2009 ]
Pulp = [ "Quentin Tarantino", "Pulp Fiction", 1994 ]
Avatar = [ "James Cameron", "Avatar", 2010 ]
Titanic = [ "James Cameron", "Titanic", 1997 ]
movies = [ Django, Basterds, Pulp, Avatar, Titanic ]
newMovies = []
for ele in movies:
	if ele[0] == "Quentin Tarantino":
		newMovies.append( ele )
for ele in newMovies:
	print( ele )