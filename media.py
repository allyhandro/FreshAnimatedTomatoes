# author: Ally Han
# Class Movie implements a Movie object and holds the movie title, storyline,
    # poster image, and a link to the trailer
import webbrowser

class Movie():

    # initialization / constructor
    def __init__ (self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # show trailer function uses webbrowser library to open webbrowser to url
    def show_trailer (self):
        webbrowser.open(self.trailer_youtube_url)
