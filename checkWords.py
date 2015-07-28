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
print email, password
br.select_form(nr=0)
br['person[email_address]'] = 'rpvnwnkl@gmail.com'
br['person[password]'] = 'password'
response2 = br.submit()
print br.title
print response2.geturl()
print response2.info()
print response2.read()
print br.select_form(nr=0)
print br['entry[body]']

