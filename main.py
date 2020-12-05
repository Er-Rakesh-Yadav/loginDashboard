"""
@author: Rakesh Yadav
@Tasks: -> UI for logIn DashBoard
        ->
"""
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk


class LoginDashboard:
    def __init__(self, win_root):
        self.root = win_root
        self.root.title("Login Dashboard")
        self.root.geometry("1000x600+0+0")

        # ------------------ icon of LogIn Dashboard ----------------------#
        icon_photo = PhotoImage(file="img/login_img/login_icon.png")
        self.root.iconphoto(False, icon_photo)

        # ------------- Entry_Field Variables ----------------------------------#
        self.uname = StringVar()
        self.pass_ = StringVar()

        # .................. All-Images .........................#
        self.bg_icon = ImageTk.PhotoImage(file="img/login_img/bg_photo.jpg")
        self.user_icon = PhotoImage(file="img/login_img/User.png")
        self.pass_icon = PhotoImage(file="img/login_img/pass.png")
        self.logo_icon = PhotoImage(file="img/login_img/user-male.png")

        # ............... background-image labelling ..........................#
        bg_label = Label(self.root, image=self.bg_icon)
        bg_label.pack()

        # ............... top-title labelling ..........................#
        title = Label(self.root, text="Login System", font=("time new roman", 30, "bold"), bg="#EC0D5B", fg="white")
        title.place(x=0, y=0, relwidth=1)

        # --------- LogIn-Frame -------------------------------------------#
        Login_frame = Frame(self.root, bg="white")
        Login_frame.place(x=200, y=200)

        logo_label = Label(Login_frame, image=self.logo_icon)
        logo_label.grid(row=0, columnspan=25, padx=20, pady=10)

        # ........... Username -  image_icon + entry_field Labelling ....................#
        user_label = Label(Login_frame, text="Username", image=self.user_icon, compound=LEFT,
                           font=("time new roman", 17, "bold"), bg="white")
        user_label.grid(row=1, column=0, padx=20, pady=10)
        user_text = Entry(Login_frame, bd=5, textvariable=self.uname,
                          font=("Fira Code", 15), bg="#ccc", fg='black')
        user_text.grid(row=1, column=2, pady=10)

        # ........... Password -  image_icon + entry_field Labelling ....................#
        pass_label = Label(Login_frame, text="Password", image=self.pass_icon, compound=LEFT,
                           font=("time new roman", 17, "bold"), bg="white", fg="black")
        pass_label.grid(row=2, column=0, padx=20, pady=15)
        pass_text = Entry(Login_frame, bd=5, textvariable=self.pass_, font=("Fira Code", 15), show="*", bg="#ccc")
        pass_text.grid(row=2, column=2, pady=10)

        # ................. button-labelling ....................#
        login_btn = Button(Login_frame, text="Login", width=7, font=("arial", 14, "italic", "bold"), bg="#cc2",
                           command=self.login, bd=2, activebackground='goldenrod4', fg='black')
        login_btn.grid(row=3, column=3, padx=5, pady=5)

        # ------------ auto-invoke method by pressing Enter key -------------------#
        def auto_invoke_enter(event):
            login_btn.invoke()

        # --- method to binding self.root with 'ENTER KEY'
        self.root.bind('<Return>', auto_invoke_enter)

    # ............... login method ...........................................................#
    def login(self):
        if self.uname.get() == "" or self.pass_.get() == "":
            messagebox.showerror("Error", "All Inputs are Required !!")
        elif self.uname.get() == "Rakesh" and self.pass_.get() == "12345":
            messagebox.showinfo("Successful", f"WELCOME {self.uname.get()}")
        else:
            messagebox.showerror("Error", "Invalid Username or Password")


root = Tk()
obj = LoginDashboard(root)
root.mainloop()
