import customtkinter as ctk
from PIL import Image
import authentication as auth
from play.questions import QuestionBox


lightBlue = "#EDF7F7"
darkBlue = "#1581B4"

class CompleteLevelWindow(ctk.CTkToplevel):
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
        self.title("Level Complete")
        
        #disable close button
        self.protocol("WM_DELETE_WINDOW", self.disable_close)

        self.screenWidth =self.winfo_screenwidth()
        self.screenHeight = self.winfo_screenheight()

        #centering the window
        self.x = (self.screenWidth//2)-(350//2)
        self.y = (self.screenHeight//2)-(350//2)
        self.geometry(f"350x350+{self.x}+{self.y}")
        self.configure(fg_color=lightBlue)
        
        
        self.warning_label = ctk.CTkLabel(self, text= "LEVEL COMPLETE", text_color = darkBlue,
                                           font = ("Montserrat", 24, "bold"))
        self.warning_label.pack(pady = (10, 15))
        
        self.image_label = ctk.CTkLabel(self, text = None, image = self.prepare_image(Image.open("images/Trophy.png"), 160))
        self.image_label.pack()
        
        self.level_label = ctk.CTkLabel(self, text= "level " + str(self.parent.level) + "/" + str(auth.get_levels(self.parent.category)), text_color = darkBlue,
                                           font = ("Montserrat", 16, "bold"))
        self.level_label.pack(pady = (15, 15))
        self.button_container = ctk.CTkFrame(self, fg_color = lightBlue)
        self.button_container.pack(expand = True, ipady = 15, ipadx = 15 )
        
        
        
        self.menu_button = ctk.CTkButton(self.button_container, text="MENU", fg_color = darkBlue, text_color= "white",
                                           font = ("Montserrat", 16, "bold"), width=100, command = self.menu_command)
        self.menu_button.pack(pady = 8, padx = (13, 10), ipady = 20, side = "left")

        self.restart = ctk.CTkButton(self.button_container, text="RESTART", fg_color = darkBlue, text_color= "white",
                                           font = ("Montserrat", 16, "bold"), width =100, command = self.restart_command)
        self.restart.pack(pady = 8,  padx = (0, 10), ipady = 20, side ="left")
        
        self.next = ctk.CTkButton(self.button_container, text="NEXT", fg_color = darkBlue, text_color= "white",
                                           font = ("Montserrat", 16, "bold"), width =100, command = self.next_command)
        self.next.pack(pady = 8, padx = (0, 10), ipady = 20, side ="left")
        
        
        
    def prepare_image(self, image, size):
        """converts an image into the customtkinter format"""
        self.height = size
        
        self.ratio = image.width/image.height
        self.newWidth = int(self.height*self.ratio)
        
        self.resized = image.resize((self.newWidth, self.height))
        self.image = ctk.CTkImage(light_image = self.resized, size = (self.newWidth,self.height))
        return self.image
    
    def menu_command(self):
        #save the current number of save me and power-ups
        auth.set_powerUp(self.playerId, "save me", self.parent.saveMe_quantity)
        auth.set_powerUp(self.playerId, "eliminate", self.parent.parent.status.eliminate_value)
        auth.set_powerUp(self.playerId, "instant", self.parent.parent.status.instant_value)
        auth.set_powerUp(self.playerId, "hint", self.parent.parent.status.hint_value)
        auth.set_powerUp(self.playerId, "money", self.parent.parent.question_box.level_money)
        auth.set_progress(self.playerId, self.parent.parent.category, self.parent.parent.question_box.level )
        auth.set_stat(self.playerId, "questions attempted", self.parent.questions_attempted)
        auth.set_stat(self.playerId, "correct", self.parent.correct_answers)
        auth.set_stat(self.playerId, "wrong", self.parent.wrong_answers)
        
        self.controller.show_menu(self.playerId)
        
        self.destroy()
        self.parent.destroy()
        self.playParent.destroy()
        
    
    def restart_command(self):
        #save the current number of save me and power-ups
        auth.set_powerUp(self.playerId, "save me", self.parent.saveMe_quantity)
        auth.set_powerUp(self.playerId, "eliminate", self.parent.parent.status.eliminate_value)
        auth.set_powerUp(self.playerId, "instant", self.parent.parent.status.instant_value)
        auth.set_powerUp(self.playerId, "hint", self.parent.parent.status.hint_value)
        auth.set_powerUp(self.playerId, "money", self.parent.parent.question_box.level_money)
        
        self.parent.parent.question_box.destroy()
        self.parent.parent.createQuestions(self.parent.category, self.parent.level)
        #close window
        self.destroy()
        
    def next_command(self):
        
        
        #save the current number of save me and power-ups
        auth.set_powerUp(self.playerId, "save me", self.parent.saveMe_quantity)
        auth.set_powerUp(self.playerId, "eliminate", self.parent.parent.status.eliminate_value)
        auth.set_powerUp(self.playerId, "instant", self.parent.parent.status.instant_value)
        auth.set_powerUp(self.playerId, "hint", self.parent.parent.status.hint_value)
        auth.set_powerUp(self.playerId, "money", self.parent.parent.question_box.level_money)
        auth.set_progress(self.playerId, self.parent.parent.category, self.parent.parent.question_box.level )
        auth.set_stat(self.playerId, "questions attempted", self.parent.questions_attempted)
        auth.set_stat(self.playerId, "correct", self.parent.correct_answers)
        auth.set_stat(self.playerId, "wrong", self.parent.wrong_answers)
        
        self.parent.parent.question_box.destroy()
        if auth.get_actual_progress(self.playerId,self.parent.category) >= 100:
            self.controller.show_menu(self.playerId)
            self.destroy()
            self.parent.destroy()
            self.playParent.destroy()
            
        else:
            self.parent.parent.createQuestions(self.parent.category, self.parent.level + 1)
            #close window
            self.destroy()
        
    def disable_close(self):
        pass
    
    