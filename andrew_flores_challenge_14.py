import tkinter # the tk module

class Star: # class def
    def __init__(self): 
        self.main_window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.main_window, width = 450, height = 450) #sets how large the window will be
        self.canvas.create_polygon(50, 150, 180, 150, 225, 35, 270, 150, 400, 150, 300, 250, 335, 380, 225, 300, 115, 380, 150, 250, 50, 150,fill="white", outline="black") #creates an eyesore of a star with a white filling and black outline  
        self.canvas.create_text(225, 225, text="Andrew Flores") #creates the text roughly centered
        self.canvas.pack() #calls the pack method
        tkinter.mainloop() #puts it all into the main loop
        
if __name__ == '__main__': #makes an instance of the Star class
    star = Star()