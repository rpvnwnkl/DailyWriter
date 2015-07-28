#!usr/bin/env python
import sys, logging

import re
import mechanize

logger = logging.getLogger('mechanize')
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG)

br = mechanize.Browser()
br.set_debug_http(True)
br.set_debug_responses(True)
br.set_debug_redirects(True)

br.open("https://750words.com/auth")

email = open('email.txt', 'r').read()
password = open('password.txt', 'r').read()

br.select_form(nr=0)
br['person[email_address]'] = 'rpvnwnkl@gmail.com'
br['person[password]'] = 'password'
response2 = br.submit()

print br.title
print response2.geturl()
print response2.info()
print response2.read()

wordFile = open('testwords.txt', 'r')
words = wordFile.read()

br.select_form(nr=0)
print br['entry[body]']
br.set_value(words, kind='text', nr=8)
print br['entry[body]']

br.open('http://750words.com/autosave')
print br.geturl()
br.open('https://750words.com/auth/logout')
print br.geturl()

wordFile.close()
