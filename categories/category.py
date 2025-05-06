import customtkinter as ctk
from PIL import Image
import authentication as auth


lightBlue = "#EDF7F7"
darkBlue = "#1581B4"
hoverBlue = "#B9E1F5"
class Category(ctk.CTkFrame):
    def __init__(self, parent, image, title, progress, on_click):
        super().__init__(parent)
        self.image = image
        self.title = title
        self.on_click = on_click
        self.configure(fg_color = "white", width=200,)
        #button image
        self.image_button = ctk.CTkButton(self, image= self.prepare_image(Image.open(image), 200), fg_color= lightBlue,
                                          text="", command = lambda : self.on_click(self.title), hover_color=hoverBlue)
        self.image_button.pack()

        #button title
        self.button_title = ctk.CTkLabel(self, text =title, text_color="black")
        self.button_title.pack()

        #create progress bar
        self.progress = ctk.CTkProgressBar(self)
        self.progress.pack()
        self.progress.set(progress/100)

    def prepare_image(self, image, size):
        """converts an image into the customtkinter format"""
        self.height = size
        
        self.ratio = image.width/image.height
        self.newWidth = int(self.height*self.ratio)
        
        self.resized = image.resize((self.newWidth, self.height))
        self.image = ctk.CTkImage(light_image = self.resized, size = (self.newWidth,self.height))
        return self.image