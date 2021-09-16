import string
import random
import time
import webbrowser

opennum = int(input('Please Enter Number Of Images To Open: '))

def genstring(len = 6, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(len))

for _ in range(opennum):
    domain = 'http://prnt.sc/'
    prntid = genstring()
    webbrowser.open(domain + prntid, new = 0)
    time.sleep(3)