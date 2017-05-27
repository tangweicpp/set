#!/usr/bin/env python
#coding:utf8

import urllib2, json, urllib

def cq():
    data = {}
    data["appkey"] = "4454"
    data["city"] = "上海"
    data["cityid"] = "111"
    data["citycode"] = "101260301"

    url_values = urllib.urlencode(data)
    url = "http://api.jisuapi.com/weather/query"
    result = urllib2.urlopen(url, data)
    jsonarr = json.loads(result.read())

    if jsonarr["status"] != u"0":
        print jsonarr["msg"]
        exit()
    result = jsonarr["result"]
    res = "城市",  result["city"], "天气", result["weather"],"\n", result["最高温"], result["temphigh"],"\n", "最低温",  result["templow"]
    return res


if __name__ == "__main__":
    cq()
