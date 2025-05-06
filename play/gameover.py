import customtkinter as ctk
from PIL import Image
import authentication as auth


lightBlue = "#EDF7F7"
darkBlue = "#1581B4"

class GameOverWindow(ctk.CTkToplevel):
    def __init__(self, controller, parent, playParent, playerId):
        super().__init__()
        self.controller = controller
        self.parent = parent
        self.playParent = playParent
        self.playerId = playerId
    
        
        #set window properties
        self.resizable(False, False)
        self.transient(controller)
        self.grab_set()
        self.title("Game over")
        
        #disable close button
        self.protocol("WM_DELETE_WINDOW", self.disable_close)

        self.screenWidth =self.winfo_screenwidth()
        self.screenHeight = self.winfo_screenheight()

        #centering the window
        self.x = (self.screenWidth//2)-(350//2)
        self.y = (self.screenHeight//2)-(350//2)
        self.geometry(f"350x350+{self.x}+{self.y}")
        self.configure(fg_color=lightBlue)
        
        
        self.warning_label = ctk.CTkLabel(self, text= "You Lose", text_color = darkBlue,
                                           font = ("Montserrat", 24, "bold"))
        self.warning_label.pack(pady = (10, 15))
        
        self.image_label = ctk.CTkLabel(self, text = None, image = self.prepare_image(Image.open("images/game over.png"), 150))
        self.image_label.pack()
        
        self.saveMe_label = ctk.CTkLabel(self, text= "Save Me " + "x" + str(self.parent.saveMe_quantity), text_color = darkBlue,
                                           font = ("Montserrat", 16, "bold"))
        self.saveMe_label.pack(pady = (15, 15))
        self.button_container = ctk.CTkFrame(self, fg_color = lightBlue)
        self.button_container.pack(expand = True, ipady = 15, ipadx = 15 )
        
        
        
        self.resume_button = ctk.CTkButton(self.button_container, text="SAVE ME", fg_color = darkBlue, text_color= "white",
                                           font = ("Montserrat", 16, "bold"), width=150, command = self.saveMe_command)
        self.resume_button.pack(pady = 8, ipady = 20, side = "left")

        self.quit_button = ctk.CTkButton(self.button_container, text="GIVE UP", fg_color = darkBlue, text_color= "white",
                                           font = ("Montserrat", 16, "bold"), width =150, command = self.giveUp_command)
        self.quit_button.pack(pady = 8, ipady = 20, side ="right")
        
        
        
    def prepare_image(self, image, size):
        """converts an image into the customtkinter format"""
        self.height = size
        
        self.ratio = image.width/image.height
        self.newWidth = int(self.height*self.ratio)
        
        self.resized = image.resize((self.newWidth, self.height))
        self.image = ctk.CTkImage(light_image = self.resized, size = (self.newWidth,self.height))
        return self.image
    
    def giveUp_command(self):
        #save the current number of save me and power-ups
        auth.set_powerUp(self.playerId, "save me", self.parent.saveMe_quantity)
        auth.set_powerUp(self.playerId, "eliminate", self.parent.parent.status.eliminate_value)
        auth.set_powerUp(self.playerId, "instant", self.parent.parent.status.instant_value)
        auth.set_powerUp(self.playerId, "hint", self.parent.parent.status.hint_value)
        auth.set_powerUp(self.playerId, "money", self.parent.parent.question_box.level_money)
        auth.set_stat(self.playerId, "questions attempted", self.parent.questions_attempted)
        auth.set_stat(self.playerId, "correct", self.parent.correct_answers)
        auth.set_stat(self.playerId, "wrong", self.parent.wrong_answers)
        auth.set_stat(self.playerId, "games played", auth.get_stat(self.playerId, "games played") + 1)
        
        self.controller.show_menu(self.playerId)
        
        self.destroy()
        self.parent.destroy()
        self.playParent.destroy()
        
    
    def saveMe_command(self):
        #update the number of used save me's
        self.parent.saveMe_quantity = self.parent.saveMe_quantity - 1
        self.saveMe_label.configure(text = str(self.parent.saveMe_quantity))
        
        #reset the number of lives
        self.playParent.status.lives = 2
        self.playParent.status.change_life(2)
        
        #restart the timer
        self.playParent.status.timer.resetTimer()
        self.playParent.status.timer.startTimer()
        
        #close window
        self.destroy()
        
    def disable_close(self):
        pass
    
    