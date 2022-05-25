from tkinter import *
from tkinter.ttk import *
import random
import codecs

Name = ''
Group = ''
A0=3
Points=0
N=1

def results():
    def window_main():
        window_results.destroy()
        result_summa = 0
        main()

    window_results = Tk()
    window_results.title("Ваш результат ")
    window_results.geometry('265x130')
    global Points
    
    T1 = Label(window_results,text=f'Ви відповіли првильно на {Points} питань')
    T2 = Label(window_results,text=str(int(Points/17*100))+'%',font='Arial 60', foreground="red")
    T1.grid(column=0, row=0)
    T2.grid(column=0, row=1, sticky=S)
    window_results.mainloop()

def testing():
    def results_window():  # результаты
        window.destroy()
        results()
    def printQ():
        global Points, N
        def a(n):
            fn=f[n]
            if fn[0]=='*':
                fn=fn[1:]
            return fn
        n=(N-1)*5
        Nl.configure(text = str(N))
        Pointl.configure(text = "Балів  " + str(Points))
        Q.configure(text = f[n])
        R1.configure(text = (a(n+1)))
        R2.configure(text = (a(n+2)))
        R3.configure(text = (a(n+3)))
        R4.configure(text = (a(n+4)))
        i=[2, 3, 4, 5]; random.shuffle(i)
        R1.grid(row = i[0])
        R2.grid(row = i[1])
        R3.grid(row = i[2])
        R4.grid(row = i[3])
        
    def NextQ():
        def a(n):
            fn=f[n]
            if fn[0]=='*': fn=fn[1:]
            return fn
        global A0, Points, N
        if Answer.get()==A0: Points+=1
        n=(N-1)*5
        N+=1
        if N<18:
            for i in range(1,5):
                I=f[i+n+5]
                if I[0]=='*': A0=i
            Answer.set(0)
            printQ()
        else: results_window()
        
    global Name, Group
    
    window = Tk()
    window.title("Тестування")
    window.geometry('500x300')

    #шапка
    N=1
    Nvl=Label(window, text="Питання №")
    Nl=Label(window, text=str(N))
    Namel=Label(window, text=Name)
    Groupl=Label(window, text=Group)
    Pointl=Label(window, text="Балів  " + str(Points))
    Nvl.grid(column=0, row=0, sticky=W)
    Nl.grid(column=1, row=0, sticky=W)
    Namel.grid(column=3, row=0, sticky=W)
    Groupl.grid(column=4, row=0, sticky=W)
    Pointl.grid(column=5, row=0, sticky=W)

    #открытие файла и перенос в массив
    test = codecs.open('question.txt', 'r', encoding='utf-8')
    f=[]
    for i in test:
        f.append(i)
    
    Answer = IntVar(); A0=3
    
    Q = Label(window)
    Q.grid(column=1, row=1, columnspan=5, sticky=W)

    R1 = Radiobutton(window, variable=Answer, value=1, command=NextQ)
    R2 = Radiobutton(window, variable=Answer, value=2, command=NextQ)
    R3 = Radiobutton(window, variable=Answer, value=3, command=NextQ)
    R4 = Radiobutton(window, variable=Answer, value=4, command=NextQ)
    R1.grid(column=1, sticky=W, columnspan=5)
    R2.grid(column=1, sticky=W, columnspan=5)
    R3.grid(column=1, sticky=W, columnspan=5)
    R4.grid(column=1, sticky=W, columnspan=5)

    printQ()
    
    btn = Button(window, text="Закінчити тестування", command=results_window)
    btn.grid(column=5, row=6)

    window.mainloop()


def main():
    def testing_begin():
        global Name, Group
        Name=HiTxt1.get()
        Group=HiTxt2.get()
        window.destroy()
        testing()

    window = Tk()
    window.title("Реєстрація")
    window.geometry('250x100')

    l1 = Label(window, text="ПІБ", width=10)
    l2 = Label(window, text="група", width=10)
    HiTxt1=Entry(window)
    HiTxt2=Entry(window)
    l1.grid(row=0, column=0, sticky=W)
    l2.grid(row=1, column=0, sticky=W)
    HiTxt1.grid(row=0, column=1, sticky=W)
    HiTxt2.grid(row=1, column=1, sticky=W)

    btn = Button(window, text="Почати тестування", command=testing_begin)
    btn.grid(column=1, row=2)

    window.mainloop()

main()
