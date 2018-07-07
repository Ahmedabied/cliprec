#!/usr/bin/python
import pyperclip,time,os.path
def record():
    day=time.strftime("%d:%m:20%y.txt")
    if not os.path.exists(day):open(day,"+x")
    while 1:
        tmp_value=pyperclip.paste()
        open(day,"+a").write(str("\n______________________________________\n"+tmp_value+time.strftime("  %H:%m %p")+"\n")+"\n______________________________________\n")
        while tmp_value==pyperclip.paste():time.sleep(0.309)
record()
