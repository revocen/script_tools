# When I get sql from java, there's always many plus and double quotes in it.
# Delete them is too boring. So, tool it for quickly

import pyperclip

result = pyperclip.paste();
result = result.replace("+ \"","").replace("\"","")
pyperclip.copy(result)

print('Done')
