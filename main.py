class Movie:
    def __init__(self, movie_name) -> None:
        pass
    
    
class Director:
    pass

class Genre:
    pass


## Techniques
## - Aggregation, - Association, - Composition


## Types of relationship in oop
## - one to one, - one to many , many to many, many-to-one,


# Define an Owner class and pass into the constructor a name argument.
# Define a Pet and pass into the constructor its name, pet_type and an optional owner.
# Define a class variable PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"] and validate that the pet_type is one of those types in the __init__ method.
# raise Exception if this check fails.
# Define a class variable all that stores all instances of the Pet class.
# In the Owner class write a method called pets(self) that returns a full list of the owner's pets.
# In the Owner class write a method called add_pet(self, pet) that checks that the the pet is of type Pet and adds the owner to the pet.
# In the Owner class write a method called get_sorted_pets(self) returns a sorted list of pets by their names.
# Owner and Pet should use isinstance to check types whenever instances are passed into methods.
# raise Exception if these checks fail.