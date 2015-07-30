
#!usr/bin/env python
import sys, logging

import re
import mechanize
import urllib

logger = logging.getLogger('mechanize')
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG)

br = mechanize.Browser()
br.set_debug_http(True)
br.set_debug_responses(True)
br.set_debug_redirects(True)



##cookies = mechanize.CookieJar()
##opener = mechanize.build_opener(mechanize.HTTPCookieProcessor(cookies))
##headers = [("Accept"," text/javascript, application/javascript, */*"),\
  ##          ("Accept-Encoding","gzip, deflate"),\
    ##        ("Accept-Language","en-US,en;q=0.5"),\
      ##      ("Connection","keep-alive"),\
        ##    ("Host","750words.com"),\
          ##  ("Referer","https://750words.com/"),\
            ##("DNT", '1'),\
       ##     ("Content-Type", 'application/x-www-form-urlencoded; charset=UTF-8'),\
         ##   ("x-requested-with:", "XMLHttpRequest"),\
           ## ("Content-Length", "1000"),\
         ##   ("Accept-Charset","ISO-8859-1,utf-8;q=0.7,*;q=0.7"),\
           ## ("Cookie:", "_bigcheckin.com_session=73aeb61c2f5a108efd5f3a91cccc82aa; amplitude_id=eyJkZXZpY2VJZCI6ImFiODgxZmZhYzI1MjAyYWQ2MTlhOGM2MTBmZmMyNDc4IiwidXNlcklkIjoiMjg2ODUwIiwiZ2xvYmFsVXNlclByb3BlcnRpZXMiOnsibmFtZSI6Ik1hdGggTWlsbHMiLCJjcmVhdGVkX2RhdGUiOiIyMDE1LTA3LTI4IiwiZ2VuZGVyIjoiIiwicGF0cm9uIjoiZmFsc2UiLCJsaWZldGltZV9hY2NvdW50IjoiZmFsc2UiLCJudW1fY29tcGxldGVkX2VudHJpZXMiOiIwIiwibW9udGhseV9jaGFsbGVuZ2VyIjoiZmFsc2UifX0="),\
           ## ("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0) Gecko/20100101 Firefox/5.0")]
##opener.addheaders = headers
##mechanize.install_opener(opener)
##params = urllib.urlencode({'LN':'myLN','BC':'myBC','INST':'myINST',\
           ##                        'req':'db','key':'PROXYAUTH','lib':'8',\
             ##                                                 'url':'http://eebo.chadwyck.com/search'})
##mechanize.urlopen("https://www.aladin.wrlc.org/Z-WEB/PATLogon",params)

##cj = mechanize.CookieJar()

request1 = mechanize.Request('https://750words.com/auth')
response1 = mechanize.urlopen(request1)

br.open("https://750words.com/auth")

email = open('email.txt', 'r').read()
password = open('password.txt', 'r').read()

br.select_form(nr=0)
br['person[email_address]'] = 'rpvnwnkl@gmail.com'
br['person[password]'] = 'password'
##response2 = br.submit()
br.submit()
print br.title
##print response2.geturl()
##print response2.info()
##print response2.read()
wordFile = open('testwords.txt', 'r')
words = wordFile.read()

br.select_form(nr=0)
br.set_all_readonly(False)
entryID = br['entry[id]']
##br['entry[record_version]'] = str(int(br['entry[record_version]'])+1)
br['entry[num_words]'] = str(len(words))
br['entry[body]'] = words
rvValue = br['entry[record_version]']
##br['v'] = 'ctrls'
##br['rv'] = 
##br.set_value(words, kind='text', nr=8)
print br['entry[body]']
data1='entry[id]=4876827&entry[num_words]=5&entry[body]=hello%20mudda%20fadda%20grandma%20gradmaadlsldskadda&v=ctrls&rv=13'
param = ("entry[id]=" + entryID + "&entry[num_words]=" + str(len(words))+ "&entry[body]=" + words + "&v=ctrls&rv=" + rvValue)
params = urllib.urlencode({'entry[id]':entryID, 'entry[num_words]':str(len(words)), 'entry[body]':words, 'v':'ctrls', 'rv':'0'})
print params
br.click()
print br['entry[num_words]']
##print br.controls
##print mechanize.add_cookie_header.__doc__
##request = mechanize.Request('https://750words.com/autosave', params)
##ckey = cj.cookies_for_request(request)
##print cj._cookie_attrs(ckey)
##response = mechanize.urlopen(request)
br.set_cookie(data1)
br.open('https://750words.com/autosave')
print br.response()
print br.response().info()
br.open(request)
##mechanize.urlopen('https://750words.com/autosave', params)
##print br.geturl()
##br.submit()
##br.follow_link(nr=0)
##br.back()

##br.open('https://750words.com/auth/logout')
print br.geturl()

wordFile.close()
