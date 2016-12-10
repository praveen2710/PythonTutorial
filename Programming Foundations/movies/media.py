import webbrowser
import video

class Movie(video.Video):
    """This class provides a way to save movie related attributes"""


    VALID_RATINGS =["G","PG","PG-13","R"]
    def __init__(self,movie_title,movie_duration,movie_storyline,poster_image,trailer_youtube):

        video.Video.__init__(self,movie_title,movie_duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url =trailer_youtube

    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def show_info(self):
      print("came in movie show info")
      print("Movie Title:"+self.title)
      print("Movie Duration:"+str(self.duration))

        

    
