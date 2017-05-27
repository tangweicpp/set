python /root/projs/dht11/dht11.py
curl --request POST --data-binary @"/root/projs/dht11/tmp_data.txt" --header "U-ApiKey:51cbf13bf93f679e00c31292aa26ca45" http://api.yeelink.net/v1.0/device/356823/sensor/404565/datapoints
sleep 10s
curl --request POST --data-binary @"/root/projs/dht11/hud_data.txt" --header "U-ApiKey:51cbf13bf93f679e00c31292aa26ca45" http://api.yeelink.net/v1.0/device/356823/sensor/404665/datapoints
