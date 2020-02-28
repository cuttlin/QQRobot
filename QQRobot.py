import win32gui
import win32con
import win32clipboard as w
import time
from tkinter import *
from tkinter import messagebox

def getText():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_UNICODETEXT)
    w.CloseClipboard()
    return d

def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()

def send_qq(to_who, msg):
    setText(msg)
    qq = win32gui.FindWindow(None, to_who)
    win32gui.SendMessage(qq, 258, 22, 2080193)
    win32gui.SendMessage(qq, 770, 0, 0)
    win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32gui.SendMessage(qq, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

def timing():
    time_input = []
    time_input.append(year.get())
    time_input.append(month.get().zfill(2))
    time_input.append(day.get().zfill(2))
    time_input.append(hour.get().zfill(2))
    time_input.append(minute.get().zfill(2))
    time_input.append("00")

    time_set = (time_input[0], time_input[1], time_input[2], time_input[3], time_input[4], time_input[5])

    while True:

        time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

        if "%s-%s-%s %s:%s:%s" % time_set == time_now:
            return "时间到，正在发送消息。"

        time.sleep(1)

def send():
    if var.get() is True:
        timing()
        time.sleep(2)  
    try:
        send_qq(user.get(), msg.get())
        messagebox.showinfo("successful","发送成功")
    except:
        messagebox.showerror("error", "发送失败")

win = Tk()
Label(text="欢迎使用~(￣▽￣~)~").pack()
user = Entry()
user.pack()
Label(text="info").pack()
msg = Entry()
msg.pack()
Label(text="year").pack()
year = Entry()
year.pack()
Label(text="month").pack()
month = Entry()
month.pack()
Label(text="date").pack()
day = Entry()
day.pack()
Label(text="hour").pack()
hour = Entry()
hour.pack()
Label(text="min").pack()
minute = Entry()
minute.pack()
var = BooleanVar()
checkbutton = Checkbutton(text="true?", onvalue="True", variable=var)
checkbutton.pack()
Button(text="发送", command=send).pack()
win.mainloop()
