# Movie and Director Management System

This project provides a simple Python-based system for managing movies and their corresponding directors using SQLite. It includes functionality for creating and saving movies, validating directors, and displaying all movie instances from the database.

## Features

- **Movie Creation:** Create and store movies in the database with a title, genre, and associated director.
- **Director Validation:** Ensure that a movie can only be created if the associated director exists in the database.
- **Data Persistence:** Use SQLite for persistent storage of movies and directors.
- **Movie Display:** Retrieve and display all movies along with their corresponding directors.

## Prerequisites

- Python 3.x
- SQLite3

## Installation

1. **Clone the repository:**
   ```bash
   git clone git@github.com:G-Okumu/SDFT-10-Oject-Mapping.git
   cd SDFT-10-Object-Mapping
2. ***Install the Required Dependencies***
    - No additional packages are required as the project uses standard libraries. Ensure you have SQLite3 installed within your system
3. **Set up the Database**
    - Ensure the SQLite database is configured correctly in config.py.
    - Create the necessary tables by calling the create_table method of both the Movie and Director classes.

    ****Establish a database connection****
    ```bash
    db_connection = sqlite3.connect('db/movie.sqlite3')
    db_cursor = db_connection.cursor()


## Classes

### `Director`

The `Director` class manages the information related to movie directors. It allows you to create, save, and retrieve director records in the database. Key functionalities include:
- Creating a new director record.
- Saving the director record to the database.
- Ensuring the integrity of director records when linked with movies.

### `Movie`

The `Movie` class represents movie records in the database. It facilitates the creation and management of movies, including:
- Associating movies with directors via `director_id`.
- Checking if the specified `director_id` exists before saving a movie.
- Saving movie details to the database.
- Displaying all movies with their associated directors.

### `NotFoundError`

The `NotFoundError` class is a custom exception used to handle cases where a movie is attempted to be created with a non-existent `director_id`. It ensures that a movie cannot be saved without a valid director, maintaining data integrity.


## LICENSE

[License.txt](LICENSE.txt)

### Acknowledgements

    This project uses SQLite for data persistence and is designed as a simple educational tool for learning basic database interactions in Python.

- ***This `README.md` file provides clear instructions for setting up the project, using its features, handling errors, and includes an example workflow. Feel free to customize it further based on your project's specifics.***





