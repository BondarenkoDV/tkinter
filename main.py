import tkinter as tk
import random
from tkinter import messagebox as mb

count = 0


def clicker():
    global count
    root['bg'] = f'#{random.choice(range(100000, 999999))}'
    count += 1
    btn1['text'] = f'Кликер\nКоличество нажатий:{count}'


def reset():
    global count
    root['bg'] = f'#000000'
    count = 0
    btn1['text'] = f'Кликер\nКоличество нажатий:{count}'


def dialog():
    question = mb.askyesno(title='Программа', message='Собираетесь идти в университет?')
    if question:
        mb.showinfo('Программа', 'Удачи на парах')
        quit()
    else:
        question2 = mb.askyesno(title='Программа',
                                message='Это может привести к отчислению. Вы пойдете на пары?')
        if question2:
            mb.showinfo('Программа', 'Вы сделали верный выбор')
            quit()
        else:
            mb.showinfo('Программа', 'Вы наигрались! Срочно в деканат!')
            quit()


root = tk.Tk()
root.title('Программа')
root['bg'] = f'#000000'
root.wm_attributes('-alpha', 0.9)
root.geometry('280x110+450+200')
root.resizable(False, False)


btn1 = tk.Button(root,
                 text=f'Кликер\nКоличество нажатий:{count}',
                 font=('Arial', 14, 'bold'),
                 padx=10,
                 pady=10,
                 width=20,
                 height=2,
                 command=clicker,
                 )

btn2 = tk.Button(root,
                 text='Сброс',
                 font=('Arial', 14, 'bold'),
                 padx=10,
                 pady=10,
                 width=10,
                 height=2,
                 command=reset,
                 bg='white',
                 )
btn3 = tk.Button(root,
                 text='Диалог',
                 font=('Arial', 14, 'bold'),
                 padx=10,
                 pady=10,
                 width=20,
                 height=2,
                 command=dialog,
                 bg='white')

btn1.grid(row=0, column=0, stick='e')
btn2.grid(row=0, column=1)
btn3.grid(row=1, column=0)

root.mainloop()
