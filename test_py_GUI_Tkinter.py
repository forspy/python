# 要使用python的GUI必须导入tkinter模块，使用GUI需要安装GUI工具包
# 实现一个简单的文本打开编辑器
# 使用方法，先save 创建一个.txt，然后open
from tkinter import *
from tkinter.scrolledtext import ScrolledText  # 多行可滚动文本区域


def load():
    with open(filename.get()) as file:  # 使用with来自动打开和关闭一个文件
        contents.delete('1.0', END)
        contents.insert(INSERT, file.read())


def save():
    with open(filename.get(), 'w') as file:
        file.write(contents.get('1.0', END))


top = Tk()
top.title('Simple Editor')
contents = ScrolledText()
contents.pack(side=BOTTOM, expand=True, fill=BOTH)  # pack()布局管理

filename = Entry()
filename.pack(side=LEFT, expand=True, fill=X)

Button(text='Open', command=load).pack(side=LEFT)  # 使用回调函数
Button(text='Save', command=save).pack(side=LEFT)


# 要添加事件处理程序，可使用方法bind
# 以下为测试方法，将鼠标点击事件和输出函数绑定
def callback(event):
    print(event.x, event.y)


print(top.bind('<Button-1>', callback))
##############
mainloop()  # 主事件循环 阻塞在这儿
