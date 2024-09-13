## Rows and Columns = relational dbs
## Rows ? instance or class itself => instance
## Columns ? instance or instance attributes => instance attr
## tables ? instance or class itself => class itself
from director import Director
from movie import Movie

Director.drop_table();

Director.create_table();

direct1 = Director('Frodo')
direct2 = Director('Francis Ford')


direct2.save();
direct1.save();

# print(Director.get_all_directors());


Movie.drop_table()
Movie.create_table()

# Create a movie

lord_of_the_rings = Movie('Lord of the Rings', 'Fantasy', direct1.id);
harry_porter = Movie('Harry Porter', 'Fantasy', direct2.id);
GOT = Movie('Game Of Thrones', 'Fantasy & War', direct1.id)

lord_of_the_rings.save()
harry_porter.save()
GOT.save()

print("                  ")
print("   All Movies               ")

Movie.display_all_movie_instances()

print("                  ")
print("    Director adding a movie    ")
direct2.director_add_movie("Prison Break", "War & Crime")

print("                  ")
print("    All Movies for a certain Director    ")

direct1.get_all_movies_for_director()



