import time
import pyperclip

result_date = time.strftime('_%Y%m%d_01', time.localtime())

pyperclip.copy(result_date + '_revocen')

