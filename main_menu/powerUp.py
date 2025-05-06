import customtkinter as ctk
from PIL import Image

lightBlue = "#EDF7F7"
darkBlue = "#1581B4"

class powerUp(ctk.CTkFrame):
    def __init__(self, parent, power_up_name, power_up_image, description, quantity, price, buy_command):
        super().__init__(parent)

        self.name = power_up_name
        self.image = power_up_image
        self.description = description
        self.quantity = quantity
        self.price = price
        self.buy_command = buy_command

        self.configure(fg_color= "white")
        self.pack(side="left", padx=15)

        #create widgets
        self.power_up = ctk.CTkLabel(self, text=self.name, font=("Montserrat Extrabold", 28),
                                   text_color= "black")
        self.power_up.pack(pady=(20,0))
        self.info = ctk.CTkLabel(self, text=self.description, font=("Montserrat", 13),
                                   text_color= "black", wraplength=230)
        self.info.pack()

        self.quantity_label = ctk.CTkLabel(self, text=f"In-stock : {self.quantity}", font=("Montserrat Extrabold", 16),
                                   text_color= darkBlue)
        self.quantity_label.pack()

        

        #create actual image
        self.power_up_icon = ctk.CTkLabel(self, image=self.prepare_image(self.image, 140), text="")
        self.power_up_icon.pack(pady=20)


        self.price_label = ctk.CTkLabel(self, text=f"Price : {self.price}", font=("Montserrat Extrabold", 16),
                                   text_color= darkBlue)
        self.price_label.pack()

        #create the buy button
        self.buy_button = ctk.CTkButton(self, fg_color=darkBlue, text_color="white", text="Buy",
                                        font=("Montserrat Extrabold", 16), width=200, height=40,
                                        command = self.buy_command)
        self.buy_button.pack(padx=35, pady=(0,30))

    def prepare_image(self, image, size):
        """converts an image into the customtkinter format"""
        self.height = size
        
        self.ratio = image.width/image.height
        self.newWidth = int(self.height*self.ratio)
        
        self.resized = image.resize((self.newWidth, self.height))
        self.image = ctk.CTkImage(light_image = self.resized, size = (self.newWidth,self.height))
        return self.image

        
        