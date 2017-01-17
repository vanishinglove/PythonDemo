# coding:utf-8

import MySQLdb
import json

cur = object
conn = object
def conn():
    try:
        conn= MySQLdb.connect(
                host='localhost',
                port = 3306,
                user='root',
                passwd='root',
                db ='mydemo',
                )
        #cur=conn.cursor()
    except:
        print "fail"
    print "success"
    return conn

def select():
    json1 = []
    dict1 = {}
    dict2 = {}
    key={}
    jsondata=[]
    c = conn()
    cur = c.cursor()
    aa = cur.execute("select * from lcf_result")
    info = cur.fetchmany(aa)

    for ii in info:
        key['packname'] = ii[1]
        key['time'] = ii[2]
        key['result'] = ii[3]
        key['env'] = ii[4]
        jsondata.append(key)
    print jsondata
    jsondata = json.dumps(jsondata)
    jsondata = jsondata[1:len(jsondata) - 1]
    return jsondata
    cur.close()
    c.commit()
    c.close()


if __name__ == "__main__":
    select()