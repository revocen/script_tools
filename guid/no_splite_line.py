import uuid
import pyperclip

pyperclip.copy(str(uuid.uuid1()).replace('-',''))