# -*- coding:utf-8 -*-
import Queue
import StringIO
import code
from cookielib import domain_match
import gzip
import httplib
import os
import random
import re
import socket
import sys
import threading
import time
import urllib
import urllib2

import MySQLdb
from bs4 import BeautifulSoup
import chardet 
from tld import get_tld 

# from Spider.URL_Scratch import page


# from bsddb.test.test_all import charset
reload(sys)
sys.setdefaultencoding( "utf-8" )

timeout = 1    
socket.setdefaulttimeout(timeout)

#global times
global len1
global url_set
#total_item=0

q=Queue.Queue()
#url = 'http://www.douban.com/'
url='http://www.people.com.cn/'
# url='http://www.juzimi.com/'
#url='http://download.csdn.net/' 
#url='http://www.huaban.com/'
# url='http://www.xcar.com.cn/'
# url='http://sports.sohu.com/'
# url='http://www.qidian.com/Default.aspx/'
# url='http://military.china.com/zh_cn/'
# url='http://www.ithome.com/'
# url='http://tieba.baidu.com/'

url_set=set([url])
localFile='url.txt'
myfile=open(localFile,'w')
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'
ip=[ ]
proxy_ip_index=0



def get_proxy():
    global ip
    with open('proxy.txt') as f:
        for proxy_ip in f.readlines():
            ip.append(proxy_ip.strip('\n'))
            
        
    
    
    
    #ip='117.136.234.8'
def set_proxy():
    
    m=random.randint(0,len(ip)-1)
    proxy = {'http':r'http://%s:80' %ip[m]}
    proxy_support = urllib2.ProxyHandler(proxy)   
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)
    
    
    
#     try:
#         headers={'User-Agent' : user_agent,'Referer':url}
#         request = urllib2.Request(url,headers = headers)
#         response = urllib2.urlopen(request,timeout=30)
#         data=response.read()
#         
#         data=unicode(data,'gb2312','ignore').encode('utf-8','ignore')
#         #print data
#         soup=BeautifulSoup(data)
#         
#     
#     except urllib2.URLError, e:
#         if hasattr(e,"code"):
#             print e.code
#             print 'zzzzzzzzz'
#         if hasattr(e,"reason"):
#             print e.reason
#             print 'aaaaaaaaa'
#     except socket.error:
#         errno, errstr = sys.exc_info()[:2]
#         if errno == socket.timeout:
#             print "There was a timeout22"
#         else:
#             print "There was some other socket error22"




def getURL(url):
    i=0
    #original_url=url
    global url_set
    global proxy_ip_index
    global is_limit_frequence
    global url_name
    global domain
    global num,total,deep_length,deep_n_link
    global threadLock
    global FLAG
    global n
    
#     print 'nnvnvnvnvnvn'
    while True:
        try:
            #time.sleep(1)
            if is_limit_frequence==True:
                #print 'aaznhg'
                set_proxy()
            #print 'nnnnnnnnnnnn'
            
            #url="http://"+url    
            #print url    
                
            
            headers={'User-Agent' : user_agent,'Referer':url,'X-Forwarded-For':'10.0.0.1'}
            request = urllib2.Request(url,headers = headers)
            response = urllib2.urlopen(request,timeout=5)
            #print response.info().getmaintype()
            #print response.info().getplist()
    #         print url
            charset=response.info().getparam('charset')
    #         if charset!=None:
    #             print charset,'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww'
            data=response.read()
            
            threadLock.acquire()
            print url
            myfile.write(url)
            myfile.write('\n')
            num=num+1
            threadLock.release()
            
            if num==total:
                try:
                    sys.exit()
                except SystemExit,e:
                    print u'共抓取连接数：'+total
    #                     return 
    #                 t_end = time.time()    
    #                 print 'the thread way take %s s' % (t_end-t_start)
                    
                    
                    #退出程序
                    os._exit(0)
                    #退出子线程
    #                 exit()
            
            #myfile.write('\r\n')
            #q.put(url)
            
            
            if charset==None:
                charset=chardet.detect(data)['encoding']
