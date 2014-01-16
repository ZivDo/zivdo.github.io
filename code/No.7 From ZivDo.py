import os
fileList = []

fileContent = open( "No.1ForTest.py" )

for line in fileContent:
	if isinstance(line, str):
		fileList.append( line )

fileContent.close()

def txt2List( _name, _lines ):
	moviesName = []
	for line in _lines:
		lineList1 = line.split( "==",1 )
		if len(lineList1) != 2:
			lineList2 = line.split( "=",1 )
			if len( lineList2 ) == 2:
				if lineList2[0].strip() == _name:
					moviesLine = line.split( "=" )
					moviesAfterEqual = moviesLine[1].strip() 
					tempString1 = moviesAfterEqual.split( "[" )[1].strip()				
					moviesNameContent = tempString1.split( "]" )[0].strip()
					contentList = moviesNameContent.split( "," )
					for name in contentList:
						moviesName.append( name.strip() )
					return moviesName

moviesList = txt2List( "movies", fileList )

newMovies = []
for ele in moviesList:
	newMovies.append( txt2List( ele, fileList ) )

def bubble(val):
	for j in range(len (val)-1):
		for i in range( len (val)-1):
			if val[i][2]>val[i+1][2]:
				val[i],val[i+1]=val[i+1],val[i]
	return val


print( bubble(newMovies) )
