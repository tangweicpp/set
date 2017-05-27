#!/usr/bin/python
# encoding:utf-8
 
import urllib2, json, urllib
 
 
# 3、查询违章
 
def cq() 
data = {}
appkey = "your_appkey_here"
data["carorg"] = ""  #交管局代号
data["lsprefix"] = "京"  #车牌前缀 utf8
data["lsnum"] = ""  #车牌
data["lstype"] = "02"  #车辆类型
data["engineno"] = ""  #发动机号
data["frameno"] = ""  #车架号
url_values = urllib.urlencode(data)
url = "http://api.jisuapi.com/illegal/query?appkey=" + appkey
request = urllib2.Request(url,url_values)
result = urllib2.urlopen(request)
jsonarr = json.loads(result.read())
 
if jsonarr["status"] != u"0":
    print jsonarr["msg"]
    exit()
result = jsonarr["result"]
print result
if isinstance(result , list):
    for val in result["list"] :
        print val["time"],val["address"],val["content"],val["legalnum"],val["price"],val["score"]
else:
    print "恭喜您，没有违章！"
