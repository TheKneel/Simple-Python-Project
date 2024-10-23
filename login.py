from tkinter import *
from tkinter import ttk, PhotoImage
from PIL import Image, ImageTk
from tkinter import messagebox
from register import register
import mysql.connector

class login_page:
    def __init__(self, root):
        self.root = root
        self.root.title("Neel Games Store")
        self.root.geometry("1550x840+0+0")
        self.root.state("zoomed")
        self.root.resizable(0, 0)

        # ========variables=========
        self.var_username = StringVar()
        self.var_password = StringVar()
        self.show_password = False

        # ===========================main frame===========================
        main_frame = Frame(self.root, width=300, height=840, bg="#1C1C1C")
        main_frame.place(x=0, y=0)

        self.right_Frame = Frame(root, width=1230, height=840, bg="#333333")
        self.right_Frame.place(x=300, y=0)

        # ===========================btn frame============================

        browse = Button(main_frame, text="Browse", font=("cursive", 20, "bold"), width=10, bg="#1C1C1C", bd=0, fg="light gray", cursor="hand2")
        browse.place(x=50, y=50)

        lbry_btn = Button(main_frame, text="Library", font=("cursive", 20, "bold"), width=10, bg="#1C1C1C", bd=0, fg="light gray", cursor="hand2")
        lbry_btn.place(x=50, y=150)

        feedback_btn = Button(main_frame, text="FeedBack", font=("cursive", 20, "bold"), width=10, bg="#1C1C1C", bd=0, fg="light gray", cursor="hand2")
        feedback_btn.place(x=50, y=250)

        report_btn = Button(main_frame, text="Report", font=("cursive", 20, "bold"), width=10, bg="#1C1C1C", bd=0, fg="light gray", cursor="hand2")
        report_btn.place(x=50, y=350)

        login_btn = Button(main_frame,command=self.backHome, text="Back Home", font=("cursive", 20, "bold"), width=10, bg="#1C1C1C", bd=0, fg="light gray", cursor="hand2")
        login_btn.place(x=50, y=770)

        frame = Frame(self.right_Frame, bg="light gray")
        frame.place(x=300, y=100, width=500, height=600)

        # Title Label
        self.heading = Label(frame, text="Login", font=("Helvetica", 20, "bold"), bg="light gray", fg="#1C1C1C")
        self.heading.place(x=200, y=30)

        # Login Image
        image = Image.open("C:/Users/NEEL PATEL/OneDrive/Desktop/project images/login.png")
        image = image.resize((50, 50), Image.Resampling.LANCZOS)
        photoimage = ImageTk.PhotoImage(image)

        lblGame = Label(frame, image=photoimage, bd=4)
        lblGame.image = photoimage
        lblGame.place(x=215, y=70)

        # Username Label and Entry
        username_lbl = Label(frame, text="USERNAME:", font=("Helvetica", 10, "bold"), fg="#1C1C1C", bg="light gray")
        username_lbl.place(x=30, y=150)

        self.txtuser = Entry(frame, highlightthickness=0, textvariable=self.var_username, font=("Cursive", 13, "bold"), bd=4, relief=FLAT, bg="light gray", fg="#1C1C1C", cursor="xterm")
        self.txtuser.place(x=60, y=190, width=290)

        self.usernameLine = Canvas(frame, width=300, height=2, bg="white", highlightthickness=0)
        self.usernameLine.place(x=30, y=213)

        userIcon_image = Image.open("C:/Users/NEEL PATEL/OneDrive/Desktop/project images/username_icon.png")
        userIcon_image = userIcon_image.resize((20, 20), Image.Resampling.LANCZOS)
        photoimage2 = ImageTk.PhotoImage(userIcon_image)

        userIcon_image = Label(frame, image=photoimage2, bd=4)
        userIcon_image.image = photoimage2
        userIcon_image.place(x=30, y=180)

        # Password Label and Entry
        password_lbl = Label(frame, text="PASSWORD:", font=("Helvetica", 10, "bold"), fg="#1C1C1C", bg="light gray")
        password_lbl.place(x=30, y=250)

        self.password = Entry(frame, highlightthickness=0, textvariable=self.var_password, font=("Cursive", 10, "bold"), bd=4, show="*", relief=FLAT, bg="light gray", fg="#1C1C1C")
        self.password.place(x=60, y=280, width=290)

        self.passwordLine = Canvas(frame, width=300, height=2, bg="white", highlightthickness=0)
        self.passwordLine.place(x=30, y=310)

        userIcon_image = Image.open("C:/Users/NEEL PATEL/OneDrive/Desktop/project images/password_icon.jpg")
        userIcon_image = userIcon_image.resize((20, 20), Image.Resampling.LANCZOS)
        photoimage2 = ImageTk.PhotoImage(userIcon_image)

        userIcon_image = Label(frame, image=photoimage2, bd=4)
        userIcon_image.image = photoimage2
        userIcon_image.place(x=30, y=280)

        # Show/Hide Password Button
        self.show_image = Image.open("C:/Users/NEEL PATEL/OneDrive/Desktop/project images/show.png")
        self.show_image = self.show_image.resize((20, 20), Image.Resampling.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(self.show_image)

        self.hide_image = Image.open("C:/Users/NEEL PATEL/OneDrive/Desktop/project images/hide.png")
        self.hide_image = self.hide_image.resize((20, 20), Image.Resampling.LANCZOS)
        self.photoimage4 = ImageTk.PhotoImage(self.hide_image)

        self.show_btn = Button(frame, command=self.toggle_password_visibility, image=self.photoimage3, fg="#1C1C1C", bg="white", activeforeground="#1C1C1C", activebackground="white", bd=0)
        self.show_btn.place(x=300, y=280)

        # Login Button
        login_btn = Button(frame, command=self.login, text="Login", font=("yu gothic ui", 20, "bold"), bd=3, relief="flat", fg="#1C1C1C", bg="light gray", activeforeground="white", activebackground="#1C1C1C", cursor="hand2")
        login_btn.place(x=190, y=350, width=120, height=50)

        # Registration Button
        reg_lbl = Label(frame, text="No Account Yet?", font=("yu gothic ui", 15, "bold"), fg="#1C1C1C", bg="light gray")
        reg_lbl.place(x=30, y=540)

        reg_btn = Button(frame,command=self.toRegister, text="Click here to Register", font=("Helvetica", 10, "bold"), borderwidth=0, fg="#1C1C1C", bg="light gray", activeforeground="#1C1C1C", activebackground="light gray", cursor="hand2")
        reg_btn.place(x=190, y=550, width=150)

    def toggle_password_visibility(self):
        if self.show_password:
            self.password.config(show='*')
            self.show_btn.config(image=self.photoimage3)
        else:
            self.password.config(show='')
            self.show_btn.config(image=self.photoimage4)
        self.show_password = not self.show_password

    def login(self):
        if self.txtuser.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Neel_123", database="mydata")
            curr = conn.cursor()
            curr.execute("select * from register where email = %s and password = %s", (
                self.var_username.get(),
                self.var_password.get()
            ))
            row = curr.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid username or password")
            else:
                messagebox.showinfo("Success", "Welcome to Video Game Store")
                self.is_logged_inlogged_in = True  # Track if the user is logged in
                for widget in self.root.winfo_children():
                    widget.destroy()

                from home import videogame
                self.is_logged_in = True  # Track if the user is logged in
                videogame(self.root)
            conn.commit()
            conn.close()
            
            if row is not None:
                self.login_callback(True)
            else:
                self.login_callback(False)

    def toRegister(self):
        register(self.root)

    def backHome(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        from home import videogame
        videogame(self.root)  

if __name__ == "__main__":
    root = Tk()
    app = login_page(root)
    root.mainloop()