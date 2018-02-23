from tkinter import *
import main_file
import tkinter.font as tkFont
root = Tk()
root.title('有道翻译插件桌面版------xiantang')
root.geometry('600x300')
ft_big = tkFont.Font(family='Helvetica', size=20, weight=tkFont.BOLD)
ft_small = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD)
# w = Label(root, text="输入需要翻译的文本:", fg="black").grid(row=0)

Label(root, text="有道翻译插件桌面版",font=ft_big).pack()


def play():
    if var_3000.get()==1 and var_all.get()!=1:
        content=e1.get()
        if content:
            txt.insert(END, '正在翻译请稍等.......\n')
            Ts=main_file.Thanslate()
            content=Ts.split_sentence(content)
            txt.insert(END,content+'\n')
            txt.insert(END, '\n')
    elif var_all.get()==1 and var_3000.get()!=1:
        content=e1.get()
        if content:
            txt.insert(END, '正在翻译请稍等.......\n')
            Ts = main_file.Thanslate()
            content=Ts.thanslate(content)
            txt.insert(END,content+'\n')
            txt.insert(END, '\n')
        else:
            pass

def clear():
    txt.delete(0.0, END)
    e1.delete(0,END)
    var_all.set(0)
    var_3000.set(0)

#输入框
e1 = Entry(root,font=ft_big)
e1.pack(fill=X,padx=10)


#按钮
button_clear = Button(root,text = "clear",command=clear,font=ft_small)
button_clear.pack(side=RIGHT)
button_paly = Button(root,text = "play",command=play,font=ft_small)
button_paly.pack(side=RIGHT)


#选择控件
var_all=IntVar()
button_check=Checkbutton(root,text="全文",variable=var_all,font=ft_small)
button_check.pack(side=RIGHT)


var_3000=IntVar()
button_check=Checkbutton(root,text="3000",variable=var_3000,font=ft_small)
button_check.pack(side=RIGHT)


#Text 文本框
txt = Text(root,font=ft_small)
txt.pack(fill=X,padx=10,pady=10)

mainloop()

