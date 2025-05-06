import customtkinter as ctk
from PIL import Image

lightBlue = "#EDF7F7"
darkBlue = "#1581B4"

class statusIcon(ctk.CTkFrame):
    def __init__(self, parent, iconImage, iconValue):
        super().__init__(parent)
        
        #setting properties
        self.configure(fg_color=lightBlue)
        self.pack(side="left", padx=10)

        #create widgets
        #for the image
        self.image = iconImage
        self.height = 200
        
        self.ratio = self.image.width/self.image.height
        self.newWidth = int(self.height*self.ratio)
        
        self.resized = self.image.resize((self.newWidth, self.height))
        self.image = ctk.CTkImage(light_image = self.resized, size = (40,40))

        self.imageIcon = ctk.CTkLabel(self, image=self.image, text="", fg_color= lightBlue)
        self.imageText = ctk.CTkLabel(self, text=iconValue, fg_color=lightBlue, 
                                      text_color=darkBlue, font=("Montserrat", 14, "bold"))

        #putting the widgets on the screen
        self.imageIcon.pack(side="left", padx= 8)
        self.imageText.pack(side = "left")
