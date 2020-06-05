#!/usr/bin/env python
#-*- conding:utf-8 -*-

''' three python inter tool '''
print ("1 make a small download server")
print ("in pyton2")
print ("python -m SimpleHTTPServer")
print ("in python3")
print ("python -m http.server")
print ("")

print ("2 string convert to JSON")
print (''' echo '{"job": "devoloper", "name": "lmx", "sex": "male" }' | python -m json.tool ''')
print (''' echo '{ "address": {"province": "zhejiang", "city": "shanghai"}, "name": "feixiang.zhao", "sex": "male" }' | python -m json.tool ''')

print ("3 check the thire package")
print ("import {package_name}")
print ("import paramiko")
print ("python -c 'import paramiko'")

