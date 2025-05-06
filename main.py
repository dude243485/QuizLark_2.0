import customtkinter as ctk
import tkinter as tk
from welcome.welcome import welcomeFrame
from login.login import loginFrame
from create_account.createAccount import createAccountFrame
from main_menu.mainmenu import mainMenuFrame
from main_menu.storeFrame import storeFrame
from stat_page.stats import statsFrame
from categories.category_page import CategoryFrame
from play.play_page import PlayFrame
from play.pause_window import PauseWindow
import matplotlib.pyplot as plt
from play.gameover import GameOverWindow
from play.levelComplete import CompleteLevelWindow



class QuizApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        #setting root window properties
        self.title("My Tkinter App")

        #get and set the screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}+0+0")
        
        
        #set screen properties
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0, weight=1)

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        
        
        #creating the welcome and login frame
        self.welcome = welcomeFrame(self, self)
        self.login_frame = loginFrame(self, self)
        self.create_account_frame = createAccountFrame(self,self)
        
        
        #displaying the welcome page first
        self.show_page(self.welcome)
        
    def show_page(self, frame_name):
        """raises the selected frame to the front"""
        frame_name.tkraise()

    def show_menu(self, playerId):
        self.main_menu_frame = mainMenuFrame(self,self, playerId)
        self.main_menu_frame.tkraise()

    def show_store_frame(self, playerId):
        self.store_frame = storeFrame(self,self, playerId)
        self.store_frame.tkraise()

    def show_stats_frame(self, playerId):
        self.stats_frame = statsFrame(self, self, playerId)
        self.stats_frame.tkraise()

    def show_categories_frame(self, playerId):
        self.category_frame = CategoryFrame(self, playerId, self)
        self.category_frame.tkraise()

    def show_play_frame(self, playerId, category):
        self.play_frame = PlayFrame(self, self, playerId, category)
        self.play_frame.tkraise()

    def show_pause_window(self, playerId, timer, parent):
        self.pause_window = PauseWindow(self, playerId, timer, parent)
        
    def show_gameover_window(self, parent, playParent, playerId):
        self.gameover_window = GameOverWindow(self, parent, playParent, playerId)
        
    def show_completeLevel_window(self, parent, playParent, playerId):
        self.completeLevel_window = CompleteLevelWindow(self, parent, playParent, playerId)
        


    def on_close(self):
        for task in self.tk.eval("after info").split():
            self.after_cancel(task)
        self.destroy()



if __name__ == "__main__": 
    app = QuizApp()
    #to close all running task
    
    # def on_closing():
    #     if (statsFrame) :
    #         #close the pie chart drawing if the statsFrame has been
    #         plt.close(app.stats_frame.pie_chart.fig)

    #     for task in app.tk.eval("after info").split():
    #         app.after_cancel(task)
    #     app.destroy()
        
    # app.protocol("WM_DELETE_WINDOW", on_closing)
    app.mainloop()
