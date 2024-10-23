from tkinter import*

window = Tk()

label = Label(window, text="                 ",width=800, bg="grey")
label.pack()

label = Label(window, text="Facebook", bg="blue", fg="white", width=45)
label.place(x=0, y=0, height=60)

label = Label(window, text="Nomor Ponsel Atau Email", bg="grey",fg="white")
label.place(x=0, y=80)

entry = Entry(window, bg="white", fg="black")
entry.place(x=5, y=124, width=470, height=50)

label = Label(window, text="kata sandi",bg="grey",fg="white")
label.place(x=0,y=195)

entry = Entry(window, show="*",bg="white", fg="black")
entry.place(x=5,y=230,width=470,height=60)

button = Button(window, text="Login", bg="blue", fg="white", activebackground="royalblue",activeforeground="white")
button.place(x=5,y=310,width=470,height=60)

button = Button(window, text="Lupa Kata Sandi?", fg="blue", bg="white", activebackground="grey", activeforeground="blue")
button.place(x=5, y=390, width=470)

label = Label(window, text="- - - - atau - - - -",bg="grey", fg="white")
label.place(x=0,y=460,width=480)

button = Button(window, text="Buat Akun Baru", bg="green", fg="white",activebackground="grey",activeforeground="white")
button.place(x=120,y=520)

label = Label(window, text="Bahasa lainya..", bg="grey",fg="blue")
label.place(x=0,y=625)

label = Label(window, text="Bahasa Indonesia", bg="grey", fg="blue")
label.place(x=0,y=665)

label = Label(window, text="English", bg="grey", fg="blue")
label.place(x=0,y=705)

window.mainloop()