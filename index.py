from tkinter import *
from PIL import ImageTk

  

def start_main_page():
    def back():
        main_window.destroy()
        import index
        index.start_main_page()
    def start_game(args):
        main_window.destroy()
        if args == 1:
            from Options import Programming_Languages
            Programming_Languages.main()
        elif args == 2:
            from Options import Social_media
            Social_media.main()
        elif args == 3:
            from Options import operating_system
            operating_system.main()
        elif args == 4:
            from Options import Android_versions
            Android_versions.main()
        elif args == 5:
            from Options import Python
            Python.main()
        elif args == 6:
            from Options import Games
            Games.main()
        

    def option():

        lab_img1 = Button(
            main_window,
            image=img1,
            bg='#334455',
            border=0,
            justify='center',
            command=back,
            activebackground="#345",
        )
        lab_img1.pack(anchor='nw', pady=10,padx=10)
        
       
        sel_btn1 = Button(
            text="Programming Languages",
            width=20,
            borderwidth=8,
            font=("", 18),
            fg="black",
            bg="#dedede",
            cursor="hand2",
            command=lambda: start_game(1),
            activebackground="#345",
            relief="groove",

        )

        sel_btn2 = Button(
            text="Social Media",
            width=20,
            borderwidth=8,
            font=("", 18),
            fg="black",
            bg="#dedede",
            cursor="hand2",
            command=lambda: start_game(2),
            activebackground="#345",
            relief="groove",
        )

        sel_btn3 = Button(
            text="Operating system",
            width=20,
            borderwidth=8,
            font=("", 18),
            fg="black",
            bg="#dedede",
            cursor="hand2",
            command=lambda: start_game(3),
            activebackground="#345",
            relief="groove",
        )

        sel_btn4 = Button(
            text="Android versions",
            width=20,
            borderwidth=8,
            font=("", 18),
            fg="black",
            bg="#dedede",
            cursor="hand2",
            command=lambda: start_game(4),
            activebackground="#345",
            relief="groove",
        )

        sel_btn5 = Button(
            text="Python",
            width=20,
            borderwidth=8,
            font=("", 18),
            fg="black",
            bg="#dedede",
            cursor="hand2",
            command=lambda: start_game(5),
            activebackground="#345",
            relief="groove",
        )

        sel_btn6 = Button(
            text="Games",
            width=20,
            borderwidth=8,
            font=("", 18),
            fg="black",
            bg="#dedede",
            cursor="hand2",
            command=lambda: start_game(6),
            activebackground="#345",
            relief="groove",
        )

        
       
        lab_img1.grid(row=0, column=0, padx=20)
        sel_btn1.grid(row=0, column=4, pady=(40, 0), padx=100, )
        sel_btn2.grid(row=1, column=4, pady=(40, 0), padx=100, )
        sel_btn3.grid(row=2, column=4, pady=(40, 0), padx=100, )
        sel_btn4.grid(row=3, column=4, pady=(40, 0), padx=100, )
        sel_btn5.grid(row=4, column=4, pady=(40, 0), padx=100, )
        sel_btn6.grid(row=5, column=4, pady=(40, 0), padx=100, )
        

    def show_option():
        start_btn.destroy()

        lab_img.destroy()
        option()
    main_window = Tk()

    main_window.geometry("700x700+450+50")
    main_window.resizable(0, 0)
    main_window.title("Guess the Word")
    main_window.configure(background="#334455")
    
    img1 = PhotoImage(file="back.png")
     
    
    

    
    lab_img = Label(
        main_window,
        text="Guess the Word ",
        bg='#334455',
        fg="#dedede",
        font=("Courier", 28),
        padx="0",
        pady="6",

    )
    lab_img.pack(pady=(50, 0))

    start_btn = Button(
        main_window,
        text="Start",
        width=10,
        borderwidth=5,      
        bg="#dedede",
        font=(0, 13),
        fg="black",
        cursor="hand2",
        command=show_option,
        relief="groove",
        activebackground="#345",
        padx="12",
        pady="0",
        
        
    )




    start_btn.pack(pady=(50, 20))

    main_window.mainloop()


start_main_page()
