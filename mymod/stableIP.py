#Filename = stableIP.py
import threading, time, requests, re
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning) # 禁用安全请求警告

#http://www.data5u.com/
#http://www.xicidaili.com/nn/
class StableIP():
	def __init__(self):
		'''废弃
		self.ipNum = ipNum
		self.ipsUrl = ipsUrl
		self.temp = []
		self.result = []
		self.lock = threading.Lock()
		'''
		self.proxies = []
		


	def getIPs(self,filename):
		data = open(filename,'r')
		while 1:
			line = data.readline()
			if not line:
				break
			line = line.replace("\n","")
			proxy = {"http":line}
			self.proxies.append(proxy)
		'''这一部分要根据具体的网站来解析'''
		'''
		headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64)"}
		ip_totle = []
		for page in range(1,pages):
			url = self.ipsUrl + str(page)
			content = requests.get(url,headers=headers,verify=False).text
			print(content)
			pattern=re.compile('<li>(\d.*?)</li>')  #截取<td>与</td>之间第一个数为数字的内容
			ip_page=re.findall(pattern,str(content))
			ip_totle.extend(ip_page)


		#print('代理IP地址     ','\t','端口','\t','速度','\t','验证时间')
		for i in range(0,len(ip_totle),4):
			#print(ip_totle[i],'    ','\t',ip_totle[i+1],'\t',ip_totle[i+2],'\t',ip_totle[i+3])
			self.proxies.append({"http":ip_totle[i]+":"+ip_totle[i+1]})
		'''
		return self.proxies
	
	def singleTest(self,proxy,testUrl):
		testUrl = "http://train.qunar.com/dict/open/s2s.do?"+\
		"callback=jQuery172031843804203989556_1495894108865&"+\
		"dptStation=上海&arrStation=北京&date=2017-06-01&"+\
		"type=normal&user=neibu&source=site&start=1&num=500&sort=3"
		try:
			print("testbegin")
			response = requests.get(testUrl,proxies=proxy,verify=False,timeout=60)
			print("testover")
			if  response.status_code==200:
				return True
		except Exception as e:
			#print(Exception,":",e)
			return False
			pass
		
		





#stableip = StableIP(1,"http://www.xicidaili.com/nn/")
#stableip.getIPs()
#stableip.filterIPs()


version = "0.1"