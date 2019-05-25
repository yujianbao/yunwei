#!/usr/bin/python
#coding=utf8

import MySQLdb
import sys

host="localhost"
user="wjq"
passwd="123456"
db="test"
Com_insert="show global status like 'Com_insert';"
Com_update="show global status like 'Com_update';"
Com_select="show global status like 'Com_select';"
Com_delete="show global status like 'Com_delete';"
Open_tables="show global status like 'Open_tables';"
Qcache_hits="show global status like 'Qcache_hits';"

def getConn(host,user,passwd,db):
  try:
    a = MySQLdb.connect(host,user,passwd,db)
    return a
  except:
    print("数据库连接失败")

def getValue(conn,query):
  try:
    cursor = conn.cursor()
    getNum = cursor.execute(query)
    if getNum > 0:
      data = cursor.fetchone()
      return int(data[1])
  except:
    print("查询失败")

conn = getConn(host,user,passwd,db)
if sys.argv[1] == 'insert':
  Com_insert = getValue(conn,Com_insert)
  print(Com_insert)
elif sys.argv[1] == 'delete':
  Com_delete = getValue(conn,Com_delete)
  print(Com_delete)
elif sys.argv[1] == 'select':
  Com_select = getValue(conn,Com_select)
  print(Com_select)
elif sys.argv[1] == 'update':
  Com_update = getValue(conn,Com_update)
  print(Com_update)
elif sys.argv[1] == 'table_num':
  Open_tables = getValue(conn,Open_tables)
  print(Open_tables)
elif sys.argv[1] == 'cache_hit':
  Qcache_hits = getValue(conn,Qcache_hits)
  print(Qcache_hits)