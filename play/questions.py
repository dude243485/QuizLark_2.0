import customtkinter as ctk
from openpyxl import load_workbook
import authentication as auth
from play.optionButton import OptionButton
from PIL import Image

lightBlue = "#EDF7F7"
darkBlue = "#1581B4"
hoverBlue = "#B9E1F5"

class QuestionBox(ctk.CTkFrame):
    def __init__(self, parent, controller, playerId, category, level = 1):
        super().__init__(parent)
        self.pack(pady = (50, 0))
        self.configure(fg_color = lightBlue)
        self.parent = parent
        self.controller = controller
        self.playerId = playerId
        self.category = category
        self.level = level
        self.saveMe_quantity = auth.get_save_me(self.playerId)
        self.level_money = auth.get_money(self.playerId)
        self.questions_attempted = auth.get_stat(self.playerId, "questions attempted")
        self.correct_answers = auth.get_stat(self.playerId, "correct")
        self.wrong_answers = auth.get_stat(self.playerId, "wrong")
        
        

        self.header = ctk.CTkLabel(self, text = self.category, font = ("Montserrat Extrabold", 32),
                                   justify="center", fg_color = lightBlue)
        self.header.pack()

        self.questionList = auth.get_questions(self.category, self.level)
        self.question, self.option_list, self.answer, self.hint =auth.get_question(self.questionList)

        self.hint_label = ctk.CTkLabel(self, text="", text_color= darkBlue, font= ("Montserrat", 16))
        self.hint_label.pack(pady = (10, 10))

        self.question_contain = ctk.CTkFrame(self, width= 400, height=150, fg_color="white")
        self.question_contain.pack(pady = (0, 15))

        self.question_counter = 1
        self.question_text = ctk.CTkLabel(self.question_contain, text= self.question, font = ("Montserrat", 20, "bold"))
        self.question_text.pack(padx=200, pady=40)

        self.option_contain = ctk.CTkFrame(self, fg_color = lightBlue)
        self.option_contain.pack()

        self.optionA = OptionButton(self.option_contain, self, self.option_list[0], 0, 0)
        self.optionB = OptionButton(self.option_contain,self, self.option_list[1], 0, 1)
        self.optionC = OptionButton(self.option_contain,self, self.option_list[2], 1, 0)
        self.optionD = OptionButton(self.option_contain,self, self.option_list[3], 1, 1)
    
    def questionAttempted(self, choice, clicked_button):
        self.questions_attempted += 1
        if choice == self.answer:
            clicked_button.configure(fg_color = "green", hover_color = "green", text_color = "white")
            self.level_money += 20
            self.correct_answers += 1
            self.parent.status.money.imageText.configure(text = self.level_money)
            if self.question_counter >= 15:
                self.currentXp = auth.get_xp(self.playerId)
                auth.set_powerUp(self.playerId, "xp", self.currentXp + 120)
                self.completeLevel()
                
            else:
                self.controller.after(1000, self.updateQuestions)
            
        else:
            self.wrong_answers += 1
            if self.parent.status.lives > 1:
                clicked_button.configure(fg_color = "red", hover_color = "red",  text_color = "white")
                self.controller.after(1000, self.updateQuestions)
            self.failedQuestion()
    
    def afterTimeout(self):
        self.wrong_answers += 1
        if self.parent.status.lives > 1:
            self.controller.after(1000, self.updateQuestions)
        self.failedQuestion()
        
        
            

    def updateQuestions(self):
            
        self.question_counter += 1
        self.question, self.option_list, self.answer, self.hint = auth.get_question(self.questionList)
        self.question_text.configure(text= self.question)
        self.optionA.configure(text = self.option_list[0], fg_color="white", hover_color = hoverBlue, text_color = "black")
        self.optionB.configure(text = self.option_list[1], fg_color="white", hover_color = hoverBlue, text_color = "black")
        self.optionC.configure(text = self.option_list[2], fg_color="white", hover_color = hoverBlue, text_color = "black")
        self.optionD.configure(text = self.option_list[3], fg_color="white", hover_color = hoverBlue, text_color = "black")
        self.hint_label.configure(text= "")
        
        self.optionA.grid(row = 0, column = 0, ipady = 5, ipadx = 10, padx = 10, pady=10)
        self.optionB.grid(row = 0, column = 1, ipady = 5, ipadx = 10, padx = 10, pady=10)
        self.optionC.grid(row = 1, column = 0, ipady = 5, ipadx = 10, padx = 10, pady=10)
        self.optionD.grid(row = 1, column = 1, ipady = 5, ipadx = 10, padx = 10, pady=10)

        #restart timer
        self.parent.status.timer.resetTimer()
        self.parent.status.timer.startTimer()

        

    def failedQuestion(self):
        if self.parent.status.lives <= 1:
            self.gameover()
        self.parent.status.lives = self.parent.status.lives - 1
        self.parent.status.life_meter.configure(image = self.prepare_image(Image.open(self.parent.status.imageUrlDict["life"][self.parent.status.lives]), 20))
            
 
    def gameover(self):
        #open main menu
        self.parent.status.timer.pauseTimer()
        self.controller.show_gameover_window(self, self.parent, self.playerId)
        
    def completeLevel(self):
        auth.set_stat(self.playerId, "games won", auth.get_stat(self.playerId, "games won")+ 1)
        auth.set_stat(self.playerId, "games played", auth.get_stat(self.playerId, "games played") + 1)
        
        #open level complete
        self.parent.status.timer.pauseTimer()
        self.controller.show_completeLevel_window(self, self.parent, self.playerId)
        
        
    def prepare_image(self, image, size):
        """converts an image into the customtkinter format"""
        self.height = size
        
        self.ratio = image.width/image.height
        self.newWidth = int(self.height*self.ratio)
        
        self.resized = image.resize((self.newWidth, self.height))
        self.image = ctk.CTkImage(light_image = self.resized, size = (self.newWidth,self.height))
        return self.image

