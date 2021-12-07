from pymongo import MongoClient
import os

host = os.environ.get("DB_URL")
client = MongoClient(host=host)
db = client.get_database("final-project")

card = db.card
coin = db.coin
dice = db.dice
rps = db.rps