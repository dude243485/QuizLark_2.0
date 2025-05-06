import customtkinter as ctk
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import authentication as auth



class chartFrame(ctk.CTkFrame):
    def __init__(self, parent, playerId):
        super().__init__(parent)
        self.playerId = playerId
        self.pack()
        self.configure(fg_color = "white")

        #for pie chart 
        #self.labels = ["History", "Science", "Politics", "Medicine"]
        #self.sizes = [35, 25, 20,20]
        self.colors = ["#A7CFE6", "#719EBD", "#25506C", "#0C658D"]

        self.labels, self.sizes = auth.get_top_categories(self.playerId)



        #create the figure
        self.fig, self.ax = plt.subplots(figsize = (5,4), dpi =100)
        explode = (0.1, 0,0,0)
        wedges, texts, autotexts = self.ax.pie(self.sizes, 
                                          labels = self.labels, 
                                          autopct = "%1.1f%%", 
                                          colors = self.colors,  startangle= 90)
        
        #customizing the pie chart
        for text in texts:
            text.set_fontsize(14)
            text.set_fontfamily("Montserrat")
            text.set_color("black")

        #customizing the percentge
        for autotext in autotexts:
            autotext.set_fontsize(12)
            autotext.set_fontfamily("Montserrat")
            autotext.set_color("white")

        self.ax.axis("equal") #ensures pie chart is a cicle

        self.canvas = FigureCanvasTkAgg(self.fig, master = self)

        self.canvas.draw_idle() 
        self.canvas.get_tk_widget().pack(pady=20)
        