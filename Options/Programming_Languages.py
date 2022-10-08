from tkinter import *
from random import *
from tkinter import messagebox


Programming_Languages_WORD = ['SCAVRIJAPT', 'HOPTYN', 'ISFWT', 'TPIRCSTYPE', 'AAVJ', 'ASLCA', 'IKONTL', 'INTYU',  ]

Programming_Languages_ANSWER = ['JAVASCRIPT', 'PYTHON', 'SWIFT', 'TYPESCRIPT', 'JAVA', 'SCALA', 'KOTLIN', 'UNITY', ]
 
ran_num = randrange(0, (len(Programming_Languages_WORD)))
jumbled_rand_word = Programming_Languages_WORD[ran_num]

points = 0
 

def main():
    def back():
        my_window.destroy()
        import index
        index.start_main_page()

    def change():
        global ran_num
        ran_num = randrange(0, (len(Programming_Languages_WORD)))
        word.configure(text=Programming_Languages_WORD[ran_num])
        get_input.delete(0, END)
        ans_lab.configure(text="")

    def cheak():
        global points, ran_num
        user_word = get_input.get().upper()
        if user_word == Programming_Languages_ANSWER[ran_num]:
            points += 1
            score.configure(text="Score: " + str(points))
            messagebox.showinfo('correct', "Correct Answer")
            ran_num = randrange(0, (len(Programming_Languages_WORD)))
            word.configure(text=Programming_Languages_WORD[ran_num])
            get_input.delete(0, END)
            ans_lab.configure(text="")
        else:
            messagebox.showerror("Error", "Inorrect Answer")
            get_input.delete(0, END)

    def show_answer():
        global points
        if points >= 1:
            points -= 1
            score.configure(text="Score: " + str(points))
           
            ans_lab.configure(text=Programming_Languages_ANSWER[ran_num])
        else:
            ans_lab.configure(text='Not enough points')
            ans_lab.configure(bg="#334455")
            ans_lab.configure(fg="#dedede")

    my_window = Tk()
    my_window.geometry("700x700+450+50")
    my_window.resizable(0, 0)
    my_window.title("Guest the Word ")
    my_window.configure(background="#334455")
    img1 = PhotoImage(file="back.png")

    lab_img1 = Button(
        my_window,
        image=img1,
        bg='#334455',
        border=0,
        justify='center',
        command=back,
        activebackground="#345",
    )
    lab_img1.pack(anchor='nw', pady=10, padx=10)

    score = Label(
        text="Score:- 0",
        pady=10,
        bg="#334455",
        fg="#dedede",
        font="Titillium  14 bold"
    )
    score.pack(anchor="n")

    word = Label(
        text=jumbled_rand_word,
        pady=10,
        bg="#334455",
        fg="#dedede",
        font="Titillium  50 bold"
    )
    word.pack()

    get_input = Entry(
        font="none 26 bold",
        borderwidth=10,
        justify='center',
    )
    get_input.pack()

    submit = Button(
        text="Submit",
        width=18,
        borderwidth=8,
        font=("", 13),
        fg="#000000",
        bg="#dedede",
        command=cheak,
        relief="groove",
        activebackground="#345",
        cursor="hand2",
    )
    submit.pack(pady=(10, 20))

    change = Button(
        text="Change Word",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#dedede",
        font=("", 13),
        command=change,
        relief="groove",
        activebackground="#345",
        cursor="hand2",
    )
    change.pack()

    ans = Button(
        text="Answer",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#dedede",
        font=("", 13),
        command=show_answer,
        relief="groove",
        activebackground="#345",
        cursor="hand2",
    )
    ans.pack(pady=(20, 10))

    ans_lab = Label(
        text="",
        bg="#dedede",
        fg="#000000",
        font="Courier 15 bold",
    )
    ans_lab.pack()

    my_window.mainloop()
