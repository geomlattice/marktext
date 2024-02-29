import pyperclip

message = pyperclip.paste()
newline_strike = message.replace("\n", " ")
pyperclip.copy(newline_strike)
