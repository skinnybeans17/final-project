from flask import Flask, render_template, request, redirect, url_for, flash
import os
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

host = os.environ.get("DB_URL")
client = MongoClient(host=host)
db = client.get_database("final-project")
cards = db.cards
coins = db.coins
dice = db.dice
rps_games = db.rps_games

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/card")
def card_draws():
    return render_template("card_draws.html")

@app.route("/card/new")
def card_draw():
    return render_template("card_draw.html")

@app.route('/card', methods=['POST'])
def card_log():
  card_draw = {
    'color': request.form.get('color'),
    'number': request.form.get('number'),
    }
  card_draws.insert_one(card_draw)
  flash('Your game record has been added!')
  return redirect(url_for('card_draws'))

@app.route('/card/<card_id>/remove', methods=['POST'])
def card_delete(card_id):
    cards.delete_one({'_id': ObjectId(card_id)})
    flash('Your game record has been deleted!')
    return redirect(url_for('card_draws'))

@app.route("/coin")
def coin_flips():
    return render_template("coin_flips.html")

@app.route("/coin/new")
def coin_flip():
    return render_template("coin_flip.html")

@app.route('/coin', methods=['POST'])
def coin_log():
  coin_flip = {
    'type': request.form.get('type'),
    'side': request.form.get('side'),
    }
  coin_flips.insert_one(coin_flip)
  flash('Your game record has been added!')
  return redirect(url_for('coin_flips'))

@app.route('/coin/<coin_id>/remove', methods=['POST'])
def coin_delete(coin_id):
    coins.delete_one({'_id': ObjectId(coin_id)})
    flash('Your game record has been deleted!')
    return redirect(url_for('coin_flips'))

@app.route("/dice")
def dice_rolls():
    return render_template("dice_rolls.html")

@app.route("/dice/new")
def dice_roll():
    return render_template("dice_roll.html")

@app.route('/die', methods=['POST'])
def dice_log():
  dice_roll = {
    'dice_num': request.form.get('dice_num'),
    'output_num': request.form.get('output_num'),
    }
  dice_rolls.insert_one(dice_roll)
  flash('Your game record has been added!')
  return redirect(url_for('dice_rolls'))

@app.route('/die/<die_id>/remove', methods=['POST'])
def die_delete(die_id):
    dice.delete_one({'_id': ObjectId(die_id)})
    flash('Your game record has been deleted!')
    return redirect(url_for('dice_rolls'))

@app.route("/rps")
def rps_plays():
    return render_template("rps_plays.html")

@app.route("/rps/new")
def rps_play():
    return render_template("rps_play.html")

@app.route('/rps', methods=['POST'])
def rps_log():
  rps = {
    'input': request.form.get('input'),
    'output': request.form.get('output'),
    }
  rps_games.insert_one(rps)
  flash('Your game record has been added!')
  return redirect(url_for('rps_plays'))

@app.route('/rps/<rps_id>/remove', methods=['POST'])
def rps_delete(rps_id):
    rps_games.delete_one({'_id': ObjectId(rps_id)})
    flash('Your game record has been deleted!')
    return redirect(url_for('rps_plays'))

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=os.environ.get("PORT", 5500))