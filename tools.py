import base64
import codecs
from urllib.parse import urlencode
from urllib.parse import unquote

def b64e(s):
    return base64.b64encode(s.encode()).decode()

def b64d(s):
    return str(base64.urlsafe_b64decode(s), "utf-8")

def hexe(s):
    pass

def hexd(s):
    pass

def r13e(s):
    return codecs.encode(s, 'rot_13')

def r13d(s):
    return codecs.decode(s, 'rot_13')

def urle(s):
    return urlencode(s)

def urld(s):
    return unquote(s) 