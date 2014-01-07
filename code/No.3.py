Django = [ "Quentin Tarantino", "Django Unchained", 2012 ]
Basterds = [ "Quentin Tarantino", "Inglourious Basterds", 2009 ]
Pulp = [ "Quentin Tarantino", "Pulp Fiction", 1994 ]
Avatar = [ "James Cameron", "Avatar", 2010 ]
Titanic = [ "James Cameron", "Titanic", 1997 ]

movies = [ Django, Basterds, Pulp, Avatar, Titanic ]

def maopao(list):
    j=0
    while j<len(list)-1:
        i=0
        while i<len(list)-1:
            if list[i][2]>list[i+1][2]:
                list[i],list[i+1]=list[i+1],list[i]
            i=i+1
        j=j+1           
    return list

print(maopao(movies))