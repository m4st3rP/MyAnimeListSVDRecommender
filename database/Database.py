from peewee import *


db = PostgresqlDatabase('database.db')


class User(Model):
    id = IntegerField()  # key
    name = CharField()

    class Meta:
        database = db


class Anime(Model):
    id = IntegerField()  # key
    name = CharField()

    class Meta:
        database = db


class Genre(Model):
    id = IntegerField()  # key
    name = CharField()

    class Meta:
        database = db


class AnimeScore(Model):
    anime_id = ForeignKeyField(Anime, backref='id')  # key
    user_id = ForeignKeyField(User, backref='id')  # key
    score = IntegerField()

    class Meta:
        databse: db


class AnimeGenre(Model):
    anime_id = ForeignKeyField(Anime, backref='id')  # key
    genre_id = ForeignKeyField(Genre, backref='id')  # key

    class Meta:
        databse: db


def initialize_dbs():
    db.connect()
    db.create_tables([User, Anime, Genre, AnimeScore, AnimeGenre])


def test():
    initialize_dbs()
    test_user = User(id=1, name="Hans Peter")
    print(test_user.save())
    for user in User.select():
        print(user.id + user.name)
    test_user.delete_instance()
