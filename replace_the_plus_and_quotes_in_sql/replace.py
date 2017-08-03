# When I get sql from java, there's always many plus and double quotes in it.
# Delete them is too boring. So, tool it for quickly

import pyperclip
import re

target = pyperclip.paste()

reg1 = re.compile(r'\+\s*\"')
target = reg1.sub(' ', target)

reg2 = re.compile(r'\"')
target = reg2.sub(' ', target)

pyperclip.copy(target)
