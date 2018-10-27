from peewee import *
import psycopg2


db = PostgresqlDatabase('database.db', user='postgres', password='abc', host='127.0.0.1')
conn = psycopg2.connect(database="database", user="postgres", password="abc")


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
        database = db


class AnimeGenre(Model):
    anime_id = ForeignKeyField(Anime, backref='id')  # key
    genre_id = ForeignKeyField(Genre, backref='id')  # key

    class Meta:
        database = db


def initialize_db():
    db.connect()
    db.create_tables([User, Anime, Genre, AnimeScore, AnimeGenre])


def test():
    initialize_db()
    test_user = User(id=1, name="Hans Peter")
    test_user2 = User(id=2, name="Manfred Meisel")
    print(test_user.save())
    print(test_user2.save())
    for user in User.select():
        print(user.id + " " + user.name)
    test_user.delete_instance()
    test_user2.delete_instance()
