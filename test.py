from pyzabbix import ZabbixAPI
import itertools
import time

z = ZabbixAPI(url = "http://10.164.45.242/zabbix", user = "admvprokoshev", password = "Vlpr3211")
hosts = z.host.get(groupids='97')
host_count = []
for i in hosts:
    host_count = host_count + [[i['hostid']] + [i['host']]]

items = z.item.get(groupids='97',
                   search= {
            "key_": "icmpping[]"
        },)
for i in items:
    print(i)

hostif = z.hostinterface.get(filter= {
            'main': '0'})
for i in hostif:
    print(i)



