import customtkinter as ctk
from play.statusBar import StatusBar
from play.questions import QuestionBox
import authentication as auth

lightBlue = "#EDF7F7"
darkBlue = "#1581B4"

class PlayFrame(ctk.CTkFrame):
    def __init__(self, controller, parent, playerId, category):
        super().__init__(parent)
        self.configure(fg_color = lightBlue)
        self.place(x=0, y=0, relwidth=1, relheight= 1)
        self.playerId = playerId
        self.category = category
        self.controller = controller
        self.current_level = auth.get_progress(self.playerId, self.category )
        
        
        self.status = StatusBar(self, self.playerId, 2, self.controller )
        #ctk.CTkLabel(self, text="The " + category + " play page works", font=("Montserrat", 36)).pack()
        
        self.question_box = QuestionBox(self, self.controller, self.playerId, category, self.current_level)
    
    def createQuestions(self, category, level):
        self.question_box = QuestionBox(self, self.controller, self.playerId, category, level)
        self.status.timer.resetTimer()
        self.status.timer.startTimer()
        
    def check_completed(self):
        if auth.get_actual_progress(self.playerId, self.category) >= 100:
            print("level Completed")
        
        
        
        