#                 charset=re.search(re.compile(r"<head>(.*)<meta([^>]*)charset=\"([^\"]*)\"",re.S|re.I), data)
#                 if charset!=None:
#                     charset=charset.group(3)
#                     print charset+'e'
#                     #data=unicode(data,charset,'ignore').encode('utf-8','ignore')
#                 else:
#                     charset=re.search(re.compile(r"<head>(.*?)content=[\"](.*?)charset=([^\"]*)[\"]",re.S|re.I), data)
#                     if charset!=None:
#                         charset=charset.group(3)
#                         print charset+'w'
#                     else:
#                         #charset='utf-8'
#                         
#                         chardit1 = chardet.detect(data)
#                         charset=chardit1['encoding'] # baidu
#                     
#                     print charset+'qw'   
#                     url=re.search(re.compile(r"<meta(\s)+http-equiv=\"REFRESH\".*url=([^\"]*)\"", re.S|re.I),data)
#                     if url!=None:
#                         url=url.group(2)
#                         #print url.group(2)
#                         #getURL(url.group(2))
#                         #q.get(block=True)
#                         
#                         threadLock.acquire()
#                         q.put(url)
#                         threadLock.release()  
#                         
#                         if url!=None and domain==get_tld(url,fail_silently=True):
#                     
#                             if url not in url_set:
#                                 url_set.add(url)
#                                 q.put(url)
#                                 i=1
                        
    #                     return i
    #                 print data
    
#             else:
#                 print charset
               
              
            data=unicode(data,charset,'ignore').encode('utf-8','ignore')
    #         print  
    #         print data
    
    #         try:
    #             data=unicode(data,charset,'ignore').encode('utf-8','ignore')
    #         except LookupError:
    #             print 'gsef'
    #             return 0
                 
            #print data
    #         print '\n\n\n'
            #data=unicode(data,'gb2312','ignore').encode('utf-8','ignore')
            
        
            i=0
            
    #         data = StringIO.StringIO(data)
    #         gzipper = gzip.GzipFile(fileobj=data)
    #         data = gzipper.read()
#             threadLock.acquire()
            soup=BeautifulSoup(data)
    #         print soup。__str__('GBK')
    #         print soup.__str__('GBK')
            
            
            for url in soup.find_all('a'):
                #print(url.get('href'))
                #try:
                    
                    url=url.get('href')
                    
                    #request = urllib2.Request(url,headers = headers)
                    #f=urllib2.urlopen(request)
                    #if f.code==200:
                    if url!=None:
                        temp=re.match(re.compile(r"^/(.*)", re.S), url)
                        if temp!=None:
                            #print temp.group(0)
                            url=url_name+temp.group(1)
    #                         print url+'oooooooooooooo'
                        if  domain==get_tld(url,fail_silently=True):
                            
                            if url not in url_set:
                                
                                threadLock.acquire()
                                url_set.add(url)
                                
                                
                                q.put(url)
                                deep_length=deep_length+1
        #                         myfile.write(url)
        #                         myfile.write('\r\n')
        #                         print url
                                i=i+1
                                
                                threadLock.release() 
                                
            if deep_length>n and FLAG==True:
#                 threadLock.release() 
                return 
            
#             else:
#                 print '[[[[[[[[['
#             print deep_length
#                     deep_n_link=deep_n_link-1         
#                     if deep_n_link==0:
#                         for i in range(n):
#                             url=q.get(block=True)
#                             threads.append(threading.Thread(target=getURL,args=(url,)))
#                                 threadLock.release() 
                            #total_item=total_item+1
    #             except socket.error:
    #                 errno, errstr = sys.exc_info()[:2]
    #                 if errno == socket.timeout:
    #                     print "There was a timeout11"
    #                     continue
    #                 else:
    #                     print "There was some other socket error11"
    #                     continue
    #             except httplib.BadStatusLine as e:
    #                 if hasattr(e,"reason"):
    #                     print e.reason
    #                     pass
    #                 else:
    #                     print 'BadStatusLine'
    #                     #print 'hehe'
    #                     pass
    #                 continue 
