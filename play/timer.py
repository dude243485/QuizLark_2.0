import customtkinter as ctk

lightBlue = "#EDF7F7"
darkBlue = "#1581B4"

class Timeout(ctk.CTkFrame):
    def __init__(self, parent, startValue, controller):
        super().__init__(parent)
        self.controller = controller
        self.time_left = startValue
        self.parent = parent

        #to track if the timer is running,
        self.running = False

        #store the timerID to cancel it later
        self.timerID = None

        self.pack(side =  "left", padx=(220, 0))
        self.configure(fg_color = lightBlue, width=70, height=70, border_width = 2,
                       border_color = darkBlue, corner_radius = 35 )
        self.value = ctk.CTkLabel(self,width=40, height=40, text_color = "white", text = startValue, font = ("Montserrat", 18, "bold"), corner_radius = 35, fg_color = darkBlue, bg_color = lightBlue)
        self.value.pack(pady=8, padx=8)
        self.startTimer()
        

    def updateTimer(self):
        """updates the Timeout every second"""
        if (self.time_left > 0) and self.running:
            self.time_left -= 1
            self.value.configure( text= self.time_left)
            self.timerID = self.controller.after(1000, self.updateTimer)

        elif self.time_left == 0:
            self.value.configure( text= self.time_left)
            self.parent.parent.question_box.afterTimeout()

    def startTimer(self):
        """starts the Timeout"""
        #prevent multile start calls
        if not self.running:
            self.running = True
            self.updateTimer()

    def pauseTimer(self):
        """Pause the Timeout"""
        self.running = False
        if self.timerID:
            self.controller.after_cancel(self.timerID)
            #stop any scheduled update

    def resetTimer(self):
        """resets the Timeout"""
        self.running = False
        self.time_left = 20
        self.value.configure( text= self.time_left)

        if self.timerID:
            self.controller.after_cancel(self.timerID)
            self.timerID = None


        