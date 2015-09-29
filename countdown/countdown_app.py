#countdown app script

import time
from stopwatch.stopwatch import *
from stopwatch.app import *

class countdown_app(App):
    
    def __init__(self):
        #self.root = Tk()
        #self.root.title("Countdown")
        
        self.work_time = 0
        self.break_time = 0
        
        
app = countdown_app()

app.root.mainloop()
app.root.destroy()
