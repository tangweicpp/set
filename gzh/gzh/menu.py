#!/usr/bin/env python
#coding: utf-8

import urllib
from basic import Basic

class Menu(object):
    def __init__(self):
        pass
    def create(self, postData, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % accessToken
        if isinstance(postData, unicode):
            postData = postData.encode('utf-8')
        urlResp = urllib.urlopen(url=postUrl, data=postData)
        print urlResp.read()

    def query(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()
    
    def delete(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()


    #获取自定义菜单配置接口
    def get_current_selfmenu_info(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()

if __name__ == '__main__':
    myMenu = Menu()
    postJson = """
    {
        "button":
        [
            {
                "name":"操作menu1",
                "sub_button":
                [
                    {
                        "type":"click",
                        "name":"实况截图",
                        "key":"V1001_SNAPSHOT"    
                    },
                    {
                        "type":"view",
                        "name":"实时监控",
                        "url":"http://"
                    }
                ]
            },
            {
                "name":"操作menu2",
                "sub_button":
                [
                    {
                        "type":"click",
                        "name":"获取温湿度",
                        "key":"V1001_TEMP"
                    },
                    {
                        "type":"click",
                        "name":"cpu温度",
                        "key":"V1001_CPU"
                    },
                    {
                        "type":"click",
                        "name":"今日天气",
                        "key":"V1001_WEATHER"
                    }
                ]
            }
        ]
    }
    """
    accessToken = Basic().get_access_token()
    #myMenu.delete(accessToken)
    myMenu.create(postJson, accessToken)
    #myMenu.query(accessToken)


