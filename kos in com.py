from tkinter import*

def show_login():
	frame2.pack_forget()
	frame1.pack()
	
def show_second_slide():
     frame1.pack_forget()
     frame2.pack()
     
window = Tk()
window.geometry("400x300")

frame1 = Frame(window)
frame1.pack()

label1 = Label(frame1, text="                 ", width=800, bg="grey")
label1.pack()

label = Label(window, text="Kos in.com", bg="red", fg="white", width=50, font=("Arial", 11))
label.place(x=0,y=0,height=60)

label = Label(window, text="Nomor Ponsel Atau Email", bg="black", fg="white")
label.place(x=0, y=100)

entry = Entry(window, bg="white", fg="black")
entry.place(x=5,y=153,width=470,height=50)

label = Label(window, text="Kata Sandi", bg="black", fg="white")
label.place(x=0,y=220)

entry = Entry(window, show="*",bg="white",fg="black")
entry.place(x=5,y=280,width=470,height=50)

login_button = Button(frame1, text="login",bg="red",fg="white",command=show_second_slide)
login_button.pack(pady=315)

frame2 = Frame(window)

label2 = Label(frame2, text="Selamat Anda Berhasil", font=("Arial", 19))
label2.pack(pady=350)


window.mainloop()