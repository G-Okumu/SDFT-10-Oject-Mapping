from config import db_connection, db_cursor
# install sqlalchemy

class Director:
    
    list_of_directors = []
    
    def __init__(self, name, id = None) -> None:
        self.id = id
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
        ## Reassing the id from db to be used in movie.py to check existence of db
        self.id = db_cursor.execute("SELECT last_insert_rowid() FROM directors").fetchone()[0]

    
    ## Get all directors
    @classmethod
    def get_all_directors(cls):
        query = """
        SELECT * from directors
        """
        
        data_found = db_cursor.execute(query).fetchall()
        
        return data_found;
        
    ## Method to return all movies for a certain director
    def get_all_movies_for_director(self):
        movies = db_cursor.execute(""" SELECT * from movies where movies.director_id = ? """, (self.id,)).fetchall()
        movies_list = []
        ## Change the movie tuple into Object now
        for movie in movies:
            movies_list.append({"title": movie[1], "genre": movie[2], "created_on": movie[4]})
            
        print(movies_list)
        
    def director_add_movie(self, title, genre):
        db_cursor.execute(""" insert into movies (title, genre, director_id, created_at, updated_at) values (?, ?, ?, datetime('now'), datetime('now')) """, (title, genre, self.id,))
        db_connection.commit()
        print("Movie added")