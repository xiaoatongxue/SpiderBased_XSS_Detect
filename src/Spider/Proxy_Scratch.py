# -*- coding:utf-8 -*-
import Queue
import code
import httplib
import os
import re
import socket
import sys
import time
import urllib
import urllib2

import MySQLdb
from bs4 import BeautifulSoup
from tld import get_tld 


reload(sys)
sys.setdefaultencoding( "utf-8" )

timeout = 10    
socket.setdefaulttimeout(timeout)


s=[]

ip_list=set(s)
port_list=['80','81','82','843','1080','21']
test_url=['http://7.leiphone.com/','http://www.people.com.cn/','http://www.mafengwo.cn/','http://www.quwan.com/','http://opinion.people.com.cn/GB/70240/','http://www.zgwlsg.com/','http://www.qyer.com/']
available_ip_list=set(s)

q=Queue.Queue()
#url = 'http://www.kjson.com/proxy/index/'
url="http://www.kjson.com/proxy/?fm=map" 
url_set=set([url])
page=2

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'


#pattern=re.compile("(?<=\/proxy\/index\/)\d+")




def getURL(url):
    global total_item
    global url_set
    global page
    try:
       # headers={'Referer':url}
        headers = { 'User-Agent' : user_agent ,'Referer':url}
        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request,timeout=30)
        data=response.read()
        #print data
        #data=unicode(data,'gb2312','ignore').encode('utf-8','ignore')
        soup=BeautifulSoup(data)
       # print soup.prettify()
        
       # print soup.find_all("a", class_='test')
        #print soup.a['href']

       # print soup.find_all("tr", class_='gradeA')
        
        i=0
#         for url in soup.find_all("tr",class_="gradeA"):
#             #print(url.get('href'))
#             #print url.find_all('td')
#             s.append(url.find_all('td'))
#             
#             
#             """temp=re.match(pattern, s[0][3])
#             if temp:
#                 print temp.group()
#             else:
#                 print 'lalal'"""
#                 
#                 
#             print s[0][3].string
#             print len(s)
#             break
            #print url.td.find_all_next()
            #print soup.a['href']  
        for url in soup.find_all("td", text="high"):
            ip=url.parent.find('td').string
            ip_list.add(ip)
            print ip
            i=i+1
        
#         pattern=re.compile(r"a",re.S)
#         for link in soup.find_all("a",text="尾页"):
#             print type(link)
#             
#             h='alfjd'
#             print type(link.string)
#             print re.search(pattern, h)
        url='http://www.kjson.com/proxy/index/'+str(page)+r'/?fm=map'
        print url
        print "\n\n\n\n"
        page=page+1
        time.sleep(1)
        if page<30:
            getURL(url)
#             print page
#             print "\n\n\n\n"
            
            
        
        
        #return i
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason
            
    except socket.timeout:
        print "time out"
    
    """except httplib.BadStatusLine: '' as e:
        if hasattr(e,"reason"):
            print e.reason
        else:
            print 'hehe'"""
            
if __name__=='__main__':
    
    getURL(url)
    
    count=0
    j=0
    
    print len(ip_list)

    
    with open("proxy.txt",'w') as f:
    #f=open("proxy.txt",'w')
       # while count<=5 and j<len(ip_list):
        k=0
        while j<len(ip_list): 
            t=ip_list.pop()
            proxy = {'http':r'http://%s:%s' %(t,port_list[0])}
            #print proxy
            
            try:
                proxy_support = urllib2.ProxyHandler(proxy)
                # opener = urllib2.build_opener(proxy_support,urllib2.HTTPHandler(debuglevel=1))
                opener = urllib2.build_opener(proxy_support)
                urllib2.install_opener(opener)
                
                headers = { 'User-Agent' : user_agent ,'Referer':test_url[k]}
                request = urllib2.Request(test_url[k],headers=headers)
                response = urllib2.urlopen(request,timeout=20)
                
                print test_url[k]
                #count=count+1
                available_ip_list.add(t)
                f.write(t)
                f.write('\n')
                #time.sleep(1)
                
            except urllib2.URLError, e:
                #print 'al'
                continue
            except socket.timeout:   
                #print "time out"
                continue
            except socket.error:
                #print "socket.error"
                continue
            except httplib.BadStatusLine as e:
                if hasattr(e,"reason"):
                    print e.reason
                else:
                    #print 'hehe'
                    pass
                continue
            except :
                continue
            finally:
                j=j+1
                k=k+1
                if k>=7:
                    k=0
                
                
        
    #f.close()
    print len(available_ip_list)
    #print response.code
    
            
    
    