from config import db_connection, db_cursor
# install sqlalchemy

class Director:
    
    list_of_directors = []
    
    def __init__(self, name) -> None:
        self.name = name
        
    @classmethod
    def create_table(cls):
        print("Table being created ---------------+000-----")
        
        sql_query = """
        
        CREATE TABLE IF NOT EXISTS directors (id integer primary key AUTOINCREMENT, name varchar(30))
        
        """
        
        db_cursor.execute(sql_query)
        
    @classmethod
    def drop_table(cls):
        print("Table being dropped ---------------+000-----")
        
        query = """
        DROP TABLE IF EXISTS directors
        """
        
        db_cursor.execute(query)
        print("Table dropped successfully ---------------+000-----")
        
    def save(self):
        print("Save method called ---------------+000-----")
        
        query = """
        INSERT INTO directors (name) VALUES (?)
        """
        
        db_cursor.execute(query, (self.name,))
        db_connection.commit()
    
    ## Get all dorectors
    @classmethod
    def get_all_directors(cls):
        query = """
        SELECT * from directors
        """
        
        data_found = db_cursor.execute(query).fetchall()
        
        return data_found;
        
        
        
    
        

    
        
        
    # def returns_all_director_movies(self):
    #     from movie import Movie
    #     return [{'title': movie.title, 'genre': movie.genre} for movie in Movie.all_movie_instances if movie.director == self]