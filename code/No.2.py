def bubbleSort( _list ):
	for j in range( len(_list) ):
		i = 0
		for i in range( len(_list) - 1 ):
		    if _list[i]>_list[i+1]:
		        _list[i],_list[i+1]=_list[i+1],_list[i]
	return _list

numbers=['8','6','3','9','5','2','4','1','7']
print(bubbleSort( numbers ))