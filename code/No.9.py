class Tickets(object):
	
	def __init__(self,_No,_dpt,_arr,_dptTime,_arrTime,_price):
		self.No     = _No
		self.dpt    = _dpt
		self.arr    = _arr
		self.dptTime= _dptTime
		self.arrTime= _arrTime
		self.price  = _price

	def searchTicket( self,_time ):
		self.time = _time
		PTdict = { 10:0.8,15:0.9,20:0.7,24:0.6}
		for key in PTdict.keys():
			if key ==_time:
				print '0001 is PEK to SHA,10:00-12:00,and the price of ticket is',PTdict[key]*self.price

newTickects = Tickets( 0001,'PEK','SHA','10:00','12:00',1000)
newTickects.searchTicket(10)
