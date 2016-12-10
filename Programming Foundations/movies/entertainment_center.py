import media
import fresh_tomatoes
from tv_shows import TVShow

toy_story = media.Movie("toyStory",150,
                       "A story of boy and his toys that come to life",
                       "http://img.lum.dolimg.com/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")



avatar   = media.Movie("Avatar",166,
                       "A marine on alien planet",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                       "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
                       
the_mask = media.Movie("The Mask",130,
                   "A guy who finds a magical mask",
                   "http://static.fastcommerce.com/content/ff808081163c05b001169d6655243ae9/Mask_video_poster.jpg",
                   "https://www.youtube.com/watch?v=hOqVRwGVUkA")


breaking_bad = TVShow("Breaking Bad",60,"EP1","Season 1","NetFlix")
breaking_bad.show_info()


movies = [toy_story,avatar,the_mask]


print(media.Movie.__doc__)
print(media.__name__)
print(media.Movie.__module__)
toy_story.show_info()
print(media.Movie.VALID_RATINGS)

fresh_tomatoes.open_movies_page(movies)

print(avatar.storyline)
#the_mask.showTrailer()
