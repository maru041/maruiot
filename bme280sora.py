#coding: utf-8
from azure.servicebus import ServiceBusService
import urllib3
import datetime

#azure service bus
key_name = 'SendRule' # SharedAccessKeyName from Azure portal
key_value = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # SharedAccessKey from Azure portal
service_namespace = 'sora-ns'
sbs = ServiceBusService(service_namespace,
                        shared_access_key_name=key_name,
                        shared_access_key_value=key_value)

#values
http = urllib3.PoolManager()
r = http.request('GET', 'http://beam.soracom.io:8888/')
devid = r.data.split("=")[1].strip()
dtime = datetime.datetime.today().strftime("%F %H:%M:%S %z").strip()
#from sensors
temp = "27.4"
pres = "1000.1"
hum = "68.0"
hilux = "100.0"
lowlux = "10.0"

#json fot event hub
json = '{ "Date":"' + dtime + '", "DeviceId":"' + devid + '", "Temp":"' + temp + '", "Pressure":"' + pres + '","Hum":"' + hum + '", "HiLux":"' + hilux + '","LowLux":"' + lowlux + '" }'
sbs.send_event('sora', json)