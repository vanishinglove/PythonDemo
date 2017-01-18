# coding:utf-8
import urllib2
import re
import database

def request(lcfenv):
    pattern = re.compile("<result>(.*?)</result>",re.S)
    pattern1 = re.compile("<fullDisplayName>(.*?)</fullDisplayName>",re.S)
    pattern2 = re.compile("<timestamp>(.*?)</timestamp>",re.S)
    pattern3 = re.compile("<building>(.*?)</building>", re.S)
    respon = urllib2.urlopen("http://172.16.16.18:9999/job/com.lcf.android.debug/lastBuild/api/xml?admin:admin123");
    str =  respon.read()
    #result = re.findall(pattern,str)
    package = re.findall(pattern1,str)
    time = re.findall(pattern2,str)
    build = re.findall(pattern3,str)
    if build[0]=="false":
        request('debug')
        database.insert(package[0], time[0], "loading", lcfenv, "no")
        result = re.findall(pattern, str)
        print result[0]
        if database.check() == "NOHAVE":
            database.insert(package[0], time[0], "loading", lcfenv, "no")
        else:
            database.update(time[0],result[0])
    else:
         database.insert(package[0], time[0], "loading", lcfenv, "no")
    print package[0]
    print time[0]
    #print result[0]
    return ""

def reqtask():
    try:
        urllib2.urlopen("http://172.16.16.18:9999/job/com.lcf.android.debug/build?token=lcfdebug")
    except:
        return "fail"
    return "success"

if __name__=="__main__":
    request("debug")