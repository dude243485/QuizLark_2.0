import customtkinter as ctk
from welcome.welcomeButton import welcomeButtons
from login.login import loginFrame

lightBlue = "#EDF7F7"
darkBlue = "#1581B4"


#welcome frame
class welcomeFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        #for the page switching
        self.controller = controller
        #make the colors available
        global lightBlue
        global darkBlue
        
        #set frame properties
        self.place(x=0, y=0, relwidth=1, relheight= 1)
        self.configure(fg_color=lightBlue)
        
        #add widgets
        
        self.greeting = ctk.CTkLabel(self, text = "Welcome",font=("Montserrat Extrabold", 30),
                                     text_color= darkBlue)
        self.greeting.pack(pady = (80,0))
        
        self.company_name = ctk.CTkLabel(self, text = "QuizLark",font=("Montserrat Extrabold", 60, "bold"),
                                         text_color="black")
        self.company_name.pack(pady = (0,40))
        
        self.buttons_container = ctk.CTkFrame(self, fg_color=lightBlue)
        self.buttons_container.place(relx=0.5, rely=0.5,  anchor= ctk.CENTER)
        
        #create buttons
        #self.guest = welcomeButtons(self.buttons_container, "Play As Guest")
        self.createAccount = welcomeButtons(self.buttons_container, "Create Account", self.show_create_account)
        self.login = welcomeButtons(self.buttons_container, "Login", self.show_login)
        self.play_as_guest = welcomeButtons(self.buttons_container, "Play As Guest", self.show_main_menu)
        
    def show_login(self):
        #directly acess the login page variable
        self.controller.show_page(self.controller.login_frame)
        
    def show_create_account(self):
        self.controller.show_page(self.controller.create_account_frame)

    def show_main_menu(self):
        self.controller.show_menu(1)

        
      
       
    