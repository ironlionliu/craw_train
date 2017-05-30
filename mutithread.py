# coding=utf-8
import threading, time, requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning) # 禁用安全请求警告

from pymongo import MongoClient
import mymod.myutil
import mymod.stableIP
from json import *



#train_info = craw_result.json()['data']['result'][j].split('|')
#train_info : [3]:车次         [4]:该车次始发站代号  [5]:该车次终点站代号  [6]:本次查询出发站代号  
#             [7]:本次查询到达站 [8]:出发时间        [9]:到达时间         [10]:是否有票       [11]:???
#                      
#去哪网数据结构: 
'''
    {
	    "ret": true,
	    "data": {
	        "flag": true,
	        "errorCode": 0,
	        "dptStation": "北京",
	        "arrStation": "汤旺河",
	        "dptDate": "2017-06-20",
	        "s2sBeanList": [],
	        "updateTs": 1496082033,
	        "status": "UNKNOWN",
	        "dptCity": "北京",
	        "arrCity": "汤旺河",
	        "dptCityFullPy": "beijing",
	        "arrCityFullPy": "tangwanghe",
	        "transfer": false,
	        "wwwRobTicketMaxTaskNum": 20,
	        "wwwRobTicketWarmTip": "继续添加备选方案，大大提升成功率!",
	        "wwwRobTicketMaxTaskWarn": "您已选择20种抢票方案，无法继续添加",
	        "robPeriod": 30,
	        "subscribePeriod": 10,
	        "extraData": {},
	        "searchType": 0,
	        "trainSearchType": 1,
	        "recommendTrainJoint": 0,
	        "sameCity": false
	    },
	    "errmsg": "请求成功",
	    "errcode": 0
	}
	{
    'seats': {
        '无座': {
            'price': 198,
            'count': 100,
            'enable': True,
            'seatMap': {
                'ticketNumStatus': 2
            }
        },
        '硬座': {
            'price': 198,
            'count': 100,
            'enable': True,
            'seatMap': {
                'ticketNumStatus': 2
            }
        },
        '硬卧': {
            'price': 337,
            'count': 5,
            'enable': True,
            'seatMap': {
                'ticketNumStatus': 1
            }
        },
        '软卧': {
            'price': 530,
            'count': 2,
            'enable': True,
            'seatMap': {
                'ticketNumStatus': 1
            }
        }
    },
    'trainNo': 'T9',
    'trainCode': '24000000T90S',
    'dptStationName': '北京西',
    'arrStationName': '万源',
    'dptStationCode': 'BXP',
    'arrStationCode': 'WYY',
    'dptStationNo': '01',
    'arrStationNo': '11',
    'startStationName': '北京西',
    'endStationName': '重庆北',
    'startStationCode': 'BXP',
    'endStationCode': 'CUW',
    'startDate': '20170620',
    'dptTime': '15: 05',
    'arrTime': '11: 21',
    'dayDifference': '1',
    'lishiValue': '1216',
    'locationCode': 'P4',
    'saleTime': '10: 00',
    'seatTypes': '1413',
    'controlFlag': '0',
    'controlMsg': '23: 00-06: 00系统维护时间',
    'presaleDay': 0,
    'robPeriod': 0,
    'subscribePeriod': 0,
    'timeDim': 12,
    'noteDim': 34,
    'ypDim': 21,
    'saleStatus': {
        'saleId': 12,
        'desc': '可预订'
    },
    'extraBeanMap': {
        'arrDate': '2017-06-21',
        'intervalMiles': 2837,
        'sort': 0,
        'interval': '20小时16分',
        'deptStationInfo': True,
        'dptCityName': '北京',
        'deptTimeRange': '下午',
        'sale': 21,
        'startSaleTime': '2017-05-2210: 00',
        'ticketType': '硬座,
        硬卧,
        无座,
        软卧',
        'ticketsUnknown': False,
        'arriTimeRange': '上午',
        'dptDate': '2017-06-20',
        'arriStationInfo': False,
        'trainType': '空调特快',
        'arrCityName': '万源',
        'stationType': '始发,
        过路',
        'tickets': 207
    }
},
{
    'seats': {
        '无座': {
            'price': 198,
            'count': 100,
            'enable': True,
            'seatMap': {
                'ticketNumStatus': 2
            }
        },
        '硬座': {
            'price': 198,
            'count': 100,
            'enable': True,
            'seatMap': {
                'ticketNumStatus': 2
            }
        },
        '硬卧': {
            'price': 337,
            'count': 100,
            'enable': True,
            'seatMap': {
                'ticketNumStatus': 2
            }
        },
        '软卧': {
            'price': 530,
            'count': 13,
            'enable': True,
            'seatMap': {
                'ticketNumStatus': 1
            }
        }
    },
    'trainNo': 'K507',
    'trainCode': '240000K50726',
    'dptStationName': '北京西',
    'arrStationName': '万源',
    'dptStationCode': 'BXP',
    'arrStationCode': 'WYY',
    'dptStationNo': '01',
    'arrStationNo': '21',
    'startStationName': '北京西',
    'endStationName': '贵阳',
    'startStationCode': 'BXP',
    'endStationCode': 'GIW',
    'startDate': '20170620',
    'dptTime': '21: 23',
    'arrTime': '19: 57',
    'dayDifference': '1',
    'lishiValue': '1354',
    'locationCode': 'PB',
    'saleTime': '10: 00',
    'seatTypes': '1413',
    'controlFlag': '0',
    'controlMsg': '23: 00-06: 00系统维护时间',
    'presaleDay': 0,
    'robPeriod': 0,
    'subscribePeriod': 0,
    'timeDim': 12,
    'noteDim': 34,
    'ypDim': 21,
    'saleStatus': {
        'saleId': 12,
        'desc': '可预订'
    },
    'extraBeanMap': {
        'arrDate': '2017-06-21',
        'intervalMiles': 2708,
        'sort': 1,
        'interval': '22小时34分',
        'deptStationInfo': True,
        'dptCityName': '北京',
        'deptTimeRange': '晚上',
        'sale': 21,
        'startSaleTime': '2017-05-2210: 00',
        'ticketType': '硬座,
        硬卧,
        无座,
        软卧',
        'ticketsUnknown': False,
        'arriTimeRange': '晚上',
        'dptDate': '2017-06-20',
        'arriStationInfo': False,
        'trainType': '快速',
        'arrCityName': '万源',
        'stationType': '始发,
        过路',
        'tickets': 313
    }
}
'''

