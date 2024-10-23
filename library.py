from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
from browse import browser

class library:
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

    def fetch_library_items(self):
        db = self.connect_to_db()
        cursor = db.cursor()
        try:
            cursor.execute("SELECT id, game_name, price FROM cart_item")  # Fetch 'id' to identify each game uniquely
            items = cursor.fetchall()
            return items
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch library items: {str(e)}")
            return []
        finally:
            cursor.close()
            db.close()

    def remove_game(self, game_id):
        db = self.connect_to_db()
        cursor = db.cursor()
        try:
            cursor.execute("DELETE FROM cart_item WHERE id = %s", (game_id,))  # Delete the game by its unique 'id'
            db.commit()
            messagebox.showinfo("Success", "Game removed from your library.")
            self.refresh_library()  # Refresh the library UI
        except Exception as e:
            messagebox.showerror("Error", f"Failed to remove game: {str(e)}")
        finally:
            cursor.close()
            db.close()

    def refresh_library(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.main()

    def main(self):
        main_frame = Frame(self.root, width=300, height=840, bg="#1C1C1C")
        main_frame.place(x=0, y=0)

        browse = Button(main_frame,command=self.open_browser, text="Browse", font=("cursive", 20, "bold"), width=10, bg="#1C1C1C", bd=0, fg="light gray", cursor="hand2")
        browse.place(x=50, y=50)

        lbry_btn = Button(main_frame, text="Library", font=("cursive", 20, "bold"), width=10, bg="#1C1C1C", bd=0, fg="light gray", cursor="hand2")
        lbry_btn.place(x=50, y=150)

        right_Frame = Frame(self.root, width=1230, height=840, bg="#333333")
        right_Frame.place(x=300, y=0)

        items = self.fetch_library_items()
        y_position = 120

        if items:
            for item in items:
                game_id = item[0]
                game_name = item[1]
                game_price = item[2]

                Label(right_Frame, text=game_name, font=("cursive", 20, "bold"), bg="#333333", fg="white").place(x=50, y=y_position)
                Label(right_Frame, text=f"₹{game_price}", font=("cursive", 20, "bold"), bg="#333333", fg="white").place(x=400, y=y_position)

                # Add a "Remove" button to remove the game from the library
                remove_btn = Button(right_Frame, text="Remove", font=("cursive", 15, "bold"), bg="red", fg="white",
                                    command=lambda game_id=game_id: self.remove_game(game_id))
                remove_btn.place(x=600, y=y_position)

                y_position += 50
        else:
            Label(right_Frame, text="No games in your library yet.", font=("cursive", 20, "bold"), bg="#333333", fg="white").place(x=50, y=y_position)

        # Back button to return to the game list
        btnBack = Button(right_Frame,command=self.backHome, text="<", font=("cursive", 20, "bold"), width=1, bd=0, bg="#333333", fg="white",activebackground="#333333", activeforeground="white", cursor="hand2")
        btnBack.place(x=10, y=10)

    def backHome(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        from home import videogame
        videogame(self.root)

    def open_browser(self):
        browser(self.root)

if __name__ == "__main__":
    root = Tk()
    obj = library(root)
    root.mainloop()