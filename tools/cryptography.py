import base64
import binascii
import codecs
from urllib.parse import urlencode
from urllib.parse import unquote

def b64e(s):
    return base64.b64encode(s.encode()).decode()

def b64d(s, altchars=None, validate=False):
    return base64.decode(s)

def hexe(s):
    return hex(s)

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