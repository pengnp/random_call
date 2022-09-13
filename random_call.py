import random
import pandas as pd
from tkinter import *
import threading


class Demo:

    def __init__(self):
        self.user_list = pd.read_excel('./学生表.xlsx').姓名.tolist()
        self.windows = Tk()
        self.start = True
        self.stop = True
        self.index = ''
        self.label_var = StringVar(value='XXXXX')
        self.button_var = StringVar(value=f'开始')

    def ui(self):
        self.windows.resizable()
        self.windows.title('班级点名')
        width, height = 480, 455
        scree_width = (self.windows.winfo_screenwidth() - width) // 2
        scree_height = (self.windows.winfo_screenheight() - height) // 2
        self.windows.geometry(f'{width}x{height}+{scree_width}+{scree_height}')
        Label(self.windows, textvariable=self.label_var, font=('微软雅黑', 60), height=4, background='grey').pack(side=TOP, fill='x')
        Button(self.windows, textvariable=self.button_var, font=('微软雅黑', 20), command=lambda: self.thread(self.show_name)).pack(side=TOP, fill='x')
        self.windows.mainloop()

    def thread(self, function):
        th = threading.Thread(target=function)
        th.daemon = True
        th.start()

    def show_name(self):
        if self.start:
            self.button_var.set(f'暂停')
            self.start = False
            while self.stop:
                if len(self.user_list) == 0:
                    self.user_list = pd.read_excel('./学生表.xlsx').姓名.tolist()
                self.index = random.randint(0, len(self.user_list) - 1)
                self.label_var.set(self.user_list[self.index])
            if not self.stop:
                self.stop = True
                del self.user_list[self.index]
                self.button_var.set(f'开始（剩余{len(self.user_list)}）')
        else:
            self.start = True
            self.stop = False


if __name__ == '__main__':
    Demo().ui()