#             threadLock.release()          
        
        except socket.error:
            errno, errstr = sys.exc_info()[:2]
            pass
    #         if errno == socket.timeout:
    #             print "There was a timeout22",url
    #              
    #         else:
    #             print "There was some other socket error22"   
        
        
        except urllib2.URLError, e:
            if hasattr(e,"code"):
                #print e.code
                #print 'zxxxxxzzzz'
                
                if e.code=='403':
                    is_limit_frequence=True
                 #   print is_limit_frequence
                    print 'hehe'
    
                    #getURL(url)
            if hasattr(e,"reason"):
                is_limit_frequence=True
                print e.reason
                print 'aarrrraaaaa'
                if e.reason=='Forbidden':
                    pass
    #                 return getURL(url)
               # is_limit_frequence=True
                
                 
                #getURL(url)
        
        except httplib.BadStatusLine as e:
            
            if hasattr(e,"reason"):
                print e.reason
            else:
                print 'www'
            #pass 
      
        
    
        except ValueError:
            print url
    #         if proxy_ip_index==0:
    #             proxy_ip_index=len(ip)-1
    #         else:
    #             proxy_ip_index=proxy_ip_index-1
    
            print 'value error'
            
#         print 'qqqqqqqqqq'+url
        
        url=q.get()
          
        #print(soup.prettify())
        #link_list =re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')" ,data)
        #link_list =re.findall(r"(?<=href=\")^(javascript)(.+?)(?=\")|(?<=href=\')^(javascript)(.+?)(?=\')" ,data)
        #i=0
        #for url in link_list:
        #    print url
        #   if domain==get_tld(url):
        #        q.put(url)
        #        i=i+1
        
    #print 'qqqq'
#     return i
    
# def extractURL(data):
#     
#     soup=BeautifulSoup(data)
#     for url in soup.find_all('a'):
#         #print(url.get('href'))
#         try:
#             url=url.get('href')
#             #request = urllib2.Request(url,headers = headers)
#             #f=urllib2.urlopen(request)
#             #if f.code==200:
#             if url!=None and domain==get_tld(url,fail_silently=True):
#                 
#                 if url not in url_set:
#                     url_set.add(url)
#                     q.put(url)
#                     myfile.write(url)
#                     myfile.write('\r\n')
#                     print url
#                     i=i+1
#                     total_item=total_item+1
#         except socket.error:
#             errno, errstr = sys.exc_info()[:2]
#             if errno == socket.timeout:
#                 print "There was a timeout11"
#                 continue
#             else:
#                 print "There was some other socket error11"
#                 continue
#         except httplib.BadStatusLine as e:
#             if hasattr(e,"reason"):
#                 pass
#             else:
#                 #print 'hehe'
#                 pass
#             continue
#         
#         
#         
#         return i
    
            
if __name__=='__main__':
    
    is_limit_frequence=False
    time1=time.time()
    deep=3
    deep_length=0
    deep_n_link=1
    FLAG=True
    global domain
    global url_name
    domain=get_tld(url)
    #url=url.replace("http://","")
    url_name=url
    total=1000
    num=0
    n=10
    
    threadLock = threading.Lock()
    
    global total_item
    total_item=0
    
    total_length=0
    
    get_proxy()
    
#     length=getURL(url)
#     
#     if length==0:
#         getURL(url)
#     
#     
#     d={url:length}
    
#     total_length=length
    
    getURL(url)
#     print'zzzzzz'
    threads = []
    FLAG=False
    for i in range(n):
#         print 'bbb mmmmm'
        url=q.get(block=True)
        threads.append(threading.Thread(target=getURL,args=(url,)))
        threads[i].setDaemon(True)
        threads[i].start()
#         print 'ccccc'
#         if i==n-1:
#             print 'nnnnnoo'
#         threads[i].join()
        
#         print 'cvcvbxb'
        
#         if i==n-1:
#             print 'ooo'
        
#     print 'eeeeeee'
        
    
        
#     for t in threads:
#         t.setDaemon(True)
#         t.start()
#         
    for t in threads:
        t.join()
    
#     k=0
#     while deep>0:
#         #length=d[url]
#         length=total_length
#         total_length=0
#         while length>0:
#             url=q.get(block=True)
#             temp_length=getURL(url)
#             if temp_length!=0:
#                 d[url]=temp_length
#                 total_length+=temp_length
#             length=length-1
#         deep=deep-1
        
    myfile.write(str(len(url_set)))
    myfile.close()
    #print total_item
    print time.time()-time1
    
