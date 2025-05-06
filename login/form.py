import customtkinter as ctk
lightBlue = "#EDF7F7"
darkBlue = "#1581B4"


class formEntry(ctk.CTkFrame):
    """This class creates individual input fields"""
    def __init__(self, parent, details):
        super().__init__(parent)
        #put it on the screen
        self.pack(pady=7)
        self.configure(fg_color="white")
        
        self.field_label = ctk.CTkLabel(self, text=details["label_name"],
                                        font= ("Montserrat", 14), text_color="black",
                                        anchor = "w", fg_color="white", bg_color="white")
        self.field_label.pack(fill="x")
        self.field_entry = ctk.CTkEntry(self, width=350, height=50,
                                        text_color="black", fg_color=lightBlue,
                                        placeholder_text= details["placeholder"],
                                        placeholder_text_color="grey", border_width=0,
                                        font= ("Montserrat", 16))
        self.field_entry.pack()
        

class formContainer(ctk.CTkFrame):
    def __init__(self, parent, login_command):
        super().__init__(parent)
        
        self.configure(fg_color="white", width=600, height=500)
        self.place(relx=0.5, rely=0.5,  anchor=ctk.CENTER)
        
        self.contain = ctk.CTkFrame(self, fg_color="white")
        self.contain.pack(pady=30, padx=30)
        
        
        #add widgets
        self.company_name = ctk.CTkLabel(self.contain, text = "QuizLark",font=("Montserrat Extrabold", 36, "bold"),
                                         text_color=darkBlue)
        self.company_name.pack(pady = (0,0))
        self.message = ctk.CTkLabel(self.contain, text = "Login to your account",font=("Montserrat Extrabold", 18),
                                     text_color= "black")
        self.message.pack(pady = (0,0))
        
        #create username entry fields
        self.username_details = {
            "label_name" : "username",
            "placeholder" : "username"
        }
        self.username_entry = formEntry(self.contain, self.username_details)
        
        #create password entry field
        self.password_details = {
            "label_name" : "password",
            "placeholder" : "password123#"
        }
        self.password_entry = formEntry(self.contain, self.password_details)
        self.password_message = ctk.CTkLabel(self.contain, text = "",
                                             font=("Montserrat",12 ),text_color="red",
                                             anchor="w")
        self.password_message.pack(fill="x")
        self.button_text = "Login"
        #create the login button
        self.action_button = ctk.CTkButton(self.contain, width=350,
                       text_color = "white",
                       text= self.button_text,
                       fg_color = darkBlue,
                       font=("Montserrat",16 , "bold"),
                       height= 50,
                       command = login_command
                       )
        self.action_button.pack(pady= (25,25))
        
    
        
        
        
    
        

