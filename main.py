# Author: Jinger
# Myblog: https://hubojing.github.io/
# Project Link: https://github.com/hubojing/JingSLink


from PIL import ImageGrab
import keyboard
from tkinter import *
from tkinter import ttk
import pyperclip

def calculate(*args):
    try:
        value = inputval.get()
        imgname.set(value)
    except ValueError:
        pass

if __name__ == '__main__':
    # 键盘监听
    keyboard.wait(hotkey='ctrl+alt+a')
    keyboard.wait(hotkey='ctrl')

    # 弹框命名
    root = Tk()
    root.title("JingSLink")
    root.wm_attributes('-topmost', 1)
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    inputval = StringVar()
    input_entry = ttk.Entry(mainframe, width=7, textvariable=inputval)
    input_entry.grid(column=2, row=1, sticky=(W, E))

    imgname = StringVar()
    ttk.Label(mainframe, textvariable=imgname).grid(column=2, row=2, sticky=(W, E))
    ttk.Button(mainframe, text="确认", command=lambda:[f() for f in [calculate, root.quit]]).grid(column=3, row=3, sticky=W)
    ttk.Label(mainframe, text="图片命名为（不带后缀）").grid(column=1, row=1, sticky=W)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    input_entry.focus()
    root.bind("<Return>", calculate)

    root.mainloop()
    name = imgname.get()

    # 读取截图
    image=ImageGrab.grabclipboard()
    imgpath = 'E:/hexo/source/images/'
    imgfullname = name + '.png'
    fullpath = imgpath + imgfullname
    print(fullpath)
    image.save(fullpath)

    # 复制相对路径
    pyperclip.copy('/images/' + imgfullname)


