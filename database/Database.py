from peewee import *

users_db = PostgresqlDatabase('users.db')  # db with user id (key) and user name
anime_db = PostgresqlDatabase('anime.db')  # db with anime id (key) and anime name
genre_db = PostgresqlDatabase('genre.db')  # db with genre id (key) and genre name
anime_score_db = PostgresqlDatabase('anime_score.db')  # db with anime id (FK, key), user id (FK, key) and score
anime_genre_db = PostgresqlDatabase('anime_genre.db')  # db with anime id (FK, key) and genre id (FK, key)


class User(Model):
    id = IntegerField()
    name = CharField()

    class Meta:
        database = users_db


class Anime(Model):
    id = IntegerField()
    name = CharField()

    class Meta:
        database = anime_db


class Genre(Model):
    id = IntegerField()
    name = CharField()

    class Meta:
        database = genre_db


class AnimeScore(Model):
    anime_id = ForeignKeyField(Anime, backref='id')
    user_id = ForeignKeyField(User, backref='id')
    score = IntegerField()

    class Meta:
        databse: anime_score_db


class AnimeGenre(Model):
    anime_id = ForeignKeyField(Anime, backref='id')
    genre_id = ForeignKeyField(Genre, backref='id')

    class Meta:
        databse: anime_genre_db
