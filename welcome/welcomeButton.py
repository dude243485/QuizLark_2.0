import customtkinter as ctk
lightBlue = "#EDF7F7"
darkBlue = "#1581B4"

class welcomeButtons(ctk.CTkButton):
    def __init__(self, parent, button_text, button_command):
        super().__init__(parent)
        self.configure(width=330,
                       text_color = "white",
                       text= button_text,
                       fg_color = darkBlue,
                       font=("Montserrat",26 , "bold"),
                       height= 80,
                       command = button_command)
        self.pack(padx= 15, side = "left")
      