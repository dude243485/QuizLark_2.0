import customtkinter as ctk
from PIL import Image
import authentication as auth
from stat_page.Item import statValue

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from stat_page.chartFrame import chartFrame

lightBlue = "#EDF7F7"
darkBlue = "#1581B4"

class statsFrame(ctk.CTkFrame):
    def __init__(self, parent, controller, playerId):
        super().__init__(parent)
        self.controller = controller
        self.playerId = playerId

        #set frame properties
        self.configure(fg_color = lightBlue)
        self.place(x=0, y=0, relwidth=1, relheight= 1)

        #create return button
        self.go_back_button = ctk.CTkButton(self, image= self.prepare_image(Image.open("images/back arrow.png"), 40),
                                            command= self.show_main_menu, text="",
                                            fg_color=lightBlue, hover_color=lightBlue)
        self.go_back_button.pack(side="top", anchor="ne", pady=15, padx=8)

        self.contain = ctk.CTkFrame(self, fg_color=lightBlue)
        self.contain.pack(fill= "both", expand=True, pady=(0, 25), padx=25)

        self.details = ctk.CTkFrame(self.contain, fg_color=lightBlue)
        self.details.pack(fill= "both", expand=True, side="left")

        self.graph = ctk.CTkFrame(self.contain, fg_color="white", width=400)
        self.graph.pack(fill= "both", side = "left")

        self.stat_header = ctk.CTkLabel(self.details, text = "STATISTICS", font= ("Montserrat Extrabold", 28),
                                        text_color= darkBlue, anchor = "w", justify="left")
        self.stat_header.pack(fill="x")

        self.items_contain = ctk.CTkFrame(self.details, fg_color= lightBlue)
        self.items_contain.pack(fill= "both", expand = True, padx=(0, 20))

        self.attempted = statValue(self.items_contain, "Questions attempted", auth.get_stat(self.playerId, "questions attempted"))
        self.correct = statValue(self.items_contain, "Correct answers", auth.get_stat(self.playerId, "correct"))
        self.wrong = statValue(self.items_contain, "Wrong answers", auth.get_stat(self.playerId, "wrong"))
        self.played = statValue(self.items_contain, "Games played", auth.get_stat(self.playerId, "games played"))
        self.won = statValue(self.items_contain, "Games won", auth.get_stat(self.playerId, "games won"))

        self.rankings = ctk.CTkLabel(self.details, text = "LEADERBOARDS", font= ("Montserrat Extrabold", 24),
                                        text_color= darkBlue, anchor = "w", justify="left")
        self.rankings.pack(fill="x", pady = (10, 5))
        self.rank_container = ctk.CTkFrame(self.details, fg_color= "white")
        self.rank_container.pack(fill= "both", expand = True, padx=(0, 35))

        self.rank_contain = ctk.CTkFrame(self.rank_container, fg_color= darkBlue)
        self.rank_contain.pack(fill= "both", expand = True, padx=20, pady=20)

        self.ranked_list = auth.get_leaderboards()
        self.ranked_list.insert(0, ["Username", "XP", "Money", "name", "playerId"])

        for i, row in enumerate(self.ranked_list):

            if row[4] == self.playerId:
                padding = 2

            else:
                padding = 0

            for j, cell in enumerate(row):

                #so you won't print the id
                if j == 4:
                    break

                if i == 0:
                    bg = darkBlue
                    fg = "white"
                    my_font = ("Montserrat", 14, "bold")

                else:
                    bg = "white"
                    fg = "black"
                    my_font = ("Montserrat", 14)


                current_cell = ctk.CTkLabel(self.rank_contain, text = str(cell), width= 200,
                             height = 40, text_color= fg, font= my_font, 
                             anchor="w", justify= "left", fg_color = bg, padx=20)
                current_cell.grid(row = i, column =j, padx=1, pady = padding)

        #pie chart 
        self.chart_header = ctk.CTkLabel(self.graph, text= "Top Categories", 
                                         font= ("Montserrat", 16), fg_color= darkBlue,
                                         text_color= "white", padx = 10, pady = 15)
        self.chart_header.pack(pady= 10, padx= 20,  fill="x")
        self.pie_chart = chartFrame(self.graph, self.playerId)

        self.titles, self.values = auth.get_top_categories(self.playerId)
        self.pie_details_frame = ctk.CTkFrame(self.graph, fg_color = "white")
        self.pie_details_frame.pack(pady=10, padx=30 , fill="x")

        for title, value in zip(self.titles, self.values):
            self.detail_containier =  ctk.CTkFrame(self.pie_details_frame, fg_color = "white")
            self.detail_containier.pack(fill="x")
            ctk.CTkLabel(self.detail_containier, text = title , font= ("Montserrat", 14)).pack(side = "left")
            ctk.CTkLabel(self.detail_containier, text = str(value) + "%", font= ("Montserrat", 14)).pack(side = "right")
            self.bottom = ctk.CTkFrame(self.pie_details_frame, height=2, fg_color=darkBlue)
            self.bottom.pack(fill="x", pady = (5, 5))
        

        
        


    def prepare_image(self, image, size):
        """converts an image into the customtkinter format"""
        self.height = size
        
        self.ratio = image.width/image.height
        self.newWidth = int(self.height*self.ratio)
        
        self.resized = image.resize((self.newWidth, self.height))
        self.image = ctk.CTkImage(light_image = self.resized, size = (self.newWidth,self.height))
        return self.image
    
    #when the back button is clicked
    def show_main_menu(self):
        #note to self: always close any active matplotlib
        #the line of code below fixed all my errors
        plt.close(self.pie_chart.fig)
        self.controller.show_page(self.controller.main_menu_frame)
        

        self.destroy()