from tkinter import *
import mysql.connector
from tkinter import messagebox, ttk
from browse import browser

class Feedback:
    def __init__(self, root):
        self.root = root
        self.root.title("Neel Games Store")
        self.root.geometry("1550x840+0+0")
        self.root.state("zoomed")
        self.root.resizable(0, 0)

        #===========================main frame=========================================================
        main_frame = Frame(self.root, width=300, height=840, bg="#1C1C1C")
        main_frame.place(x=0,y=0)

        self.right_Frame = Frame(root,width=1230,height=840,bg="#333333")
        self.right_Frame.place(x=300,y=0)

        #===========================btn frame=========================================================

        browse = Button(main_frame,command=self.open_browser, text="Browse", font=("cursive",20,"bold"),width=10,bg="#1C1C1C",bd=0,fg="light gray",cursor="hand2")
        browse.place(x=50,y=50)

        lbry_btn=Button(main_frame,text="Library", font=("cursive",20,"bold"),width=10,bg="#1C1C1C",bd=0,fg="light gray",cursor="hand2")
        lbry_btn.place(x=50,y=150)

        feedback_btn=Button(main_frame, text="FeedBack", font=("cursive",20,"bold"),width=10,bg="#1C1C1C",bd=0,fg="light gray",cursor="hand2")
        feedback_btn.place(x=50,y=250)

        report_btn=Button(main_frame,text="Report", font=("cursive",20,"bold"),width=10,bg="#1C1C1C",bd=0,fg="light gray",cursor="hand2")
        report_btn.place(x=50,y=350)
        
        login_btn=Button(main_frame,command=self.backHome, text="Back Home", font=("cursive",20,"bold"),width=10,bg="#1C1C1C",bd=0,fg="light gray",cursor="hand2")
        login_btn.place(x=50,y=770)
        
        title_lbl = Label(self.right_Frame, text="We value your Feedback", font=("helvetica", 20, "bold"), bg="#333333", fg="light gray")
        title_lbl.place(x=300, y=50)

        name_lbl = Label(self.right_Frame, text="Name:", font=("helvetica", 20, "bold"), bg="#333333", fg="light gray")
        name_lbl.place(x=100, y=150)

        self.name_entry = ttk.Entry(self.right_Frame, font=("arial", 20, "bold"))
        self.name_entry.place(x=200, y=150, width=670)

        email_lbl = Label(self.right_Frame, text="E-Mail:", font=("helvetica", 20, "bold"), bg="#333333", fg="light gray")
        email_lbl.place(x=100, y=250)

        self.email_entry = ttk.Entry(self.right_Frame, font=("arial", 20, "bold"))
        self.email_entry.place(x=200, y=250, width=670)

        feedback_lbl = Label(self.right_Frame, text="Feed-Back:", font=("helvetica", 20, "bold"), bg="#333333", fg="light gray")
        feedback_lbl.place(x=100, y=350)

        self.feedback_text = Text(self.right_Frame, font=("arial", 20, "bold"), width=45, height=10)
        self.feedback_text.place(x=260, y=350)

        btn_submit = Button(self.right_Frame, text="Submit", font=("helvetica", 20, "bold"), bg="#333333", fg="light gray", command=self.submit_feedback)
        btn_submit.place(x=500, y=750)

    def submit_feedback(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        feedback = self.feedback_text.get("1.0", "end-1c")

        if not name or not email or not feedback:
            messagebox.showerror("Error", "All fields are required.")
            return
        
        try:
            # Connect to the database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Neel_123",
                database="mydata"
            )
            cursor = conn.cursor()
            query = "INSERT INTO feedback (name, email, feedback) VALUES (%s, %s, %s)"
            values = (name, email, feedback)
            cursor.execute(query, values)
            conn.commit()

            messagebox.showinfo("Success", "Feedback submitted successfully!")
            self.clear_fields()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}")
        
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def clear_fields(self):
        self.name_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.feedback_text.delete("1.0", END)

    def open_browser(self):
        browser(self.root)

    def backHome(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        from home import videogame
        videogame(self.root)

if __name__ == "__main__":
    root = Tk()
    app = Feedback(root)
    root.mainloop()
