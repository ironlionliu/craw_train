#Filename = myutil.py
from pymongo import MongoClient

class myUtil():
	def __init__(self,db):
		self.name = "hello myutil"
		self.db = db



	def readStations(self, filename):
		data = open(filename,'r')
		stations = []
		while 1:
			line = data.readline()
			if not line:
				break
			line = line.replace("'","")
			line = line.replace(",","")
			line = line.replace("\n","")
			line = line.replace(" ","")
			element = line.split(":")
			element = {"C":element[0],"E":element[1]}
			stations.append(element)
		dict_temp = {}
		for k in stations:
			dict_temp[k["C"]] = k["E"]
		stations = dict_temp
		return stations


	def readStationsAsArr(self, filename):
		data = open(filename,'r')
		stations = []
		while 1:
			line = data.readline()
			if not line:
				break
			line = line.replace("'","")
			line = line.replace(",","")
			line = line.replace("\n","")
			line = line.replace(" ","")
			element = line.split(":")
			element = {"C":element[0],"E":element[1]}
			stations.append(element)
		return stations

	def changeQuery(self, query, stations, from_station, to_station, date):
		query['date'] = date
		query['dptStation'] = stations[from_station]["C"]
		query['arrStation'] = stations[to_station]["C"]

	def genUrl(self, stations, from_station, to_station, date):
	#commonUrl = "https://kyfw.12306.cn/otn/leftTicket/query?"
	#query = {"leftTicketDTO.train_date":"2017-05-24",\
	#"leftTicketDTO.from_station":"BJP","leftTicketDTO.to_station":"SHH","purpose_codes":"ADULT"}
		commonUrl = "http://train.qunar.com/dict/open/s2s.do?"
		query = {"callback":"jQuery172031843804203989556_1495894108865",\
		"dptStation":"北京",\
		"arrStation":"南京",\
		"date":"2017-05-29",\
		"type":"normal",\
		"user":"neibu",\
		"source":"site",\
		"start":"1",\
		"num":"500",\
		"sort":"3"}
		self.changeQuery(query,stations,from_station,to_station,date)
		url = commonUrl
		for(k,v) in query.items():
			url = url + k + "=" + v
			if k != 'sort':
				url = url + '&'
		return url



	##outer_start是外层循环起始,outer_end是外层结束,闭区间.scale是内循环尺寸,闭区间应为2638
	def putUrl2Mongo(self, outer_start, outer_end, scale, date):
		stations = self.readStationsAsArr('stations.py')
		for i in range(outer_start, outer_end+1):
			for j in range(1,scale+1):
				url = self.genUrl(stations, i-1, j-1, date)
				dbdata = {"url":url,"from":stations[i-1]["C"],"to":stations[j-1]["C"],"status":"no"}
				self.db.url.insert_one(dbdata)
			

	def updateMongo(self, option):
		print(option)
		if  option == "addproperty":
			self.db.url.update({},{"$set":{"status":"no"}},upsert=False, multi=True)
		elif option == "restart":
			self.db.url.update({"status":"ing"},{"$set":{"status":"no"}},upsert=False, multi=True)

	




version = "0.1"