#!/usr/bin/env python
#coding: utf-8

from basic import Basic
import urllib2
import json
import poster.encode
import os
from poster.streaminghttp import register_openers

no = 1
class Media(object):
    def __init__(self):
        self.mediaId = ''
        register_openers()
    # 上传图片
    def upload(self, accessToken, filePath, mediaType):
        openFile = open(filePath, 'rb')
        param = {'media':openFile}
        postData, postHeaders = poster.encode.multipart_encode(param)

        postUrl = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s" % (accessToken, mediaType)
        request = urllib2.Request(postUrl, postData, postHeaders)
        urlResp = urllib2.urlopen(request)
        res = urlResp.read()
        print res
        urlResp = json.loads(res)
        self.mediaId = urlResp['media_id']
        
def get_mediaId():
    myMedia = Media()
    accessToken = Basic().get_access_token()
    take_picture()
    filePath = r'/root/sources/%d.jpg' %no
#    filePath = '/root/medias/test.jpg'
    mediaType = 'image'
    myMedia.upload(accessToken, filePath, mediaType)
    print 'mediaId = ', myMedia.mediaId
    return myMedia.mediaId
        
def _take_snapshot(addr, port):
    url = 'http://%s:%d/?action=snapshot' %(addr, port)
    req = urllib2.Request(url)
    resp = urllib2.urlopen(req, timeout = 2)
    print resp.read()
# return client.media.upload.file(type = 'image', pic = resp)
if __name__ == '__main__':
    '''
    myMedia = Media()
    accessToken = Basic().get_access_token()
    filePath = '/root/medias/test.jpg'
    mediaType = 'image'
    myMedia.upload(accessToken, filePath, mediaType)
    print 'mediaId = ', myMedia.mediaId
    '''
    _take_snapshot('127.0.0.1', 8080)  
def take_picture():
    global no
    no += 1
    cmd = r'fswebcam -d /dev/video0 -r 960x640 /root/sources/%d.jpg' %no
    os.system(cmd)

