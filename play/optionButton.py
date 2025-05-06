import customtkinter as ctk
import tkinter.font as tkfont

lightBlue = "#EDF7F7"
darkBlue = "#1581B4"
hoverBlue = "#B9E1F5"

class OptionButton(ctk.CTkButton):
    def __init__(self, parent,master, text, row, col):
        super().__init__(parent)
        self.master = master
        self.text = text
        self.row = row
        self.col = col

        font = tkfont.Font(family = "Montserrat", size =20, weight="bold")
        text_width = font.measure(self.text)

        base_width = max(text_width + 20, 390)
        self.configure(fg_color = "white", 
                       width = base_width, 
                       height = 70,
                        text =self.text,
                        text_color = "black", 
                        font = ("Montserrat", 20, "bold"), 
                        hover_color = hoverBlue, 
                        command = lambda : self.onButtonClick(self.cget("text"), self)
                         )
                         
        self.grid(row = self.row, column = self.col, ipady = 5, ipadx = 10, padx = 10, pady=10)
        



    def onButtonClick(self, choice, clicked_button):
        self.master.questionAttempted(choice, clicked_button)