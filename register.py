from tkinter import*
from tkinter import ttk, PhotoImage
from PIL import Image,ImageTk
from tkinter import messagebox 
import mysql.connector

class register:
        def __init__(self,root):
                self.root = root
                self.root.title("Registration")
                self.root.geometry("1600x900+0+0")
                self.root.state("zoomed")
                self.root.resizable(0, 0)

#============Variables=============
                self.var_fname = StringVar()
                self.var_lname = StringVar()
                self.var_contact = StringVar()
                self.var_email = StringVar()
                self.var_SecurityQ = StringVar()
                self.var_SecurityA = StringVar()
                self.var_create_pass = StringVar()
                self.var_confirm_pass = StringVar()


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

                report_btn = Button(main_frame, text="Report", font=("cursive", 20, "bold"), width=10, bg="#1C1C1C", bd=0, fg="light gray", cursor="hand2")
                report_btn.place(x=50, y=250)

                backHome_btn = Button(main_frame,command=self.backHome, text="Back Home", font=("cursive", 20, "bold"), width=10, bg="#1C1C1C", bd=0, fg="light gray", cursor="hand2")
                backHome_btn.place(x=50, y=770)

#==============Label and entry==============


#============row1
                fname = Label(self.right_Frame,text="First Name: ",font=("cursive",20),bg="#333333", fg="white")
                fname.place(x=30,y=150)

                fname_enty = ttk.Entry(self.right_Frame,textvariable=self.var_fname,font=("arial",20,"bold"))
                fname_enty.place(x=250,y=150)

                lname = Label(self.right_Frame,text="Last Name: ",font=("cursive",20),bg="#333333", fg="white")
                lname.place(x=600,y=150)

                lname_enty = ttk.Entry(self.right_Frame,textvariable=self.var_lname,font=("arial",20,"bold"))
                lname_enty.place(x=750,y=150)

#============row2
                contact_num = Label(self.right_Frame,text="Contact Number: ",font=("cursive",20),bg="#333333", fg="white")
                contact_num.place(x=30,y=250)

                contact_num_enty = ttk.Entry(self.right_Frame,textvariable=self.var_contact,font=("arial",20,"bold"))
                contact_num_enty.place(x=250,y=250)

                email = Label(self.right_Frame,text="E-Mail: ",font=("cursive",20),bg="#333333", fg="white")
                email.place(x=600,y=250)

                email_enty = ttk.Entry(self.right_Frame,textvariable=self.var_email,font=("arial",20,"bold"))
                email_enty.place(x=750,y=250)

#============row3
                create_pass = Label(self.right_Frame,text="Create Password: ",font=("cursive",20),bg="#333333", fg="white")
                create_pass.place(x=30,y=350)

                create_pass_enty = ttk.Entry(self.right_Frame,textvariable=self.var_create_pass,font=("arial",20,"bold"))
                create_pass_enty.place(x=250,y=350)

                confirm_pass = Label(self.right_Frame,text="Confirm Password: ",font=("cursive",20),bg="#333333", fg="white")
                confirm_pass.place(x=600,y=350)

                confirm_pass_enty = ttk.Entry(self.right_Frame,textvariable=self.var_confirm_pass,font=("arial",20,"bold"))
                confirm_pass_enty.place(x=850,y=350)

#============row4
                security_quetion = Label(self.right_Frame,text="Security Quetion: ",font=("cursive",20),bg="#333333", fg="white")
                security_quetion.place(x=30,y=450)

                self.combo_security_Q = ttk.Combobox(self.right_Frame,textvariable=self.var_SecurityQ,font=("cursive",20),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Pet Name")
                self.combo_security_Q.place(x=250,y=450)
                self.combo_security_Q.current(0)

                security_ans = Label(self.right_Frame,text="Security Answer: ",font=("cursive",20),bg="#333333", fg="white")
                security_ans.place(x=600,y=450)

                security_ans_enty = ttk.Entry(self.right_Frame,textvariable=self.var_SecurityA,font=("arial",20,"bold"))
                security_ans_enty.place(x=850,y=450)

#===========checkbox button===========
                self.var_check = IntVar()
                check_btn = Checkbutton(self.right_Frame,variable=self.var_check,text="I agree the terms and condiditons",font=("Arial Black",15,"bold"),bg="#333333", fg="white", activeforeground="white", activebackground="#333333",onvalue=1,offvalue=0)
                check_btn.place(x=50,y=540)

#===========buttons==================
                img = Image.open(r"C:\Users\NEEL PATEL\OneDrive\Desktop\project images\register_btn.png")
                img=img.resize((250,150),Image.Resampling.LANCZOS)
                self.photoimage = ImageTk.PhotoImage(img) 
                b1 = Button(self.right_Frame,command=self.register_data,image=self.photoimage,borderwidth=0,cursor="hand2",font=("cursive",20,"bold"),bg="#333333", fg="white", activeforeground="white", activebackground="#333333")
                b1.place(x=100,y=650,width=240)

                img2 = Image.open(r"C:\Users\NEEL PATEL\OneDrive\Desktop\project images\login_btn.png")
                img2=img2.resize((250,150),Image.Resampling.LANCZOS)
                self.photoimage2 = ImageTk.PhotoImage(img2)
                b1 = Button(self.right_Frame,command=self.backLogin,image=self.photoimage2,borderwidth=0,cursor="hand2",font=("cursive",20,"bold"),bg="#333333" , fg="white", activeforeground="white", activebackground="#333333")
                b1.place(x=600,y=650,width=240)

        def register_data(self):
                if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_SecurityQ.get() == "Select":
                        messagebox.showerror("Error","All fields are requried")
                elif self.var_create_pass.get() != self.var_confirm_pass.get():
                        messagebox.showerror("Error","Password does not match")
                elif self.var_check.get() == 0:
                        messagebox.showerror("Error","Please agree the terms and conditions")
                else:
                        conn = mysql.connector.connect(host="localhost",user="root",password="Neel_123",database="mydata")
                        curr = conn.cursor()
                        query = ("select * from register where email = %s")
                        value = (self.var_email.get(),)
                        curr.execute(query,value)
                        row = curr.fetchone()
                        if row!=None:
                                messagebox.showerror("Error","Email already in use")
                        else:
                                curr.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_fname.get(),
                                                                                                        self.var_lname.get(),
                                                                                                        self.var_contact.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_SecurityQ.get(),
                                                                                                        self.var_SecurityA.get(),
                                                                                                        self.var_create_pass.get()
                                                                                                ))
                                conn.commit()
                                conn.close()
                                messagebox.showinfo("Success","Register Successfully")

        def backHome(self):
                for widget in self.root.winfo_children():
                        widget.destroy()

                from home import videogame
                videogame(self.root)

        def backLogin(self):
                for widget in self.root.winfo_children():
                        widget.destroy()

                from login import login_page
                login_page(self.root)
        

if __name__ == "__main__":
    root = Tk()
    app = register(root)
    root.mainloop()