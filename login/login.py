import customtkinter as ctk
from PIL import Image, ImageTk
from login.form import formContainer
import authentication as auth
from CTkMessagebox import CTkMessagebox



lightBlue = "#EDF7F7"
darkBlue = "#1581B4"
class loginFrame(ctk.CTkFrame):
    def __init__(self,parent, controller):
        #controller to switch frame
        super().__init__(parent)
        self.controller = controller
        
        #set frame properties
        self.place(x=0, y=0, relwidth=1, relheight= 1)
        self.configure(fg_color=lightBlue)
        
        #using an image for the back button
        self.back_button =  Image.open("images/back arrow.png")
        self.height = 200
        
        self.ratio = self.back_button.width/self.back_button.height
        self.newWidth = int(self.height*self.ratio)
        
        self.resized = self.back_button.resize((self.newWidth, self.height))
        self.back_button = ctk.CTkImage(light_image = self.resized, size = (50,50))
        
        #create the actual button
        self.go_back_button = ctk.CTkButton(self, image=self.back_button,
                                            command= self.show_welcome, text="",
                                            fg_color=lightBlue, hover_color=lightBlue)
        self.go_back_button.pack(side="top", anchor="nw", pady=15, padx=8)
        
        #for the form
        self.login_form = formContainer(self, self.on_login_click)
        self.playerId = 1
        
    def show_welcome(self):
        #directly acess the login page variable
        #note that controller is refering to the main page
        self.controller.show_page(self.controller.welcome)
        
        #delete existing text
        self.login_form.username_entry.field_entry.delete(0, "end")
        
        #delete existing text
        self.login_form.password_entry.field_entry.delete(0, "end")
        
        #remove the warning text
        self.login_form.password_message.configure(text="")
        
    
        
        
    def on_login_click(self):

        #validate information
        #note that you're directly accessing the login_form 
        #and it is field_entry that is the actual entry field
        self.username  = self.login_form.username_entry.field_entry.get()
        self.password = self.login_form.password_entry.field_entry.get()
        
        if auth.check_user(self.username):
            print("username exists")
            if auth.login_user(self.username, self.password):
                print("login successful")
                #sets the player ID
                self.playerId = auth.get_id(self.username)
                
                print(self.playerId)
                

                self.controller.show_menu(self.playerId)
                
                
            else:
                self.wrong_password()
                print("Incorrect password")
        
        else:
            self.msg = CTkMessagebox(title="Error",
                                     message="User does not exist",
                                     icon = "cancel", 
                                     option_1 = "OK",
                                     fg_color="white",
                                     bg_color = lightBlue,
                                     border_color="white",
                                     border_width=5
                                     )
            print("Username does not exist")
            
    def wrong_password(self):
        
        #show message
        self.login_form.password_message.configure(text="*incorrect password")
        self.msg = CTkMessagebox(title="Error",
                                     message="Incorrect password",
                                     icon = "cancel", 
                                     option_1 = "OK",
                                     fg_color="white",
                                     bg_color = lightBlue,
                                     border_color="white",
                                     border_width=5
                                     )
        
    def correct_password(self):
        self.controller.show_page(self.controller.main_menu_frame)
        self.login_form.password_message.configure(text="*Correct password", text_color="green")
                
                
            
        
        