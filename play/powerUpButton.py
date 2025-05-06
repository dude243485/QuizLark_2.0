import customtkinter as ctk

lightBlue = "#EDF7F7"
darkBlue = "#1581B4"
hoverBlue = "#B9E1F5"

class PowerUpButton(ctk.CTkFrame):
    def __init__(self, parent, controller, image, text, button_command):
        super().__init__(parent)
        self.pack(side ="right", padx=15)
        self.configure(fg_color = lightBlue)

        #define instance variable
        self.controller = controller
        self.image = image
        self.text = text
        self.on_click = button_command

        self.button = ctk.CTkButton(self, text = None, fg_color=lightBlue, image = self.image, width=45, hover_color= hoverBlue
                                    ,command = self.on_click)
        self.button.pack(padx = (0,10), side ="left")

        self.text_label = ctk.CTkLabel(self, text=self.text,  font =("Montserrat", 16, "bold"), text_color= "black")
        self.text_label.pack(side = "left")
