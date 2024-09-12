from movie import Movie
from director import Director



direct1 = Director('Frodo')
direct2 = Director('Francis Ford')

lord_of_the_rings = Movie('Lord of the Rings', 'Fantasy', direct1);
harry_porter = Movie('Harry Porter', 'Fantasy', direct1);
god_father = Movie('God Father', 'Crime', direct2);


# print(lord_of_the_rings.title);

# print(Movie.display_all_movie_instances())

print(f'{direct1.name} directed these movies: {direct1.returns_all_director_movies()}')

