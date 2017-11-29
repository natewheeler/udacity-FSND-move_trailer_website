'''
Objective: Create a data structure (i.e. a Python Class) to store your favorite movies,
including movie title, box art URL (or poster URL) and a YouTube link to the movie trailer.
'''
import webbrowser


class Movie():
    def __init__(self,movie_title,poster_url,trailer):
        self.title = movie_title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)



