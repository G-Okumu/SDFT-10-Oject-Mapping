from director import Director

class Movie:
    all_movie_instances = []
    
    def __init__(self, title, genre, director) -> None:
        self.title = title
        self.genre = genre
        if isinstance(director, Director):
            self.director = director ## relationship btn movie and director
        else:
            raise ValueError('Director object has not been created.')

        Movie.all_movie_instances.append(self)
        
    @classmethod
    def display_all_movie_instances(cls):
        print("Below is all movie instances")
        return [{"title": movie.title, "genre": movie.genre, "director": movie.director.name} for movie in Movie.all_movie_instances]
        