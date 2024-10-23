from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
from browse import browser
from feedbox import Feedback
from login import login_page
from library import library

cart = []

class videogame:
    def __init__(self, root):
        self.root = root
        self.root.title("Neel Games Store")
        self.root.geometry("1550x840+0+0")
        self.root.state("zoomed")
        self.root.resizable(0, 0)
        self.main()
            
    @staticmethod
    def connect_to_db():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Neel_123",
            database="mydata"
        )

    def add_to_cart(self, game_name, game_price):
        cart.append({'name': game_name, 'price': game_price})
        messagebox.showinfo("Cart", f"Added {game_name} to the cart!")

    def place_order(self):
        db = self.connect_to_db()
        cursor = db.cursor()

        try:
            for item in cart:
                cursor.execute(
                    "INSERT INTO cart_item (game_name, price) VALUES (%s, %s)",
                    (item['name'], item['price'])
                )
            db.commit()
            messagebox.showinfo("Order", "Order placed successfully!")
            cart.clear()  # Clear the cart after placing the order
        except Exception as e:
            db.rollback()
            messagebox.showerror("Error", f"Failed to place order: {str(e)}")
        finally:
            cursor.close()
            db.close()

    def remove_from_cart(self, game_name):
        global cart
        # Find the item in the cart and remove it
        cart = [item for item in cart if item['name'] != game_name]
        
        # Refresh the cart view to update the UI
        self.view_cart()

    def view_cart(self):
        cartFrame = Frame(self.root, width=1230, height=840, bg="#333333")
        cartFrame.place(x=300, y=0)

        Label(cartFrame, text="Your Cart", font=("cursive", 30, "bold"), bg="#333333", fg="white").place(x=500, y=40)

        y_position = 120
        total = 0

        for item in cart:
            Label(cartFrame, text=item['name'], font=("cursive", 20, "bold"), bg="#333333", fg="white").place(x=50, y=y_position)
            Label(cartFrame, text=f"₹{item['price']}", font=("cursive", 20, "bold"), bg="#333333", fg="white").place(x=400, y=y_position)
            
            # Adjust the y position for the Remove button
            remove_btn = Button(cartFrame, text="Remove", command=lambda g=item['name']: self.remove_from_cart(g), font=("cursive", 10, "bold"), width=10, bg="red", bd=0, fg="white", cursor="hand2", activebackground="red", activeforeground="white")
            remove_btn.place(x=600, y=y_position)

            y_position += 50
            total += item["price"]

        Label(cartFrame, text=f"Total:₹{total}", font=("cursive", 25, "bold"), bg="#333333", fg="white").place(x=50, y=y_position) 

        backButton = Button(cartFrame, text="<", command=self.main, font=("cursive", 20, "bold"), width=1, bg="#333333", bd=0, fg="white", activebackground="#333333", activeforeground="white", cursor="hand2")
        backButton.place(x=1, y=1)

        placeOrderButton = Button(cartFrame, command=self.place_order, text="Place Order", font=("cursive", 20, "bold"), width=15, bg="black", bd=0, fg="gold", cursor="hand2")
        placeOrderButton.place(x=50, y=y_position + 40)

    def main(self):
        main_frame = Frame(self.root, width=300, height=840, bg="#1C1C1C")
        main_frame.place(x=0, y=0)

        browse = Button(main_frame, command=self.open_browser, text="Browse", font=("cursive", 20, "bold"), width=10, bg="#1C1C1C", bd=0, fg="light gray", cursor="hand2")
        browse.place(x=50, y=50)

        lbry_btn = Button(main_frame,command=self.open_library, text="Library", font=("cursive", 20, "bold"), width=10, bg="#1C1C1C", bd=0, fg="light gray", cursor="hand2")
        lbry_btn.place(x=50, y=150)

        feedback_btn = Button(main_frame, command=self.open_feedback, text="FeedBack", font=("cursive", 20, "bold"), width=10, bg="#1C1C1C", bd=0, fg="light gray", cursor="hand2")
        feedback_btn.place(x=50, y=250)

        report_btn = Button(main_frame, text="Report", font=("cursive", 20, "bold"), width=10, bg="#1C1C1C", bd=0, fg="light gray", cursor="hand2")
        report_btn.place(x=50, y=350)

        cart_btn = Button(main_frame, text="Cart", command=self.view_cart, font=("cursive", 20, "bold"), width=10, bg="#1C1C1C", bd=0, fg="light gray", cursor="hand2")
        cart_btn.place(x=50, y=450)

        # Update the login/logout button text based on login status
        login_btn_text = "Log In"
        self.login_btn = Button(main_frame, text=login_btn_text, font=("cursive", 20, "bold"), width=10, bg="#1C1C1C", bd=0, fg="light gray", cursor="hand2")
        self.login_btn.place(x=50, y=770)

        right_Frame = Frame(self.root, width=1230, height=840, bg="#333333")
        right_Frame.place(x=300, y=0)

        title_lbl = Label(right_Frame, text="Welcome to The Video Game Store", font=("helvatica", 20, "bold"), bg="#333333", fg="white")
        title_lbl.place(x=50, y=50)

        self.contect_frame = Frame(right_Frame, width=1130, height=540, bg="black")
        self.contect_frame.place(x=50, y=120)

        lblGameName = Label(self.contect_frame, text="Best Seller Games", font=("helvatica", 20, "bold"), bg="black", fg="white")
        lblGameName.place(x=50, y=50)

        games = [
            {"name": "Resident Evil 8", "price": 2399, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/story_game_img6.jpg", "x": 50, "y": 130},
            {"name": "A Plague Tale: Requiem", "price": 2299, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/story_game_img2.jpg", "x": 410, "y": 130},
            {"name": "Red Dead Redemption 2", "price": 3199, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/rpg_game_img4.jpg", "x": 780, "y":130}
        ]

        for game in games:
            image = Image.open(game["image"])
            image = image.resize((250, 300), Image.Resampling.LANCZOS)
            photoimage = ImageTk.PhotoImage(image)

            lblGame = Label(self.contect_frame, image=photoimage, bd=4)
            lblGame.image = photoimage
            lblGame.place(x=game["x"], y=game["y"])

            game1Text = Label(self.contect_frame, text=game["name"], font=("cursive", 20, "bold"), bg="black", fg="white")
            game1Text.place(x=game["x"], y=game["y"] + 310)

            btnAddToCart = Button(self.contect_frame, command=lambda g=game: self.add_to_cart(g["name"], g["price"]), text="Add To Cart", font=("cursive", 10, "bold"), width=10, bg="black", bd=0, fg="white", cursor="hand2", activebackground="black", activeforeground="white")
            btnAddToCart.place(x=game["x"], y=game["y"] + 350)

            btnPriceGame = Label(self.contect_frame, text=f"₹{game['price']}", font=("cursive", 15, "bold"), bg="black", fg="white")
            btnPriceGame.place(x=game["x"] + 90, y=game["y"] + 350)

    def open_browser(self):
        browser(self.root)

    def open_feedback(self):
        Feedback(self.root)

    def open_login(self):
            login_page(self.root)
            
    def open_library(self):
        library(self.root)

if __name__ == "__main__":
    root = Tk()
    obj = videogame(root)
    root.mainloop()