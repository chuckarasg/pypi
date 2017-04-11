from Tkinter import *
import datetime
import time
from PIL import ImageTk, Image

def NextIndex(index, length):
    index += 1
    if (index >= length):
        index = 0
    return index

class slideshow:
    def __init__(self, window, images, timer = 0, autoFlip = False):
        self.window = window
        self.images = images
        self.timer = timer
        self.lastFlip = datetime.datetime.now()
        self.currentImage = 0
        self.autoFlip = autoFlip
        img = ImageTk.PhotoImage(Image.open(self.images[self.currentImage]))
        self.panel = Label(window, image = img, anchor = S)
        self.panel.pack(fill = "both", expand = "yes")
    
    def tick(self):
        if (self.autoFlip):
            currentTime = datetime.datetime.now()
            if ((currentTime - self.lastFlip).total_seconds() >= self.timer):
                self.NextImage()
        
    def NextImage(self):
        self.currentImage = NextIndex(self.currentImage, len(self.images))
        img = ImageTk.PhotoImage(Image.open(self.images[self.currentImage]))
        self.panel.configure(image = img)
        self.panel.image = img
        self.panel.pack(side = "bottom", fill = "both", expand = "yes")
        self.lastFlip = datetime.datetime.now()

def main():
    #create a window
    window = Tk()
    w, h = window.winfo_screenwidth(), window.winfo_screenheight()
    #window.overrideredirect(1)
    window.geometry("%dx%d+0+0" % (w, h))
    #place first image
    topImages = ["Images\weekdaylunch.jpg", "Images\weekdaydinner.jpg", "Images\weekendlunch.jpg", "Images\weekenddinner.jpg"]
    currentTopImage = 0
    
    img = ImageTk.PhotoImage(Image.open(topImages[currentTopImage]))
    topFrame = Frame(window)
    topFrame.pack()
    topPanel = Label(topFrame, image = img, anchor = N)
    topPanel.pack(fill = "both", expand = "yes")
    
    #place video
    videos = ["Videos\Chuck_PizzaFries_30.mp4", "Videos\Chuck_SingleDad_30.mp4", "Videos\Chuck_Jello_30.mp4"]
    middleImages = ["Images\FreeDrinks.jpg", "Images\IOTM_Jello.jpg"]
    currentVideo = 0
    currentMiddleImage = 0
    isShowingVideo = False
    videoTimer = time.time()
    #place second image
    bottomImages = ["Images\DailyMenu.jpg", "Images\MondayDayMenu.jpg", "Images\TuesdayDayMenu.jpg", "Images\WednesdayDayMenu.jpg", "Images\ThursdayDayMenu.jpg", "Images\FridayDayMenu.jpg", "Images\SaturdayDayMenu.jpg", "Images\SundayDayMenu.jpg"]
    currentBottomImage = 0
    bottomTimer = time.time()
    img = ImageTk.PhotoImage(Image.open(bottomImages[currentBottomImage]))
    bottomFrame = Frame(window)
    bottomFrame.pack()
    bottomPanel = Label(bottomFrame, image = img, anchor = S)
    bottomPanel.pack(fill = "both", expand = "yes")
    
    #main loop
    while(True):
        currentTime = datetime.datetime.now()
        
        # handle top image
        if (currentTime.weekday < 5):
            #mon-fri
            if (currentTime.hour < 16):
                currentTopImage = 0
            else:
                currentTopImage = 1
        elif (currentTime.weekday == 5 and currentTime.hour < 16):
            #sat day
            currentTopImage = 2
        else:
            #sun
            currentTopImage = 3
            #set top image to topImages[currentTopImage]
            img = ImageTk.PhotoImage(Image.open(topImages[currentTopImage]))
            #topPanel = Label(window, image = img)
            topPanel.configure(image = img)
            topPanel.image = img
            topPanel.pack(side = "bottom", fill = "both", expand = "yes")
        
        # handle video
        # if (time.mktime(currentTime.timetuple()) - videoTimer > 30):
            # if (isShowingVideo):
                # # change to image
                # currentVideo = NextIndex(currentVideo, len(videos))
            # else:
                # # change to video
                # currentMiddleImage = NextIndex(currentMiddleImage, len(middleImages))
            # isShowing = !isShowing
            # videoTimer = time.time()
            
        #handle bottom image
        if (time.mktime(currentTime.timetuple()) - bottomTimer > 30):
            currentBottomImage = NextIndex(currentBottomIndex, len(bottomImages))
            img = ImageTk.PhotoImage(Image.open(bottomImages[currentBottomImage]))
            bottomPanel.configure(image = img)
            bottomPanel.image = img
            bottomPanel.pack(side = "bottom", fill = "both", expand = "yes")
        #update the window
        window.update()              
        
        
main()          
