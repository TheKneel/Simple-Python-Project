from tkinter import*
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

cart = []

class browser():
    def __init__(self, root):
        self.root = root
        self.root.title("Neel Games")
        self.root.geometry("1550x840+0+0")
        self.root.state("zoomed")
        self.root.resizable(0, 0)
        self.main()

    @staticmethod
    def connect_to_db():
        return mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Neel_123",
            database = "mydata"
        )

    @staticmethod
    def add_to_cart(game_name, game_price):
        cart.append({'name': game_name, 'price': game_price})
        messagebox.showinfo("Cart", f"Added {game_name} to the cart!")

    def place_order(self):
        if not cart:
            messagebox.showwarning("Cart", "Your cart is empty!")
            return

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

        Label(cartFrame, text="Your Cart", font=("cursive", 30, "bold"), bg="#333333", fg="white").place(x=50, y=20)

        y_position = 120
        total = 0

        for item in cart:
            Label(cartFrame, text=item['name'], font=("cursive", 20, "bold"), bg="gray", fg="white").place(x=50, y=y_position)
            Label(cartFrame, text=f"₹{item['price']}", font=("cursive", 20, "bold"), bg="gray", fg="white").place(x=400, y=y_position)
            
            remove_btn = Button(cartFrame, text="Remove", command=lambda g=item['name']: self.remove_from_cart(g), font=("cursive", 10, "bold"), width=10, bg="red", bd=0, fg="white", cursor="hand2", activebackground="red", activeforeground="white")
            remove_btn.place(x=600, y=y_position)
            
            y_position += 40
            total += item["price"]

        Label(cartFrame, text=f"Total:₹{total}", font=("cursive", 25, "bold"), bg="#333333", fg="white").place(x=50, y=y_position) 
        
        placeOrderButton = Button(cartFrame, command=self.place_order, text="Place Order", font=("cursive", 20, "bold"), width=15, bg="black", bd=0, fg="gold", cursor="hand2")
        placeOrderButton.place(x=50, y=y_position + 40)

    def main(self):
        frame = Frame(self.root, width=300, height=840, bg="#1C1C1C")
        frame.place(x=0,y=0)

        self.right_Frame = Frame(self.root,width=1230,height=840,bg="#333333")
        self.right_Frame.place(x=300,y=0)

        btnStoryGames = Button(frame,command=self.storyGames, text="Story Games", font=("cursive",20,"bold"),width=10,bg="#1C1C1C",bd=0,fg="light gray",cursor="hand2")
        btnStoryGames.place(x=50,y=100)
        
        btnFpsGames = Button(frame,command=self.fpsGame, text="FPS Games", font=("cursive",20,"bold"),width=10,bg="#1C1C1C",bd=0,fg="light gray",cursor="hand2")
        btnFpsGames.place(x=50,y=200)

        btnRpgGames = Button(frame,command=self.rpgGame, text="RPG Games", font=("cursive",20,"bold"),width=10,bg="#1C1C1C",bd=0,fg="light gray",cursor="hand2")
        btnRpgGames.place(x=50,y=300)

        btn2dGames = Button(frame,command=self._2DGame, text="2D Games", font=("cursive",20,"bold"),width=10,bg="#1C1C1C",bd=0,fg="light gray",cursor="hand2")
        btn2dGames.place(x=50,y=400)

        btnOnSaleGames = Button(frame,command=self.onSaleGame, text="On Sale", font=("cursive",20,"bold"),width=10,bg="#1C1C1C",bd=0,fg="light gray",cursor="hand2")
        btnOnSaleGames.place(x=50,y=500)

        btnCart = Button(frame,command=self.view_cart, text="Cart", font=("cursive",20,"bold"),width=10,bg="#1C1C1C",bd=0,fg="light gray",cursor="hand2")
        btnCart.place(x=50,y=600)

        btnBackHome = Button(frame,command=self.backHome, text="Back Home", font=("cursive",20,"bold"),width=10,bg="#1C1C1C",bd=0,fg="light gray",cursor="hand2")
        btnBackHome.place(x=50,y=700)
        
        # right frame content

        backButton = Button(self.right_Frame, text="<", command=self.backHome, font=("cursive", 20, "bold"), width=1, bg="#333333", bd=0, fg="white", activebackground="#333333", activeforeground="white", cursor="hand2")
        backButton.place(x=1, y=1)

        newReleaseLbl = Label(self.right_Frame, text="New Release", font=("open sans", 20, "bold"), bg="#333333", fg="white")
        newReleaseLbl.place(x=550, y=40)

    def storyGames(self):
        storyGamesFrame = Frame(self.root,width=1230,height=840,bg="#333333")
        storyGamesFrame.place(x=300,y=0)

        games = [
            {"name": "Alan Wake 2", "price": 2748, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/story_game_img1.jpg","description": "Saga Anderson arrives to investigate ritualistic murders in a small town. Alan Wake pens a dark story to shape the reality around him. These two heroes are somehow connected. Can they become the heroes they need to be?", "x": 350, "y": 40},
            {"name": "A Plague Tale: Requiem", "price": 2299, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/story_game_img2.jpg","description": "Embark on a heartrending journey into a brutal, breathtaking world, and discover the cost of saving those you love in a desperate struggle for survival. Strike from the shadows or unleash hell with a variety of weapons, tools and unearthly powers.", "x": 750, "y": 40},
            {"name": "Mafia", "price": 120, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/story_game_img3.jpg","description": "It’s 1930. After an inadvertent brush with the mafia, cabdriver Tommy Angelo is reluctantly thrust into the world of organized crime. Initially, he is uneasy about falling in with the Salieri family, but soon the rewards become too big to ignore.", "x": 1150, "y": 40},
            {"name": "Dishonored", "price": 670, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/story_game_img4.jpg","description": "Dishonored is an immersive first-person action game that casts you as a supernatural assassin driven by revenge. With Dishonored’s flexible combat system, creatively eliminate your targets as you combine the supernatural abilities, weapons and unusual gadgets at your disposal.", "x": 350, "y": 450},
            {"name": "Stray", "price": 1249, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/story_game_img5.jpg","description": "Lost, alone and separated from family, a stray cat must untangle an ancient mystery to escape a long-forgotten cybercity and find their way home.", "x": 750, "y": 450},
            {"name": "Resident Evil 8", "price": 2399, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/story_game_img6.jpg","description": "Experience survival horror like never before in the 8th major installment in the Resident Evil franchise - Resident Evil Village. With detailed graphics, intense first-person action and masterful storytelling, the terror has never felt more realistic.", "x": 1150, "y": 450}
        ]

        for game in games:
            image = Image.open(game["image"])
            image = image.resize((250, 300), Image.Resampling.LANCZOS)
            photoimage = ImageTk.PhotoImage(image)

            lblGame = Label(self.root, image=photoimage, bd=4)
            lblGame.image = photoimage
            lblGame.place(x=game["x"], y=game["y"])

            # Create an 'action' button but hide it initially
            hoverButton = Button(self.root, text="View Details", font=("cursive", 10, "bold"), bg="#333333", fg="white", bd=0, cursor="hand2", command=lambda g=game: self.show_game_details(g))
            hoverButton.place_forget()

            # Function to display the button when the user hovers over the image
            def on_enter(event, button=hoverButton, x=game["x"], y=game["y"]):
                button.place(x=x + 170, y=y + 10)  # Top right corner of the image

            # Function to hide the button when the user moves the cursor away
            def on_leave(event, button=hoverButton):
                button.place_forget()

            # Bind hover in and hover out events
            lblGame.bind("<Enter>", on_enter)
            lblGame.bind("<Leave>", on_leave)
            hoverButton.bind("<Enter>", on_enter)
            hoverButton.bind("<Leave>", on_leave)

    def show_game_details(self, game):
            """Display detailed information of the clicked game"""
            # Clear the current frame
            for widget in self.root.winfo_children():
                    widget.destroy()
                    self.main()

            # Create a new frame for game details
            gameDetailFrame = Frame(self.root, width=1230, height=840, bg="#333333")
            gameDetailFrame.place(x=300, y=0)

            # Display the game image in larger size
            image = Image.open(game["image"])
            image = image.resize((500, 600), Image.Resampling.LANCZOS)
            photoimage = ImageTk.PhotoImage(image)

            lblGame = Label(gameDetailFrame, image=photoimage, bd=4)
            lblGame.image = photoimage
            lblGame.place(x=50, y=100)

            # Display the game name
            gameName = Label(gameDetailFrame, text=game["name"], font=("cursive", 30, "bold"), bg="#333333", fg="white")
            gameName.place(x=600, y=100)

            # Display the game description
            gameDescription = Label(gameDetailFrame, text=game["description"], wraplength=500, justify="left", font=("cursive", 16), bg="#333333", fg="white")
            gameDescription.place(x=600, y=160)

            # Display the game price
            gamePrice = Label(gameDetailFrame, text=f"Price: ₹{game['price']}", font=("cursive", 20, "bold"), bg="#333333", fg="white")
            gamePrice.place(x=600, y=300)

            # Add to Cart button
            btnAddToCart = Button(gameDetailFrame, command=lambda: self.add_to_cart(game["name"], game["price"]), text="Add To Cart", font=("cursive", 20, "bold"), width=15, bg="green", fg="white", cursor="hand2")
            btnAddToCart.place(x=600, y=400)

            # Back button to return to the game list
            btnBack = Button(gameDetailFrame, text="Back to Games", font=("cursive", 20, "bold"), width=15, bg="red", fg="white", cursor="hand2", command=self.storyGames)
            btnBack.place(x=600, y=500)

    def fpsGame(self):
        storyGamesFrame = Frame(self.root,width=1230,height=840,bg="#333333")
        storyGamesFrame.place(x=300,y=0)

        games = [
            {"name": "Doom Eternal", "price": 899, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/fps_game_img1.jpg","description": "Hell’s armies have invaded Earth. Become the Slayer in an epic single-player campaign to conquer demons across dimensions and stop the final destruction of humanity. The only thing they fear... is you.", "x": 350, "y": 40},
            {"name": "Metro Exodus", "price": 450, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/fps_game_img2.jpg","description": "Flee the shattered ruins of the Moscow Metro and embark on an epic, continent-spanning journey across the post-apocalyptic Russian wilderness. Explore vast, non-linear levels, lose yourself in an immersive, sandbox survival experience, and follow a thrilling story-line that spans an entire year in the", "x": 750, "y": 40},
            {"name": "turbo Overkill", "price": 1100, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/fps_game_img3.jpg","description": "Turbo Overkill is complete and with many new updates (just in: spectacular ending credits). Clean up Paradise with your chainsaw leg, 15+ weapons & hovercar, and battle Syn (a super AI), bounty hunters, and cyberpunks aplenty. Apogee's most outrageous FPS since Duke Nukem 3D. Good hunting, Sir!", "x": 1150, "y": 40},
            {"name": "Ultrakill", "price": 1100, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/fps_game_img4.jpg","description": "ULTRAKILL is a fast-paced ultraviolent retro FPS combining the skill-based style scoring from character action games with unadulterated carnage inspired by the best shooters of the '90s. Rip apart your foes with varied destructive weapons and shower in their blood to regain your health.", "x": 350, "y": 450},
            {"name": "Valorant", "price": 0, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/fps_game_img5.jpg","description": "VALORANT is a character-based 5v5 tactical shooter set on the global stage. Outwit, outplay, and outshine your competition with tactical abilities, precise gunplay, and adaptive teamwork.", "x": 750, "y": 450},
            {"name": "Overwatch 2", "price": 1249, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/fps_game_img6.jpg","description": "Overwatch 2 is a critically acclaimed, team-based shooter game set in an optimistic future with an evolving roster of heroes. Team up with friends and jump in today.", "x": 1150, "y": 450}
        ]

        for game in games:
            image = Image.open(game["image"])
            image = image.resize((250, 300), Image.Resampling.LANCZOS)
            photoimage = ImageTk.PhotoImage(image)

            lblGame = Label(self.root, image=photoimage, bd=4)
            lblGame.image = photoimage
            lblGame.place(x=game["x"], y=game["y"])

            # Create an 'action' button but hide it initially
            hoverButton = Button(self.root, text="View Details", font=("cursive", 10, "bold"), bg="#333333", fg="white", bd=0, cursor="hand2", command=lambda g=game: self.show_game_details(g))
            hoverButton.place_forget()

            # Function to display the button when the user hovers over the image
            def on_enter(event, button=hoverButton, x=game["x"], y=game["y"]):
                button.place(x=x + 170, y=y + 10)  # Top right corner of the image

            # Function to hide the button when the user moves the cursor away
            def on_leave(event, button=hoverButton):
                button.place_forget()

            # Bind hover in and hover out events
            lblGame.bind("<Enter>", on_enter)
            lblGame.bind("<Leave>", on_leave)
            hoverButton.bind("<Enter>", on_enter)
            hoverButton.bind("<Leave>", on_leave)

    def rpgGame(self):
        rpgGamesFrame = Frame(self.root,width=1230,height=840,bg="#333333")
        rpgGamesFrame.place(x=300,y=0)

        games = [
            {"name": "Genshin Impact", "price": 0, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/rpg_game_img1.jpg","description": "Embark on a journey across Teyvat to find your lost sibling and seek answers from The Seven — the gods of each element. Explore this wondrous world, join forces with a diverse range of characters, and unravel the countless mysteries that Teyvat holds...", "x": 350, "y": 40},
            {"name": "Final Fantasy 14", "price": 719, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/rpg_game_img2.jpg","description": "Join over 30 million adventurers worldwide and take part in an epic and ever-changing FINAL FANTASY. Experience an unforgettable story, exhilarating battles, and a myriad of captivating environments to explore.", "x": 750, "y": 40},
            {"name": "Dragon’s Dogma 2", "price": 4474, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/rpg_game_img3.jpg","description": "Dragon’s Dogma 2 is a single player, narrative driven action-RPG that challenges the players to choose their own experience – from the appearance of their Arisen, their vocation, their party, how to approach different situations and more - in a truly immersive fantasy world.", "x": 1150, "y": 40},
            {"name": "Red Dead Redemption 2", "price": 3199, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/rpg_game_img4.jpg","description": "Winner of over 175 Game of the Year Awards and recipient of over 250 perfect scores, RDR2 is the epic tale of outlaw Arthur Morgan and the infamous Van der Linde gang, on the run across America at the dawn of the modern age. Also includes access to the shared living world of Red Dead Online.", "x": 350, "y": 450},
            {"name": "Starfield", "price": 4999, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/rpg_game_img5.jpg","description": "Starfield is the first new universe in 25 years from Bethesda Game Studios, the award-winning creators of The Elder Scrolls V: Skyrim and Fallout 4.", "x": 750, "y": 450},
            {"name": "Baldur’s Gate 3", "price": 2999, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/rpg_game_img6.jpg","description": "Baldur’s Gate 3 is a story-rich, party-based RPG set in the universe of Dungeons & Dragons, where your choices shape a tale of fellowship and betrayal, survival and sacrifice, and the lure of absolute power.", "x": 1150, "y": 450}
        ]

        for game in games:
            image = Image.open(game["image"])
            image = image.resize((250, 300), Image.Resampling.LANCZOS)
            photoimage = ImageTk.PhotoImage(image)

            lblGame = Label(self.root, image=photoimage, bd=4)
            lblGame.image = photoimage
            lblGame.place(x=game["x"], y=game["y"])

            # Create an 'action' button but hide it initially
            hoverButton = Button(self.root, text="View Details", font=("cursive", 10, "bold"), bg="#333333", fg="white", bd=0, cursor="hand2", command=lambda g=game: self.show_game_details(g))
            hoverButton.place_forget()

            # Function to display the button when the user hovers over the image
            def on_enter(event, button=hoverButton, x=game["x"], y=game["y"]):
                button.place(x=x + 170, y=y + 10)  # Top right corner of the image

            # Function to hide the button when the user moves the cursor away
            def on_leave(event, button=hoverButton):
                button.place_forget()

            # Bind hover in and hover out events
            lblGame.bind("<Enter>", on_enter)
            lblGame.bind("<Leave>", on_leave)
            hoverButton.bind("<Enter>", on_enter)
            hoverButton.bind("<Leave>", on_leave)

    def _2DGame(self):
        _2dGamesFrame = Frame(self.root,width=1230,height=840,bg="#333333")
        _2dGamesFrame.place(x=300,y=0)

        games = [
            {"name": "Inside", "price": 56, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/2d_game_img1.jpg","description": "Hunted and alone, a boy finds himself drawn into the center of a dark project. INSIDE is a dark, narrative-driven platformer combining intense action with challenging puzzles. It has been critically acclaimed for its moody art style, ambient soundtrack and unsettling atmosphere.", "x": 350, "y": 40},
            {"name": "Hollow Knight", "price": 690, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/2d_game_img2.jpg","description": "Forge your own path in Hollow Knight! An epic action adventure through a vast ruined kingdom of insects and heroes. Explore twisting caverns, battle tainted creatures and befriend bizarre bugs, all in a classic, hand-drawn 2D style.", "x": 750, "y": 40},
            {"name": "Terraria", "price": 480, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/2d_game_img3.jpg","description": "Dig, fight, explore, build! Nothing is impossible in this action-packed adventure game. Four Pack also available!", "x": 1150, "y": 40},
            {"name": "Ori And the Blind Forest", "price": 1299, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/2d_game_img4.jpg","description": "“Ori and the Blind Forest” tells the tale of a young orphan destined for heroics, through a visually stunning action-platformer crafted by Moon Studios for PC.", "x": 350, "y": 450},
            {"name": "Celeste", "price": 220, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/2d_game_img5.jpg","description": "Help Madeline survive her inner demons on her journey to the top of Celeste Mountain, in this super-tight platformer from the creators of TowerFall. Brave hundreds of hand-crafted challenges, uncover devious secrets, and piece together the mystery of the mountain.", "x": 750, "y": 450},
            {"name": "Limbo", "price": 36, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/2d_game_img6.jpg","description": "Uncertain of his sister's fate, a boy enters LIMBO", "x": 1150, "y": 450}
        ]

        for game in games:
            image = Image.open(game["image"])
            image = image.resize((250, 300), Image.Resampling.LANCZOS)
            photoimage = ImageTk.PhotoImage(image)

            lblGame = Label(self.root, image=photoimage, bd=4)
            lblGame.image = photoimage
            lblGame.place(x=game["x"], y=game["y"])

            # Create an 'action' button but hide it initially
            hoverButton = Button(self.root, text="View Details", font=("cursive", 10, "bold"), bg="#333333", fg="white", bd=0, cursor="hand2", command=lambda g=game: self.show_game_details(g))
            hoverButton.place_forget()

            # Function to display the button when the user hovers over the image
            def on_enter(event, button=hoverButton, x=game["x"], y=game["y"]):
                button.place(x=x + 170, y=y + 10)  # Top right corner of the image

            # Function to hide the button when the user moves the cursor away
            def on_leave(event, button=hoverButton):
                button.place_forget()

            # Bind hover in and hover out events
            lblGame.bind("<Enter>", on_enter)
            lblGame.bind("<Leave>", on_leave)
            hoverButton.bind("<Enter>", on_enter)
            hoverButton.bind("<Leave>", on_leave)

    def onSaleGame(self):
        onSaleGamesFrame = Frame(self.root,width=1230,height=840,bg="#333333")
        onSaleGamesFrame.place(x=300,y=0)

        games = [
            {"name": "Mafia", "price": 120, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/story_game_img3.jpg","description": "It’s 1930. After an inadvertent brush with the mafia, cabdriver Tommy Angelo is reluctantly thrust into the world of organized crime. Initially, he is uneasy about falling in with the Salieri family, but soon the rewards become too big to ignore.", "x": 350, "y": 40},
            {"name": "Metro Exodus", "price": 450, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/fps_game_img2.jpg","description": "Flee the shattered ruins of the Moscow Metro and embark on an epic, continent-spanning journey across the post-apocalyptic Russian wilderness. Explore vast, non-linear levels, lose yourself in an immersive, sandbox survival experience, and follow a thrilling story-line that spans an entire year in the", "x": 750, "y": 40},
            {"name": "Celeste", "price": 220, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/2d_game_img5.jpg","description": "Help Madeline survive her inner demons on her journey to the top of Celeste Mountain, in this super-tight platformer from the creators of TowerFall. Brave hundreds of hand-crafted challenges, uncover devious secrets, and piece together the mystery of the mountain.", "x": 1150, "y": 40},
            {"name": "Limbo", "price": 36, "image": "C:/Users/NEEL PATEL/OneDrive/Desktop/project images/2d_game_img6.jpg","description": "Uncertain of his sister's fate, a boy enters LIMBO", "x": 350, "y": 450}
        ]

        for game in games:
            image = Image.open(game["image"])
            image = image.resize((250, 300), Image.Resampling.LANCZOS)
            photoimage = ImageTk.PhotoImage(image)

            lblGame = Label(self.root, image=photoimage, bd=4)
            lblGame.image = photoimage
            lblGame.place(x=game["x"], y=game["y"])

            # Create an 'action' button but hide it initially
            hoverButton = Button(self.root, text="View Details", font=("cursive", 10, "bold"), bg="#333333", fg="white", bd=0, cursor="hand2", command=lambda g=game: self.show_game_details(g))
            hoverButton.place_forget()

            # Function to display the button when the user hovers over the image
            def on_enter(event, button=hoverButton, x=game["x"], y=game["y"]):
                button.place(x=x + 170, y=y + 10)  # Top right corner of the image

            # Function to hide the button when the user moves the cursor away
            def on_leave(event, button=hoverButton):
                button.place_forget()

            # Bind hover in and hover out events
            lblGame.bind("<Enter>", on_enter)
            lblGame.bind("<Leave>", on_leave)
            hoverButton.bind("<Enter>", on_enter)
            hoverButton.bind("<Leave>", on_leave)   

    def backHome(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        from home import videogame
        videogame(self.root)

if __name__ == "__main__":
    root = Tk()
    obj = browser(root)
    root.mainloop()