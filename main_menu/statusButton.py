import customtkinter as ctk

lightBlue = "#EDF7F7"
darkBlue = "#1581B4"
hoverColor = "#E1F1F6"

class statusButton(ctk.CTkFrame):
    def __init__(self, parent, buttonImage, buttonText, buttonCommand):
        super().__init__(parent)
        self.buttonImage = buttonImage
        self.buttonText = buttonText
        self.buttonCommand = buttonCommand

        self.configure(fg_color=lightBlue)
        self.pack(side="right", padx=10)

        #for the image
        self.image = self.buttonImage
        self.height = 200
        
        self.ratio = self.image.width/self.image.height
        self.newWidth = int(self.height*self.ratio)
        
        self.resized = self.image.resize((self.newWidth, self.height))
        self.image = ctk.CTkImage(light_image = self.resized, size = (45,45))

        self.imageIcon = ctk.CTkButton(self, image=self.image, text="", fg_color= lightBlue,
                                      command= self.buttonCommand, width=60, hover_color= hoverColor)
        self.imageText = ctk.CTkLabel(self, text=self.buttonText, fg_color=lightBlue, 
                                      text_color="black", font=("Montserrat", 16, "bold")
                                      )
        
        #putting it on the screen
        self.imageIcon.pack(pady=(0, 4))
        self.imageText.pack()