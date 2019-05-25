#!/usr/bin/python
import os

'''
1、实现原理：通过SNMP协议获取系统信息，再进行相应的计算和格式化，最后输出结果
2、特别注意：被监控的机器上需要支持snmp。yum install -y net-snmp*安装
'''

def getAllitems(host, oid):
    sn1 = os.popen('snmpwalk -v 2c -c public ' + host + ' ' + oid).read().split('\n')
    return sn1


def getload(host, loid):
    load_oids = '1.3.6.1.4.1.2021.10.1.3.' + str(loid)
    return getAllitems(host, load_oids)[0].split(':')[3]


if __name__ == '__main__':
    hosts = ['192.168.10.1', '192.168.10.2']
    # check_system_load
    print('==============System Load==============')
    for host in hosts:
        load1 = getload(host, 1)
        load10 = getload(host, 2)
        load15 = getload(host, 3)
        print('%s load(1min): %s ,load(10min): %s ,load(15min): %s' % (host, load1, load10, load15))