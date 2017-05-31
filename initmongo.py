# coding=utf-8
import threading, time, requests
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning) # 禁用安全请求警告

from pymongo import MongoClient
import mymod.myutil
import mymod.stableIP
from json import *

client = MongoClient()
db = client.test
myutil = mymod.myutil.myUtil(db)

#myutil.updateMongo("restart")
myutil.putUrl2Mongo(372,392,2638,"2017-06-20")
print("开始")
results = list(db.url.find({"status":"no"}).limit(50000))
for result in results:
	db.url.update({"_id":result["_id"]},{"$set":{"status":"ing"}},upsert=False, multi=False)


print("更新完成")
#myutil.updateMongo("restart")
#
#
#
'''
###4liushangyu  (1~1319)*2638
for i in range(1,440):
	print(i)
	start = (i-1)*3+1
	end = i*3
	scale = 2638
	datestrr = "2017-06-20"
	threading.Thread(target = myutil.putUrl2Mongo, args = ([start,end,scale,datestrr]), name = i).start() 

myutil.putUrl2Mongo(1318,1319,2638,"2017-06-20")
###4liushangyu
#
#
###4yujialong  (1320~2638)*2638
for i in range(1,440):
	print(i)
	start = (i-1)*3+1+1319
	end = i*3+1319
	scale = 2638
	datestrr = "2017-06-20"
	threading.Thread(target = myutil.putUrl2Mongo, args = ([start,end,scale,datestrr]), name = i).start() 
myutil.putUrl2Mongo(2637,2638,2638,"2017-06-20")
###4yujialong
'''



###4yujialong