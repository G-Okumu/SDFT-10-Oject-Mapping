from director import Director
from config import db_cursor, db_connection
from error import NotFoundError

class Movie:
    all_movie_instances = []
    
    def __init__(self, title, genre, director_id, id = None) -> None:
        self.id = None
        self.title = title
        self.genre = genre
        self.director_id = self.check_if_director_id_exists(director_id)
        
    ## Check if the director exists before linking it with the movie
    def check_if_director_id_exists(self, director_id):
        director = db_cursor.execute(
            """SELECT id FROM directors WHERE id = ?""",
            (director_id,)
        ).fetchone()
        
        if director is None:
            raise NotFoundError(f"Director with ID {director_id} not found.")
        
        return director_id
        

    
    
    @classmethod
    def create_table(cls):
        query = """
        CREATE TABLE IF NOT EXISTS movies (id integer primary key AUTOINCREMENT, title varchar(32), genre varchar(255), director_id integer, created_at timestamp, updated_at timestamp)
        """
        db_cursor.execute(query)
        print("------ Table created successfully ---------")
        
    @classmethod
    def drop_table(cls):
        db_cursor.execute(""" DROP TABLE IF EXISTS movies""")
        print("---- Table dropped successfly -----")
        
    def save(self):
        query = """
        
        insert into movies (title, genre, director_id, created_at, updated_at) values (?, ?, ?, datetime('now'), datetime('now'))
        
        """
        
        db_cursor.execute(query, (self.title, self.genre, self.director_id,))
        db_connection.commit()
    
    # @classmethod
    # def display_all_movie_instances(cls):
    #     print("Below is all movie instances")
    #     return [{"title": movie.title, "genre": movie.genre, "director": movie.director.name} for movie in Movie.all_movie_instances]
        