import customtkinter as ctk
from PIL import Image
import random
import authentication as auth

lightBlue = "#EDF7F7"
darkBlue = "#1581B4"

class PauseWindow(ctk.CTkToplevel):
    def __init__(self, controller, playerId, timer, play_parent):
        super().__init__()
        self.playerId = playerId
        self.controller = controller
        self.parent = play_parent
        self.timer = timer
        timer.pauseTimer()

        #set window properties
        self.resizable(False, False)
        self.transient(controller)
        self.grab_set()
        self.title("Pause")
        
        #disable close button
        self.protocol("WM_DELETE_WINDOW", self.disable_close)

        self.screenWidth =self.winfo_screenwidth()
        self.screenHeight = self.winfo_screenheight()

        #centering the window
        self.x = (self.screenWidth//2)-(300//2)
        self.y = (self.screenHeight//2)-(220//2)
        self.geometry(f"300x220+{self.x}+{self.y}")
        self.configure(fg_color=lightBlue)

        self.resume_button = ctk.CTkButton(self, text="RESUME", fg_color = darkBlue, text_color= "white",
                                           font = ("Montserrat", 16, "bold"), width=250, command = lambda : self.resume_command(timer))
        self.resume_button.pack(pady = (50, 8), ipady = 20)

        self.quit_button = ctk.CTkButton(self, text="QUIT", fg_color = darkBlue, text_color= "white",
                                           font = ("Montserrat", 16, "bold"), width =250, command = self.quit_command)
        self.quit_button.pack(pady = 8, ipady = 20)

    def resume_command(self, timer):
        timer.startTimer()
        self.destroy()

    def quit_command(self):
        self.controller.show_menu(self.playerId)

        self.destroy()
        self.parent.destroy()
        
    def disable_close(self):
        pass
        
        