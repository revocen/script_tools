
# 用于获取剪贴板上所有符合要求的字符串

import re
import pyperclip


target = pyperclip.paste()

reg1 = re.compile(r'"ftp.+\.rmvb"')

links = reg1.findall(target)

result = ''
for item in links:
    item = item.replace('\"','')
    result += item + '\r\n'
    # print(item)

print(result)
pyperclip.copy(result)