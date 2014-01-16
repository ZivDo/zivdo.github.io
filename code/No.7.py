import os
def fileContent(ele):
	File=open('No.1ForTest.py')
	for lines in File:
		lists=lines.strip()
		lists1=lines.split('==',1)
		if len('lists')!=2:
			lists2=lists.split('=',1)
			if len(lists2)==2:
				if lists2[0].strip()==ele:
					moviesName=lists2[1].strip()
					moviesName1=moviesName.split('[')[1].strip()
					moviesName2=moviesName1.split(']')[0].strip()
					moviesName3=moviesName2.split(',')
					return moviesName3
	File.close()
# print fileContent('movies')[1]
newMovies=[]
for name in fileContent('movies'):
	newMovies.append(fileContent(name.strip()))

def bubble(val):
	for j in range(len (val)-1):
		for i in range( len (val)-1):
			if val[i][2]>val[i+1][2]:
				val[i],val[i+1]=val[i+1],val[i]
	return val
print bubble(newMovies)