import webbrowser

class Movie():
    """Server-side code that stores a list of favorite movies,
    including the movie poster and the movie trailer URL.
    This comment is printed when we type print(media.Movie.__doc__)
    """
    #init is a function defined within the class Movie
    #self is itself, or the instance of it being created
    #movie_title gets value of ''Toy Story", etc 
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
    		#initialize movie variables
    		self.title = movie_title
    		self.storyline = movie_storyline
    		self.poster_image_url = poster_image
    		self.trailer_youtube_url = trailer_youtube

    #function defined within a class is called an INSTANCE METHOD
    def show_trailer(self):
        #link is stored in instance variable called trailer_youtube_url
        #access this variable thru self keyword
        webbrowser.open(self.trailer_youtube_url)
