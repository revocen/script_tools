# python 3.x
# utf-8

import base64
import re
import pyperclip
import chardet


thunder_header = 'thunder://'
thunder_prefix = 'AA'
thunder_subfix = 'ZZ'


def thunder2real(url):
    url = url[len(thunder_header):]

    url = base64.b64decode(url)
    code = chardet.detect(url)
    print('url编码方式为 -> %s' % code)

    url = url.decode(code['encoding'])

    url = url[len(thunder_prefix):-len(thunder_subfix)]

    return url


url = pyperclip.paste()
url = thunder2real(url)

print('解析后地址 -> %s' % url)
pyperclip.copy(url)
