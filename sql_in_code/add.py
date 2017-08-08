
import re
import pyperclip

target = pyperclip.paste()

array = target.splitlines()

regexStart = re.compile('^\s+')

result = ''

for item in array:
    result += '\r\n\t\t\t\t' + regexStart.sub('+ "',item) + ' "'

pyperclip.copy(result)