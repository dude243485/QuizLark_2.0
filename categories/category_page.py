import customtkinter as ctk
from PIL import Image
import authentication as auth
from categories.category import Category
from CTkMessagebox import CTkMessagebox

lightBlue = "#EDF7F7"
darkBlue = "#1581B4"

class CategoryFrame(ctk.CTkFrame):
    def __init__(self, parent, playerId, controller ):
        super().__init__(parent)
        self.playerId = playerId
        self.controller = controller

        self.place(x=0, y=0, relwidth=1, relheight= 1)
        self.configure(fg_color = lightBlue)
        
        self.total_categories = len(auth.get_total_categories())

        self.imageUrl_list = [
            "images/knowledge.png",
            "images/sports (1).png",
            "images/tv.png",
            "images/images (3).png",
            "images/robotic-hand.png",
            "images/parchment.png",
            "images/stethoscope.png",
            "images/atomic.png",
            "images/cross.png",
            "images/politician.png"
        ]
        self.titleList = [
            "general",
            "sports",
            "movie",
            "arts",
            "tech",
            "history_",
            "medicine",
            "science",
            "bible",
            "politics"
        ]

        self.header = ctk.CTkLabel(self, text= "CATEGORIES", text_color="black", font=("Montserrat Extrabold", 36), justify = "center")
        self.header.pack(pady= (20,20), anchor="center" , fill ="x")

        self.progress_list = auth.get_game_progress(self.playerId)
        self.container = ctk.CTkFrame(self, fg_color="white")
        self.container.pack(pady= 10, padx=10)

        
        
        for i in range(2):
            self.container.grid_rowconfigure(i, weight=1)

        for j in range(5):
            self.container.grid_columnconfigure(j, weight=1)

        for row in range(2):
            for col in range(5):
                # self.label = ctk.CTkLabel(self, text = "Boxes", corner_radius= 5)
                self.category = Category(self.container, self.imageUrl_list[col + (5*row)], self.titleList[col + (5*row)], self.progress_list[col + (5*row)], self.on_click)
                self.category.grid(row = row, column = col, padx =5, pady =5, sticky = "nsew")

    def on_click(self, title):
        
        def show_error_msg():
            msg = CTkMessagebox(title="Error",
                                message="Category Completed, Do you wan't to restart progress",
                                icon = "cancel", 
                                option_1 = "YES",
                                option_2= "NO",
                                fg_color="white",
                                bg_color = lightBlue,
                                border_color="white",
                                border_width=5,
                                
                                )
            return msg.get()
            
        if title == "general":
            if auth.get_actual_progress(self.playerId,title) >= 100:
                print("level completed")
                #show error message
                reply = show_error_msg()
                if reply == "YES":
                    auth.reset_progress(self.playerId, title)
                    self.controller.show_play_frame(self.playerId, title)
                  
                
            else:
                self.controller.show_play_frame(self.playerId, title)
            
                

        