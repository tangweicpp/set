#!/usr/bin/python
# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO
import time

#BCM编号方式的17对应树莓派的pin11
channel = 17
data = []
j = 0

#I/O口使用BCM编号方式
GPIO.setmode(GPIO.BCM)

time.sleep(1)

#设置数据线为输出
GPIO.setup(channel, GPIO.OUT)

GPIO.output(channel, GPIO.LOW)
time.sleep(0.02)
GPIO.output(channel, GPIO.HIGH)

#设置数据线为输入
GPIO.setup(channel, GPIO.IN)
while GPIO.input(channel) == GPIO.LOW:
     continue

while GPIO.input(channel) == GPIO.HIGH:
     continue

while j < 40:
     k = 0
     while GPIO.input(channel) == GPIO.LOW:
         continue

     while GPIO.input(channel) == GPIO.HIGH:
         k += 1
         if k > 100:
             break

     if k < 8:
         data.append(0)
     else:
         data.append(1)

     j += 1

print "sensor is working."
print data

#读取数值
humidity_bit = data[0:8]
humidity_point_bit = data[8:16]
temperature_bit = data[16:24]
temperature_point_bit = data[24:32]
check_bit = data[32:40]

humidity = 0
humidity_point = 0
temperature = 0
temperature_point = 0
check = 0

#转换数值
for i in range(8):
     humidity += humidity_bit[i] * 2 ** (7 - i)
     humidity_point += humidity_point_bit[i] * 2 ** (7 - i)
     temperature += temperature_bit[i] * 2 ** (7 - i)
     temperature_point += temperature_point_bit[i] * 2 ** (7 - i)
     check += check_bit[i] * 2 ** (7 - i)

tmp = humidity + humidity_point + temperature + temperature_point

#数据校验
if check == tmp:
     print "temperature : ", temperature, ", humidity : " , humidity
else:
     print "wrong"
     print "temperature : ", temperature, ", humidity : " , humidity, " check : ", check, " tmp : ", tmp

GPIO.cleanup()

#数据转换成JSON格式
mytemp = '{"value":%f}' %temperature
myhumi = '{"value":%f}' %humidity

#打开文件
tmp_output = open('/root/projs/dht11/tmp_data.txt', 'w')
hud_output = open('/root/projs/dht11/hud_data.txt', 'w')

#写数据到文本文件中
tmp_output.write(mytemp)
hud_output.write(myhumi)

#关闭文件
tmp_output.close
hud_output.close
