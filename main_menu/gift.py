import customtkinter as ctk
from PIL import Image
import random
import authentication as auth

lightBlue = "#EDF7F7"
darkBlue = "#1581B4"

class giftWindow(ctk.CTkToplevel):
    def __init__(self, controller, playerId):
        super().__init__()
        self.playerId = playerId
        self.controller = controller

        #set window properties
        self.resizable(False, False)
        self.geometry("330x430")
        self.transient(controller)
        self.grab_set()

        

        self.configure(fg_color=lightBlue)
        self.gift_list = ["Save Me", "Eliminate", "Instant", "Hint"]
        self.quantity = random.randint(1,3)
        self.index = random.randint(0,3)
        self.images_list = [Image.open("images/save me.png"),
                            Image.open("images/eliminate.png"),
                            Image.open("images/instant.png"),
                            Image.open("images/hint.png")]
        self.description_list = [
            "Maintain your progress and keep playing after getting a question wrong.",
            "Provides the correct answer to the current question.",
            "Eliminates two wrong answers from the current question.",
            "Displays a hint on the current question."
        ]
        self.contain = ctk.CTkFrame(self, fg_color=lightBlue)
        #self.contain.place(relx=0.5, rely=0.5, anchor = ctk.CENTER)
        self.contain.pack(anchor = ctk.CENTER, pady= (15, 0))

        #create widgets
        self.header_label = ctk.CTkLabel(self.contain, text="Daily Gift!", font=("Montserrat Extrabold", 16),
                                   text_color= darkBlue)
        self.header_label.pack(pady=(20,0))

        self.power_up = ctk.CTkLabel(self.contain, text= f"{self.gift_list[self.index]} x{self.quantity}",
                                    font=("Montserrat Extrabold", 28),
                                   text_color= "black")
        self.power_up.pack()

        self.power_up_icon = ctk.CTkLabel(self.contain, image = self.prepare_image(self.images_list[self.index], 150 ), text="")
        self.power_up_icon.pack(pady=20)

        self.info = ctk.CTkLabel(self.contain, text=self.description_list[self.index], font=("Montserrat", 13),
                                   text_color= "black", wraplength=230)
        self.info.pack(pady=5)

        #create the continue button
        self.buy_button = ctk.CTkButton(self, fg_color=darkBlue, text_color="white", text="Continue",
                                        font=("Montserrat Extrabold", 16), width=200, height=40,
                                        command = self.on_continue)
        self.buy_button.pack(padx=35, pady=(0,30))


    def prepare_image(self, image, size):
        """converts an image into the customtkinter format"""
        self.height = size
        
        self.ratio = image.width/image.height
        self.newWidth = int(self.height*self.ratio)
        
        self.resized = image.resize((self.newWidth, self.height))
        self.image = ctk.CTkImage(light_image = self.resized, size = (self.newWidth,self.height))
        return self.image
    
    def on_continue(self):
        if self.gift_list[self.index] == "Save Me":
            auth.increase_value(self.playerId, "save me", self.quantity)
            

        elif self.gift_list[self.index] == "Instant":
            auth.increase_value(self.playerId, "instant", self.quantity)
            

        elif self.gift_list[self.index] == "Eliminate":
            auth.increase_value(self.playerId, "eliminate", self.quantity)
            

        elif self.gift_list[self.index] == "Hint":
            auth.increase_value(self.playerId, "hint", self.quantity)

        #close window
        self.destroy()

            