from video import Video

class TVShow(Video):
    def __init__(self,show_name,duration,season,episode,tv_station):
        Video.__init__(self,show_name,duration)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station

    def show_info(self):
        print("Video Title"+self.title)
        print("Video Duration"+str(self.duration))
        print("TV Show season:"+self.season)
        print("TV Show episode:"+self.episode)
        print("TV Show station:"+self.tv_station)
    
        
