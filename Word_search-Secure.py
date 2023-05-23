from tkinter import *
import random
import messagebox
import playsound
import time
diag=Tk()
playsound.playsound("Adventure-320bit.mp3",0)
diag.title("INPUT")
diag.configure(background="black")
ph2 = PhotoImage(file="word_search_bg.png")
ph=PhotoImage(file="word_search (2).png")
c1=Canvas(diag,width=1200,height=1000)
c1.pack(fill="y",expand=True)
c1.create_image(650,350,image=ph)
Labb=Label(diag,text="Enter number of words to find :",font=("Times New Roman",18,"italic"),background="orange",fg="brown")
labb1=c1.create_window(450,400,anchor="n",window=Labb)
#Labb.grid(row=0,column=0)
n_wor=0
def ii(nww,ph2,n_wor=int(5)):
    playsound.playsound("mixkit-retro-game-notification-212.wav", 0)
    n_wor=int(n_wor)
    root = Tk()
    print(n_wor)
    diag.destroy()
    fl = open("sgb-words.txt", "r")
    flstr = fl.readlines()
    root.title("WORD-SEARCH")
    root.configure(background="black")
    # n_wor=int(input())
    '''can1 = Canvas(root, width=1000, height=1000)
    can1.pack(fill="both", expand=True)
    can1.create_image(450, 350, image=ph2)'''
    mwid = max(15, n_wor + 2)
    Lee=Label(root,text="WORD-SEARCH", font=("Impact", 16, "italic"), background="black",fg="green")
    #leee1 = can1.create_window(1, 0, anchor="ne", window=Lee)
    Lee.grid(row=1,column=0,columnspan=1)
    e = Entry(root, width=20, background="black", fg="green", borderwidth=0)
    #leee1 = can1.create_window(0, 1, anchor="ne", window=e)
    e.grid(row=0, column=1, columnspan=1, pady=5, padx=5)
    i = 65
    sla = Label(root, text=(f"SCORE :"), height=2, font=("Times New Roman", 12, "bold"), background="black",
                fg="green")
    #leee1 = can1.create_window(0, mwid+2, anchor="ne", window=sla)
    sla.grid(row=0, column=mwid + 2)
    scc = Entry(root, background="black", fg="green",font=("Times New Roman", 15, "italic"), width=2, borderwidth=0)
    #leee1 = can1.create_window(0, mwid+3, anchor="ne", window=scc)
    scc.grid(row=0, column=mwid+3, pady=2, padx=2,columnspan=1)
    scc.insert(0,0)

    def Lab_pressed(lst, Le, e, r_glo, c_glo):
        if (e.get().upper() == lst.upper()):
            (Le.configure(state="disable", fg="cyan", background="black", borderwidth=0))
            ee = 0
            sc = scc.get()
            scc.delete(0, 2)
            scc.insert(0, int(sc) + 1)
            playsound.playsound("mixkit-arcade-score-interface-217.wav",0)
            if (int(scc.get()) == n_wor):
                print("win")
                playsound.playsound("mixkit-males-yes-victory-2012.wav",0)
                root.destroy()
                rr2 = Tk()
                rr2.title("Congratulations.")
                rr2.configure(background="black")
                ph2 = PhotoImage(file="obama (2).png")
                can1 = Canvas(rr2, width=700, height=500)
                can1.pack(fill="y", expand=True)
                can1.create_image(400, 250, image=ph2)

                b11 = Button(rr2, text="Congratulations!!! :)", borderwidth=0, anchor="center", fg="cyan", bg="black",
                             font=("Roman", 18, "italic"))
                but11 = can1.create_window(400, 400, anchor="ne", window=b11)
                rr2.mainloop()
        else:
            playsound.playsound("mixkit-wrong-answer-bass-buzzer-948.wav",0)
            Le.configure(fg="red")
        e.delete(0, len(e.get()))
    r_glo = 0
    c_glo = 0
    def Lab(lst, cc, r_glo, c_glo):
        Le = Button(root, text=lst, background="black", fg="green" if cc % 2 == 0 else "yellow",
                    command=(lambda: Lab_pressed(lst, Le, e, r_glo, c_glo)))
        #leee1 = can1.create_window(cc, 0, anchor="ne", window=Le)
        Le.grid(row=cc, column=0)
    cc = 4
    def buttt_pressed(r_butt, c_butt, crswrd, e, r_glo, c_glo, mwid):
        r_glo = r_butt
        c_glo = c_butt
        playsound.playsound("mixkit-retro-game-notification-212.wav", 0)
        if (c_butt < (mwid - 2)):
            e.delete(0,len(e.get()))
            e.insert(len(e.get()), f"{crswrd[(r_butt - 4)][(c_butt - 2):(c_butt + 3)]}")
        ee = 0
        for rrr in range(c_glo, c_glo + 5):
            butt = Button(root, text=e.get()[ee], pady=5, padx=5, borderwidth=0, background="black", fg="grey",
                          command=lambda: buttt_pressed(r_butt, c_butt, crswrd, e, r_glo, c_glo, mwid))
            #leee7= can1.create_window(r_glo, rrr, anchor="ne", window=butt)
            butt.grid(row=r_glo, column=rrr)
            ee += 1
    def destroy(la,le,lf,close_bu):
        playsound.playsound("mixkit-game-flute-bonus-2313.wav", 0)
        la.destroy()
        le.destroy()
        lf.destroy()
        close_bu.destroy()
    def help_hover(mwid):
        playsound.playsound("mixkit-game-flute-bonus-2313.wav", 0)
        La=Label(root,text="> Select the first letter of the word/sequence in the crossword",font=("Helvetica", 12, "italic"),background="black",fg="white")
        #leee8 = can1.create_window(2, mwid+2, anchor="ne", window=La)

        La.grid(row=2,column=mwid+2)
        Le = Label(root, text="> The Selected word will be displayed on the Label at the left-most corner",font=("Helvetica", 12, "italic"), background="black", fg="white")
        #leee10 = can1.create_window(3, mwid + 2, anchor="ne", window=Le)
        Le.grid(row=3, column=mwid+2)
        Lf = Label(root, text="> Click on the desired Word to check with, from the left Word-list",font=("Helvetica", 12, "italic"), background="black", fg="white")
        #leee9 = can1.create_window(4, mwid + 2, anchor="ne", window=Lf)
        Lf.grid(row=4,  column=mwid+2)
        close_bu=Button(root,text="CLOSE",font=("Helvetica", 10, "bold"), background="black", fg="red",command=lambda :destroy(La,Le,Lf,close_bu))
        #leee11 = can1.create_window(1, mwid + 2, anchor="ne", window=close_bu)
        close_bu.grid(row=1,column=mwid+2)


    butt_help=Button(root,text="HELP",font=("Helvetica", 10, "italic"),background="black",fg="yellow",command=lambda :help_hover(mwid))
    #leee18 = can1.create_window(1, 25, anchor="ne", window=butt_help)
    butt_help.grid(row=1,column=25,columnspan=1)

    def buttt(ch, r_butt, c_butt, r_glo, c_glo):
        butt = Button(root, text=ch, pady=5, padx=5, borderwidth=0, background="black", fg="cyan",
                      command=lambda: buttt_pressed(r_butt, c_butt, crswrd, e, r_glo, c_glo, mwid))
        #leee80 = can1.create_window(r_butt, c_butt, anchor="ne", window=butt)
        butt.grid(row=r_butt, column=c_butt)
    buttsub = Button(root, text="Submit",
                     command=lambda: messagebox.showinfo(title="Result", message=f"Score is {scc.get()}"),
                     background="green", fg="orange", height=2)
    #leee8 = can1.create_window(25, 0, anchor="ne", window=buttsub)
    buttsub.grid(row=25, column=0, columnspan=1, padx=10, pady=10)
    buttexi=Button(root,text="X",font=("handwritten","12","bold"),command=lambda :root.destroy(),background="black",fg="red",borderwidth=1)
    #leee89 = can1.create_window(0, 25, anchor="ne", window=buttexi)
    buttexi.grid(row=0,column=25 ,columnspan=1,padx=10,pady=10)
    chh = 65
    s1 = []
    s = []
    for a in range(65, 91):
        s.append(chr(a))
    def choose_word(n_wor, r_glo, c_glo):
        cc = 4
        for a in range(n_wor):
            n = random.randint(0, 5757)
            stt = ""
            test_st = ""
            for c in flstr[n].upper().strip("\n"):
                stt = stt + c
                test_st += c
            s1.append(stt.lstrip(" "))

            Lab(test_st, cc, r_glo, c_glo)
            cc += 1
    choose_word(n_wor, r_glo, c_glo)
    lr = []
    lw = []
    row = []
    for c in range(max(n_wor + 3, 5)):
        row.append(c)
    for b in range(n_wor):
        lr.append(random.choice(row))
        row.remove(lr[-1])
        lw.append(random.randint(0, 10))
    crswrd = []
    l1 = lr.copy()
    l2 = lw.copy()
    for a in range(max(n_wor + 3, 5)):
        ste = ""
        b = 0
        while b < mwid:
            if (a in l1 and b == l2[l1.index(a)]):
                l1.remove(a)
                l2.remove(b)
                check_st = random.choice(s1)
                s1.remove(check_st)
                ste += check_st
                b += 5
            else:
                ste += random.choice(s)
                b += 1
        crswrd.append(ste)
    r, c = 4, 2
    for a in range(len(crswrd)):
        for wor in crswrd[a]:
            buttt((wor), r, c, r_glo, c_glo)
            c += 1
        r += 1
        c = 2
    print(lr)
    print(lw)
    root.mainloop()
nww=Entry(diag,width=5,background="orange",fg="brown",font=("Engravers MT",20))
#nww.grid(row=0,column=1,columnspan=1)
nwwww=c1.create_window(690,400,anchor="n",window=nww,height=30)
b1=Button(diag,text="SUBMIT",borderwidth=0,anchor="center",fg="brown",bg="orange",font=("Georgia",15,"bold"),command=lambda :ii(nww,ph2,nww.get() if nww.get()!="" else 5),compound=CENTER)
but1=c1.create_window(650,450,anchor="ne",window=b1)
#BUe=Button(diag,text="Submit",background="grey",fg="green",command=lambda :ii(n_wor,nww),compound=CENTER)
diag.mainloop()