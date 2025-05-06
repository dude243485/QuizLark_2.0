import customtkinter as ctk
import authentication as auth
from PIL import Image
from main_menu.statusIcon import statusIcon
from play.timer import Timeout
from play.powerUpButton import PowerUpButton
import random

lightBlue = "#EDF7F7"
darkBlue = "#1581B4"
hoverBlue = "#B9E1F5"

class StatusBar(ctk.CTkFrame):
    def __init__(self, parent, playerId, lives, controller):
        super().__init__(parent)
        #self.configure(fg_color = lightBlue)
        self.configure(fg_color = lightBlue)
        self.pack(fill = "x", padx =15 , pady=15)
        self.lives = lives
        self.playerId = playerId
        self.controller = controller
        self.parent = parent
        self.hint_value = auth.get_hint(self.playerId)
        self.instant_value = auth.get_instant(self.playerId)
        self.eliminate_value = auth.get_eliminate(self.playerId)

        self.imageUrlDict = {
            "saveMe" : "images/save me.png",
            "eliminate" : "images/eliminate.png",
            "instant" : "images/instant.png",
            "hint" : "images/hint.png",
            "pause" : "images/pause.png",
            "money" : "images/money.png",
            "full life" : "images/full life.png",
            "half life" : "images/half life.png",
            "empty life" : "images/empty life.png",
            "life" : [ "images/empty life.png", "images/half life.png","images/full life.png"]
        }

        self.life_meter = ctk.CTkLabel(self, fg_color = lightBlue, text= "",
                                       image = self.prepare_image(Image.open(self.imageUrlDict["life"][2]), 20))
        self.life_meter.pack(side = "left", padx=(0, 15))

        self.money = statusIcon(self, Image.open(self.imageUrlDict["money"]), auth.get_money(self.playerId))
        self.timer = Timeout(self, 20, controller)

       
        self.pause_button_container = ctk.CTkFrame(self, fg_color= lightBlue, corner_radius = 35 )
        self.pause_button_container.pack(side ="right", padx=40 )

        self.pause_button = ctk.CTkButton(self.pause_button_container, fg_color=lightBlue, text="", width = 50, height = 50, hover_color= hoverBlue,
                                          image = self.prepare_image(Image.open(self.imageUrlDict["pause"]), 45) , command = self.pause_command)
        
        self.pause_button.pack(side ="left", padx=(20,0), pady=0)

        self.eliminate = PowerUpButton(self, 
                                  self.controller, 
                                  self.prepare_image(Image.open(self.imageUrlDict["eliminate"]), 40),
                                  self.eliminate_value,
                                  self.on_eliminate)
        
        self.instant = PowerUpButton(self, 
                                  self.controller, 
                                  self.prepare_image(Image.open(self.imageUrlDict["instant"]), 40),
                                  self.instant_value,
                                  self.on_instant)
    
        self.hint = PowerUpButton(self, 
                                  self.controller, 
                                  self.prepare_image(Image.open(self.imageUrlDict["hint"]),40),
                                  self.hint_value,
                                  self.on_hint)


    def prepare_image(self, image, size):
        """converts an image into the customtkinter format"""
        self.height = size
        
        self.ratio = image.width/image.height
        self.newWidth = int(self.height*self.ratio)
        
        self.resized = image.resize((self.newWidth, self.height))
        self.image = ctk.CTkImage(light_image = self.resized, size = (self.newWidth,self.height))
        return self.image
    
    def pause_command(self):
         self.controller.show_pause_window(self.playerId, self.timer, self.parent )
         
    def change_life(self, life):
        self.life_meter.configure(image = self.prepare_image(Image.open(self.imageUrlDict["life"][life]), 20))
        
    def on_eliminate(self):
        self.option_list = []
        def optionCheck(option):
            #i don't know what this line does, but since it is not breaking the
            #code just leave it be
            option
            if option.cget("text") != self.parent.question_box.answer:
                self.option_list.append(option)
                
        optionCheck(self.parent.question_box.optionA)
        optionCheck(self.parent.question_box.optionB)
        optionCheck(self.parent.question_box.optionC)
        optionCheck(self.parent.question_box.optionD)
        
        self.option_list.pop(random.randint(0,2))
        for option in self.option_list:
            option.grid_forget()
            
        self.eliminate_value -= 1
        self.eliminate.text_label.configure(text = str(self.eliminate_value))
        
            
    def on_instant(self):
        if self.parent.question_box.optionA.cget("text") == self.parent.question_box.answer:
            self.parent.question_box.optionA.configure(fg_color = darkBlue, text_color = "white")
            
        elif self.parent.question_box.optionB.cget("text") == self.parent.question_box.answer:
            self.parent.question_box.optionB.configure(fg_color = darkBlue, text_color = "white")
        
        elif self.parent.question_box.optionC.cget("text") == self.parent.question_box.answer:
            self.parent.question_box.optionB.configure(fg_color = darkBlue, text_color = "white")
        
        elif self.parent.question_box.optionD.cget("text") == self.parent.question_box.answer:
            self.parent.question_box.optionD.configure(fg_color = darkBlue, text_color = "white")    
            
        self.instant_value -= 1
        self.instant.text_label.configure(text = str(self.instant_value))
        
    def on_hint(self):
        self.parent.question_box.hint_label.configure(text = self.parent.question_box.hint)
        self.hint_value -= 1
        self.hint.text_label.configure(text = str(self.hint_value))
        