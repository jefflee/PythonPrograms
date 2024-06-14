from sqlalchemy import create_engine, text, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

# Refer to this post
# https://planetscale.com/blog/using-mysql-with-sql-alchemy-hands-on-examples

Base = declarative_base()


class Film(Base):
    __tablename__ = 'film'
    film_id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    release_year = Column(Integer)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)


connection_string = "mysql+mysqlconnector://testuser:testuser@localhost:3306/sakila"
engine = create_engine(connection_string, echo=True)

with engine.connect() as connection:
    result = connection.execute(
        text("SELECT * FROM film WHERE title like :title"), dict(title="to%"))

    # Solution 1: print data by dictionary
    # for row in result.mappings():
    #     print("description:", row["description"])

    # Solution 2: map to an object
    films = [Film(**row) for row in result.mappings()]
    for film in films:
        print(f'film_id={film.film_id}, title={
              film.title}, description={film.description}, release_year={film.release_year}')
