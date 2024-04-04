from tkinter import *
import random

window=Tk()
window.title('Password Generator')
window.geometry('500x400')
window.configure(bg="#ffffff")


label1 = Label(window,text='Password Generator',font=('times new roman',25,'bold'),width=25,height=2,bg="#ADD8E6",fg="#36454F")
label1.place(x=10,y=2)


label3 = Label(window, text='Enter password length:',width=20,height=1,font='Ivy 12 bold',bg="#ffffff",fg="#36454F")
label3.place(x=30, y=110,)

label4 = Label(window, text='Generate password',width=20,height=1,font='Ivy 12 bold',bg="#ffffff",fg="#36454F")
label4.place(x=155, y=250)

'''
entry2 = Entry(window, width=20, font='Ivy 15')
entry2.place(x=200, y=140)
'''
entry2 = Entry(window, width=20, font='Ivy 15', bg='lightblue', fg='black', bd=2, relief='solid', selectbackground='skyblue')
entry2.config(highlightthickness=2, highlightcolor="blue", highlightbackground="lightblue", insertbackground="black")
entry2.place(x=230, y=100, height=40)

entry3 = Entry(window, width=20, font='Ivy 20', bg='lightblue', fg='black', bd=2, relief='solid', selectbackground='skyblue')
entry3.config(highlightthickness=2, highlightcolor="blue", highlightbackground="lightblue", insertbackground="black")
entry3.place(x=100, y=300, height=60)



def generate():

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbol = "@_"
    num = "0123456789"

    all = lower + upper + symbol + num

    n = int(entry2.get())

    password = "".join(random.sample(all, n))

    entry3.delete(0, END)
    entry3.insert(0, password)

icon = PhotoImage(file="gene.png")
button = Button(window, image=icon, bd=0, command=generate, bg="#ffffff", highlightthickness=0)
button.place(x=210, y=180)  # Adjust the x and y coordinates as needed



window.mainloop()