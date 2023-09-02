from peewee import *
import datetime

db_url = 'db.sqlite3'
db = SqliteDatabase(db_url)

class BaseModel(Model):
    class Meta:
        database = db

class Person(BaseModel):
    name = CharField(unique=True)
    kg = FloatField(null=True)

    now_drink = IntegerField(null=True, default=0)

class Container(BaseModel):
    title = CharField(unique=True, max_length=30, null=False)
    capacity = FloatField(null=False)

class Info(BaseModel):
    daily_goal = FloatField(null=True)
    drank = FloatField(null=False, default=0)
    reached_goal = BooleanField(default=False)

    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=None, null=True)

    person = ForeignKeyField(Person, backref='infos', null=True)