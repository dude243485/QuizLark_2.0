import customtkinter as ctk

class statValue(ctk.CTkFrame):
    def __init__(self, parent, name, value):
        super().__init__(parent)

        self.name = name
        self.value = value

        #define frame properties
        self.configure(fg_color="white", height=30, width= 500, corner_radius = 10)
        self.pack(fill="x", padx= (0,15), pady=(8, 0))

        self.title = ctk.CTkLabel(self, text= self.name, text_color= "black",
                                  font = ("Montserrat", 14), anchor="w")
        self.title.pack(side = "left", padx= 15, pady=4)

        self.value_label = ctk.CTkLabel(self, text= self.value, font= ("Montserrat", 14), 
                                  text_color= "black")
        self.value_label.pack(side = "right", padx = 15)

