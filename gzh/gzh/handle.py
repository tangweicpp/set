#!/usr/bin/env python
#coding:utf-8
import hashlib
import web
import receive
import reply
import tianqi
from media import get_mediaId

def _cpu_and_gpu_temp():
    '''Get from pi'''
    import commands
    try:
        fd = open('/sys/class/thermal/thermal_zone0/temp')
        ctemp = fd.read()
        fd.close()
        #gtemp = commands.getoutput('/opt/vc/bin/vcgencmd measure_temp').replace('temp=', '').replace('\'C', '')
    except Exception, e:
        return 0
    return float(ctemp) / 1000

class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return 'hello, this is handle view'
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = 'tangweicpp'

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print 'handle/GET func: hashcode, signature: ', hashcode, signature
            if hashcode == signature:
                return echostr
            else:
                return ''
        except Exception, Arg:
            return Arg

    def POST(self):
        try:
            webData = web.data()
            print 'Handle Post webdata is ', webData
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                    content = recMsg.Content
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                if recMsg.MsgType == 'image':
                    mediaId = get_mediaId()
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                return replyMsg.send()
            if isinstance(recMsg, receive.EventMsg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.Event == 'CLICK':
                    print 'click -------'
                    print recMsg.EventKey
                    if recMsg.EventKey == 'V1001_TEMP':
                     #   mediaId = get_mediaId()
                      #  replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                        content = u"编写中，尚未完成".encode('utf-8')
                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                        return replyMsg.send()
                    if recMsg.EventKey == 'V1001_CPU':
                        c = _cpu_and_gpu_temp()
                        content = u'CPU : %.02f℃' %c
                        content = content.encode('utf-8')
                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                        return replyMsg.send()
                    if recMsg.EventKey == 'V1001_WEATHER':
                        content = tianqi.tq()
                        content = content.encode('utf-8')
                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                        return replyMsg.send()
                    if recMsg.EventKey == 'V1001_SNAPSHOT':
                        mediaId = get_mediaId()
                        replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                        return replyMsg.send()
                        
            print '暂且不处理'
            return reply.Msg().send()
        except Exception, Arg:
            return Arg
