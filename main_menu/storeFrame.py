import customtkinter as ctk
from PIL import Image
from main_menu.powerUp import powerUp
import authentication as auth
from CTkMessagebox import CTkMessagebox

lightBlue = "#EDF7F7"
darkBlue = "#1581B4"

class storeFrame(ctk.CTkFrame):
    def __init__(self,parent, controller, playerId):
        super().__init__(parent)
        self.controller = controller
        self.playerId = playerId
        
        #design appearance
        self.configure(fg_color=lightBlue)
        self.place(x=0, y=0, relwidth=1, relheight= 1)

        #using an image for the back button
        self.back_button =  Image.open("images/back arrow.png")
        self.height = 200
        
        self.ratio = self.back_button.width/self.back_button.height
        self.newWidth = int(self.height*self.ratio)
        
        self.resized = self.back_button.resize((self.newWidth, self.height))
        self.back_button = ctk.CTkImage(light_image = self.resized, size = (50,50))
        
        #create the actual button
        self.go_back_button = ctk.CTkButton(self, image=self.back_button,
                                            command= self.show_main_menu, text="",
                                            fg_color=lightBlue, hover_color=lightBlue)
        self.go_back_button.pack(side="top", anchor="nw", pady=15, padx=8)

        self.header = ctk.CTkLabel(self, text = "POWER-UP STORE", font=("Montserrat Extrabold", 32),
                                   text_color= "black")
        self.header.pack()

        self.contain = ctk.CTkFrame(self, fg_color = lightBlue)
        self.contain.place( relx=0.5, rely=0.55, anchor = ctk.CENTER)

        
        self.save_me = powerUp(self.contain,
                               "Save Me",
                               Image.open("images/save me.png"),
                               "Maintain your progress and keep playing after getting a question wrong.",
                               auth.get_save_me(self.playerId),
                               200,
                               lambda : self.on_buy(self.playerId, 200, "save me"))

        self.instant = powerUp(self.contain,
                               "Instant",
                               Image.open("images/instant.png"),
                               "Provides the correct answer to the current question.",
                               auth.get_instant(self.playerId),
                               150,
                               lambda : self.on_buy(self.playerId, 150, "instant"))
        
        self.eliminate = powerUp(self.contain,
                               "Eliminate",
                               Image.open("images/eliminate.png"),
                               "Eliminates two wrong answers from the current question.",
                               auth.get_eliminate(self.playerId),
                               150,
                               lambda : self.on_buy(self.playerId, 150, "eliminate"))
        self.hint = powerUp(self.contain,
                               "Hint",
                               Image.open("images/hint.png"),
                               "Displays a hint on the current question.",
                               auth.get_hint(self.playerId),
                               150,
                               lambda : self.on_buy(self.playerId, 150, "hint"))

    #when the back button is clicked
    def show_main_menu(self):
        self.controller.show_page(self.controller.main_menu_frame)

    def on_buy(self, playerId, price, item):
        if auth.get_money(playerId) >= price:
            print("Transaction successful")
            if item == "save me":
                auth.increase_value(playerId, "save me", 1)
                auth.set_money(playerId, price)
                self.save_me.quantity_label.configure(text= f"In-stock : {auth.get_save_me(playerId)}")
                self.controller.main_menu_frame.money.imageText.configure(text=auth.get_money(self.playerId))

            elif item == "instant":
                auth.increase_value(playerId, "instant", 1)
                auth.set_money(playerId, price)
                self.instant.quantity_label.configure(text= f"In-stock : {auth.get_instant(playerId)}")
                self.controller.main_menu_frame.money.imageText.configure(text=auth.get_money(self.playerId))

            elif item == "eliminate":
                auth.increase_value(playerId, "eliminate", 1)
                auth.set_money(playerId, price)
                self.eliminate.quantity_label.configure(text= f"In-stock : {auth.get_eliminate(playerId)}")
                self.controller.main_menu_frame.money.imageText.configure(text=auth.get_money(self.playerId))

            elif item == "hint":
                auth.increase_value(playerId, "hint", 1)
                auth.set_money(playerId, price)
                self.hint.quantity_label.configure(text= f"In-stock : {auth.get_hint(playerId)}")
                self.controller.main_menu_frame.money.imageText.configure(text=auth.get_money(self.playerId))



        else:
            self.msg = CTkMessagebox(title="Error",
                                     message="Insufficient Funds",
                                     icon = "cancel", 
                                     option_1 = "OK",
                                     fg_color="white",
                                     bg_color = lightBlue,
                                     border_color="white",
                                     border_width=5
                                     )



