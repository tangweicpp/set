#!/usr/bin/env python
# decoding:utf-8

import urllib, urllib2, json

def tq():
    data = {}
    data['appkey'] = '193f1a1e066e22dc'
    data['city'] = '上海'
    data['cityid'] = '111'
    data['citycode'] = '101260301'

    value = urllib.urlencode(data)
    url = 'http://api.jisuapi.com/weather/query'
    request = urllib2.Request(url, value)
    reponse = urllib2.urlopen(request)
    jsonarr = json.loads(reponse.read())

    if jsonarr['status'] != u'0':
        res =  jsonarr['msg']
        return res
    result = jsonarr['result']
    res = result["city"] + '\n' + result["date"] +'\n'+ result["week"] + '\n' + u'天气:' + result["weather"] + '\n' + u'最高温:'+ result["temphigh"] + '\n' + u'最低温:' + result["templow"]+ '\n' + u'湿度:' + result["humidity"] + '\n' + u'气压:'+result["pressure"] + '\n' + u'风向:'+result['winddirect']+'\n'+u'风级:'+result['windpower']
    aqi = result['aqi']
    res = res + '\n' + 'pm2.5:' + aqi['pm2_5']
    return res
    
if __name__ == '__main__':
    city = '南京'
    print tq()
