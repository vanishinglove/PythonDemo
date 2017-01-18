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
    key={}
    jsondata=[]
    c = conn()
    cur = c.cursor()
    aa = cur.execute("select * from lcf_result ORDER BY id DESC")
    info = cur.fetchmany(aa)

    for ii in info:
        key['packname'] = ii[1]
        key['time'] = ii[2]
        key['result'] = ii[3]
        key['env'] = ii[4]
        key['link'] = ii[5]
        jsondata.append(key)
        key = {}
    print info
    jsondata = json.dumps(jsondata)
    jsondata2 = jsondata[1:len(jsondata) - 1]
    print jsondata
    return jsondata
    cur.close()
    c.commit()
    c.close()

def insert(pack_name,pactime,result,env,link):
    c = conn()
    cur = c.cursor()
    sql="INSERT INTO lcf_result(pack_name,pactime,result,env,link) VALUES("+"\'"+pack_name+"\'"+","+"\'"+pactime+"\'"+","+"\'"+result+"\'"+","+"\'"+env+"\'"+","+"\'"+link+"\'"+")"
    print sql
    cur.execute(sql)
    cur.close()
    c.commit()
    c.close()
    return ""

def update(pactime,result):
    c = conn()
    cur = c.cursor()
    sql = "UPDATE lcf_result SET result = "+"\'"+result+"\'"+" WHERE pactime ="+"\'"+pactime+"\'"+";"
    print sql
    cur.execute(sql)
    cur.close()
    c.commit()
    c.close()
    return ""

def check():
    key={}
    jsondata=[]
    c = conn()
    cur = c.cursor()
    aa = cur.execute("select * from lcf_result  WHERE result = 'loading' ORDER BY id DESC")
    info = cur.fetchmany(aa)
    print info
    if len(info)==0:
        print "NOHAVE"
        return "NOHAVE"
    else:
        print "HAVE"
        return "HAVE"
    cur.close()
    c.commit()
    c.close()

def checkpac(packname):
    c = conn()
    cur = c.cursor()
    sql="select * from lcf_result  WHERE result = 'loading'and "+"pack_name="+"\'"+packname+"\'"+" ORDER BY id DESC"
    aa = cur.execute(sql)
    info = cur.fetchmany(aa)
    print info
    if len(info) == 0:
        print "NOHAVE"
        return "NOHAVE"
    else:
        print "HAVE"
        return "HAVE"
    cur.close()
    c.commit()
    c.close()


if __name__ == "__main__":
    #insert("1","1","1","1","1")
    checkpac("com.lcf.android.debug #160")