#测试并行效率
def crawtest(step, proxy, urlquery, isproxy):
    threadname = "线程" + threading.currentThread().getName()
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64)"}
    for i in range(0,step):
        try:
            if isproxy == 1:
                craw_result = requests.get(urlquery[i]["url"],proxies=proxy,headers=headers,verify=False)
            else:
                craw_result = requests.get(urlquery[i]["url"],headers=headers,verify=False)
            print(threadname+"@@@@"+str(craw_result.status_code))
		#request.get出错
        except Exception as e:
            print(e)
            break
            pass
    print("the thread is over"+threadname)



def craw(step, proxy, urlquery, isproxy):
    threadname = "线程" + threading.currentThread().getName()
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64)"}
    for i in range(0,step):
        try:
            if isproxy == 1:
                craw_result = requests.get(urlquery[i]["url"],proxies=proxy,headers=headers,verify=False)
            else:
                craw_result = requests.get(urlquery[i]["url"],headers=headers,verify=False)
            if craw_result.status_code==200:
				#必有正则表达式代替如此傻逼的写法
                result = craw_result.text.replace("/**/jQuery172031843804203989556_1495894108865","")
                result = result.replace("(","")
                result = result.replace(")","")
                result = result.replace(";","")
				#
                result = JSONDecoder().decode(str(result))
				#result = JSONDecoder().decode(str(result["data"]))
				#
				#有车次
                if len(result['data']['s2sBeanList']):
                    print(urlquery[i]["url"])
                    for train in range(0,len(result['data']['s2sBeanList'])):
                        print(result['data']['s2sBeanList'][train]['seats'])
                        print(result['data']['s2sBeanList'][train]['trainNo'])
						#train_data = ?????@@@于佳龙
						#爬取后的数据处理
						#db.trainmap.insert_one(train_data)
						#db.url.update({"url":urlquery[i]["url"]},{"$set":{"status":"hasdata"}},\
						#upsert=False, multi=False)
                    print(threadname+"@@@@200")
                else:
                    print(threadname+"没车")
					#db.url.update({"url":urlquery[i]["url"]},{"$set":{"status":"nodata"}},\
					#upsert=False,multi=False)
			#非200请求，请求出错
            else:
                print(threadname+"@@@@"+str(craw_result.status_code))
        #request.get出错
        except Exception as e:
            print(e)
            break
            pass
