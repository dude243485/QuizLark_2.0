import customtkinter as ctk
from PIL import Image, ImageTk
from CTkMessagebox import CTkMessagebox
from main_menu.statusIcon import statusIcon
import json
import authentication as auth
from main_menu.statusButton import statusButton
from main_menu.gift import giftWindow
import datetime as dt


lightBlue = "#EDF7F7"
darkBlue = "#1581B4"



class mainMenuFrame(ctk.CTkFrame):
    def __init__(self, parent, controller, playerId):
        super().__init__(parent)
        self.controller = controller
        self.playerId = playerId

        #set frame properties
        self.place(x=0, y=0, relwidth=1, relheight= 1)
        self.configure(fg_color=lightBlue)


        #create widgets

        self.status_bar = ctk.CTkFrame(self, fg_color=lightBlue )
        self.status_bar.pack(fill="x", padx= 12, pady=10)

        #create xp icon
        self.xp_image = Image.open("images/xp.png")
        self.xp_text = auth.get_xp(self.playerId)
        self.xp = statusIcon(self.status_bar, self.xp_image, self.xp_text )

        #create money icon
        self.money_image = Image.open("images/money.png")
        self.money_text = auth.get_money(self.playerId)
        self.money = statusIcon(self.status_bar, self.money_image, self.money_text )

        #create store button
        self.store_image = Image.open("images/store.png")
        self.store_button = statusButton(self.status_bar, self.store_image, "STORE", self.show_store)

        #create gift button
        self.gift_image = Image.open("images/gift.png")
        self.gift_button = statusButton(self.status_bar, self.gift_image, "GIFTS", self.show_gift)

        #center widgets
        self.center = ctk.CTkFrame(self, fg_color=lightBlue)
        self.center.pack(fill="both")

        self.company_name = ctk.CTkLabel(self.center, text="QuizLark",
                                         font=("Montserrat Extrabold", 32), text_color="black")
        self.company_name.pack(pady=(20, 0))

        #create buttons 
        self.play = ctk.CTkButton(self.center, text="PLAY",text_color="white",
                                  font=("Montserrat Extrabold", 40),
                                  fg_color=darkBlue, width=500, height=100, command = self.show_categories )
        self.play.pack(pady=(10, 15))

        self.statistics = ctk.CTkButton(self.center, text="STATS",text_color="white",
                                  font=("Montserrat Extrabold", 40),
                                  fg_color=darkBlue, width=500, height=100, command = self.show_stats )
        self.statistics.pack(pady=(15, 15))
        self.quit_button = ctk.CTkButton(self.center, text="QUIT",text_color="white",
                                  font=("Montserrat Extrabold", 40),
                                  fg_color=darkBlue, width=500, height=100,
                                  command = self.controller.destroy)
        self.quit_button.pack(pady=(10, 15))
        

    #show store
    def show_store(self):
        self.controller.show_store_frame(self.playerId)

    #on gift button click
    def show_gift(self):
        self.gift_window = giftWindow(self.controller, self.playerId)

    def show_stats(self):
        self.controller.show_stats_frame(self.playerId)

    def show_categories(self):
        self.controller.show_categories_frame(self.playerId)

        
    


    
        
        