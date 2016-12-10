class Video():
    def __init__(self,title,duration):
        print("Came in parent class Video")
        self.title    = title
        self.duration = duration
    

    def show_info(self):
        print("Video Title"+self.title)
        print("Video Duration"+str(self.duration))

