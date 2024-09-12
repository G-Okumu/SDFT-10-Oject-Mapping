## Rows and Columns = relational dbs
## Rows ? instance or class itself => instance
## Columns ? instance or instance attributes => instance attr
## tables ? instance or class itself => class itself
from director import Director

# Director.drop_table();

# Director.create_table();

# direct1 = Director('Frodo')
# direct2 = Director('Francis Ford')


# direct2.save();
# direct1.save();

print(Director.get_all_directors());