import customtkinter as ctk
from PIL import Image
import random
import json
import authentication as auth
from CTkMessagebox import CTkMessagebox
from create_account.accountForm import formContainer

lightBlue = "#EDF7F7"
darkBlue = "#1581B4"
greetings_list = [
    "Welcome to the best quizzing app out there...",
    "Feeling doubtful, test your knowledge on our app...",
    "it's great to have you here, Let's get started...",
    "Good to see you, lets make today productive..."
]

class createAccountFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        #set frame properties
        self.place(x=0, y=0, relwidth=1, relheight= 1)
        self.configure(fg_color=lightBlue)
        
        
        #create the left container
        self.greeting_container = ctk.CTkFrame(self, fg_color=lightBlue)
        self.greeting_container.pack(fill="both", side="left",  expand=True)
        
        #using an image for the back button
        self.back_button =  Image.open("images/back arrow.png")
        self.height = 200
        
        self.ratio = self.back_button.width/self.back_button.height
        self.newWidth = int(self.height*self.ratio)
        
        self.resized = self.back_button.resize((self.newWidth, self.height))
        self.back_button = ctk.CTkImage(light_image = self.resized, size = (50,50))
        
        #create the actual button
        self.go_back_button = ctk.CTkButton(self.greeting_container, image=self.back_button,
                                            command= self.show_welcome, text="",
                                            fg_color=lightBlue, hover_color=lightBlue)
        self.go_back_button.pack(anchor="nw", pady=15, padx=8)
        
        
        
        #right container
        self.account_container = ctk.CTkFrame(self, fg_color=lightBlue)
        self.account_container.pack(fill="both", side="left",  expand=True, padx=60)
        
        self.g_container = ctk.CTkFrame(self.greeting_container, fg_color=lightBlue)
        self.g_container.pack(pady=40, padx=0)
        #add widgets to greeting container
        self.company_name = ctk.CTkLabel(self.g_container, text = "QuizLark",
                                         font=("Montserrat Extrabold", 56, "bold"),
                                         text_color=darkBlue, justify="left", anchor="w")
        self.company_name.pack(pady = (0,0), fill="x")
        self.message = ctk.CTkLabel(self.g_container, text = random.choice(greetings_list),
                                    font=("Montserrat", 20, "bold"),
                                    text_color= "black", wraplength=380,
                                    justify="left", anchor="w")
        self.message.pack(pady = (0,0), fill="x")
        
        
        self.account_form  = formContainer(self.account_container, self.on_create_account_click)
        
        
     
    def on_create_account_click(self):      
        self.full_name = self.account_form.fullname_entry.field_entry.get()
        self.username = self.account_form.username_entry.field_entry.get()
        self.password = self.account_form.password_entry.field_entry.get()
        self.id = auth.get_next_id()
        
        if auth.check_user(self.username):
            #error message if username exists
            self.msg = CTkMessagebox(title="Error",
                                     message="Username already exists, pick another one",
                                     icon = "cancel", 
                                     option_1 = "OK",
                                     fg_color="white",
                                     bg_color = lightBlue,
                                     border_color="white",
                                     border_width=5
                                     )
            
        else:
            #if password is strong enough
            if auth.checkPasswordStrength(self.password):
                current_user = {
                    "name" : self.full_name,
                    "username" : self.username,
                    "password" :self.password,
                    "id": self.id + 1,
                    "xp" : 0,
                    "money" : 2000,
                    "save me" : 10,
                    "instant" : 10,
                    "eliminate" : 10,
                    "hint" : 10,
                    "stats" : {
                        "questions attempted": 0,
                        "correct": 0,
                        "wrong": 0,
                        "games played": 0,
                        "games won": 0
                    },
                    "categories progress": {
                    "general": 0,
                    "sports": 0,
                    "movie": 0,
                    "arts": 0,
                    "tech": 0,
                    "history": 0,
                    "medicine": 0,
                    "science": 0,
                    "bible": 0,
                    "politics": 0
        }
                    
                }
                #save the user data
                auth.save_user(current_user)
                self.account_form.password_message.configure(text="*strong password",
                                                             text_color = "green")
                self.controller.show_menu(current_user["id"])
                
            else:
                #show error message
                self.msg = CTkMessagebox(title="Error",
                                     message="Password not strong enough",
                                     icon = "cancel", 
                                     option_1 = "OK",
                                     fg_color="white",
                                     bg_color = lightBlue,
                                     border_color="white",
                                     border_width=5
                                     )
                self.account_form.password_message.configure(text="*must contain uppercase, digit and special characters",
                                                             text_color = "red")
            
                
        
        
        
    #go back to welcome page
    def show_welcome(self):
        #access the welcome page from the main.py file
        self.controller.show_page(self.controller.welcome)
        
        #clear input fields
        self.account_form.fullname_entry.field_entry.delete(0, "end")
        self.account_form.username_entry.field_entry.delete(0, "end")
        self.account_form.password_entry.field_entry.delete(0, "end")
        
        #clear all messages
        self.account_form.password_message.configure(text="")
        
        
    
        