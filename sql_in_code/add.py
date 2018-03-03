
import re
import pyperclip

target = pyperclip.paste()

array = target.splitlines()

regexStart = re.compile('^( )*')
regexTab = re.compile('\t')

result = '""'

for item in array:
    temp = regexStart.sub('+ "',item)
    temp = regexTab.sub('   ',temp)
    result += '\r\n' + temp + ' "'

result += "\r\n;"
pyperclip.copy(result)