'''
		#print(craw_result.json()['data']['result'])
		if len(craw_result.json()['data']['result']):
			for j in range(0, len(craw_result.json()['data']['result'])):
				train_info = craw_result.json()['data']['result'][j].split('|')
				train_data = {"车次":train_info[3],"始发站代号":train_info[4],\
				"始发站名":english_stations[train_info[4]],\
				"终点站代号":train_info[5],\
				"终点站名":english_stations[train_info[5]],\
				"出发站代号":train_info[6],\
				"出发站名":english_stations[train_info[6]],\
				"到达站代号":train_info[7],\
				"到达站名":english_stations[train_info[7]],\
				"出发时间":train_info[8],\
				"到达时间":train_info[9]}
				db.trainmap.insert_one(train_data)
				db.url.update({"url":urlquery[i]["url"]},{"$set":{"status":"hasdata"}},\
				upsert=False, multi=False)
		else:
			db.url.update({"url":urlquery[i]["url"]},{"$set":{"status":"nodata"}},upsert=False, \
			multi=False)


'''


#测试区————测试自定义包的各种函数
#'''
testUrl = "http://train.qunar.com/dict/open/s2s.do?"+\
        "callback=jQuery172031843804203989556_1495894108865&"+\
        "dptStation=上海&arrStation=北京&date=2017-05-31&"+\
        "type=normal&user=neibu&source=site&start=1&num=500&sort=3"

client = MongoClient()
db = client.test
myutil = mymod.myutil.myUtil(db)
#myutil.putUrl2Mongo(382,382,2638,"2017-06-20")
myutil.updateMongo("restart")
lock = threading.Lock()
stableip = mymod.stableIP.StableIP()
proxies = stableip.getIPs("ips.py")
#craw(100,proxies[0],0)
#测试多线程速度
def callcrawtest(step, proxy, urlquery_step):
    #if stableip.singleTest(proxy,testUrl):
    if step > 0:
        print("succeded")
        crawtest(step, proxy, urlquery_step, 0)
    else:
        print("failed")



step = 100
urlquery = list(db.url.find({"status":"no"}).limit(step*len(proxies)))
for i in range(0, step*len(proxies)):
    db.url.update({"url":urlquery[i]["url"]},{"$set":{"status":"ing"}},upsert=False, multi=False)
count = 0
for proxy in proxies:
    count = count + 1
    start = (count - 1)*step
    end =(count)*step
    urlquery_step = urlquery[start:end]
    threading.Thread(target = callcrawtest,args=([step,proxy,urlquery_step]),name = "name:"+str(count)).start()




#craw(100,proxies[0],0)
#stations = myutil.readStationsAsArr("mymod/stations.py")
#myutil.genUrl(stations,1,2,"2017-06-20")
#myutil.updateMongo("addproperty")

#'''
#测试区结束



#主程序————爬虫程序
'''

testUrl = "http://train.qunar.com/dict/open/s2s.do?"+\
        "callback=jQuery172031843804203989556_1495894108865&"+\
        "dptStation=上海&arrStation=北京&date=2017-05-31&"+\
        "type=normal&user=neibu&source=site&start=1&num=500&sort=3"

client = MongoClient()
db = client.quna
myutil = mymod.myutil.myUtil(db)
myutil.updateMongo("restart")
lock = threading.Lock()
stableip = mymod.stableIP.StableIP()
proxies = stableip.getIPs("ips.py")

def callcraw(step, proxy, urlquery_step):
    if stableip.singleTest(proxy,testUrl):
        craw(step, proxy, urlquery_step, 1)
    else:
        print("error")

step = 1000
urlquery = list(db.url.find({"status":"no"}).limit(step*len(proxies)))
for i in range(0, step*len(proxies)):
    db.url.update({"url":urlquery[i]["url"]},{"$set":{"status":"ing"}},upsert=False, multi=False)
count = 0
for proxy in proxies:
    count = count + 1
    start = (count - 1)*step
    end =(count)*step
    urlquery_step = urlquery[start:end]
    threading.Thread(target = callcraw,args=([step,proxy,urlquery_step]),name = "name:"+str(count)).start()






'''
#######主函数结束




''' 
#初始化数据库
for i in range(1,261):
	print(i)
	start = (i-1)*10
	end = i*10-1
	scale = 2638
	threading.Thread(target = putUrl2Mongo, args = ([start,end,scale]), name = i).start() 

	'''  








