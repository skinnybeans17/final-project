from flask import Flask, render_template, request, redirect, url_for, flash
import os
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

host = os.environ.get("DB_URL")
client = MongoClient(host=host)
db = client.get_database("final-project")
card_draws = db.card_draws
coin_flips = db.coin_flips
dice_rolls = db.dice_rolls
rps_games = db.rps_games

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/card")
def card_drawed():
    return render_template("card_draws.html")

@app.route("/card/new")
def card_draw():
    return render_template("card_draw.html")

@app.route('/card', methods=['POST'])
def card_log():
  card_draw = {
    'card': request.form.get('card'),
    }
  card_draws.insert_one(card_draw)
  flash('Your game record has been added!')
  return redirect(url_for('card_draws'))

@app.route('/card/<card_id>')
def card_show(card_id):
    card_draw = card_draws.find_one({'_id': ObjectId(card_id)})
    return render_template('card_show.html', card_draw=card_draw)

@app.route('/card/<coin_id>', methods=['POST'])
def card_update(card_id):
    updated_card = {
        'card': request.form.get('card'),
    }
    coin_flip.update_one(
        {'_id': ObjectId(card_id)},
        {'$set': updated_card})
    return redirect(url_for('playlists_show', card_id=card_id))

@app.route('/card/<card_id>/remove', methods=['POST'])
def card_delete(card_id):
    card_draws.delete_one({'_id': ObjectId(card_id)})
    flash('Your game record has been deleted!')
    return redirect(url_for('card_draws'))

@app.route("/coin")
def coin_flipped():
    return render_template("coin_flips.html")

@app.route("/coin/new")
def coin_flip():
    return render_template("coin_flip.html")

@app.route('/coin', methods=['POST'])
def coin_log():
  coin = {
    'type': request.form.get('type'),
    'side': request.form.get('side'),
    }
  coin_flips.insert_one(coin)
  flash('Your game record has been added!')
  return redirect(url_for('coin_flips'))

@app.route('/coin/<coin_id>')
def coin_show(coin_id):
    coin = coin_flips.find_one({'_id': ObjectId(coin_id)})
    return render_template('coin_show.html', coin=coin)

@app.route('/coin/<coin_id>', methods=['POST'])
def coin_update(coin_id):
    updated_coin = {
        'type': request.form.get('type'),
        'side': request.form.get('side'),
    }
    coin_flip.update_one(
        {'_id': ObjectId(coin_id)},
        {'$set': updated_coin})
    return redirect(url_for('playlists_show', coin_id=coin_id))

@app.route('/coin/<coin_id>/remove', methods=['POST'])
def coin_delete(coin_id):
    coin_flips.delete_one({'_id': ObjectId(coin_id)})
    flash('Your game record has been deleted!')
    return redirect(url_for('coin_flips'))

@app.route("/dice")
def dice_rolled():
    return render_template("dice_rolls.html")

@app.route("/dice/new")
def dice_roll():
    return render_template("dice_roll.html")

@app.route('/dice', methods=['POST'])
def dice_log():
  dice = {
    'dice_num': request.form.get('dice_num'),
    'output_num': request.form.get('output_num'),
    }
  dice_rolls.insert_one(dice)
  flash('Your game record has been added!')
  return redirect(url_for('dice_rolls'))

@app.route('/dice/<dice_id>')
def dice_show(dice_id):
    dice = dice_rolls.find_one({'_id': ObjectId(dice_id)})
    return render_template('dice_show.html', dice=dice)

@app.route('/dice/<dice_id>', methods=['POST'])
def dice_update(dice_id):
    updated_dice = {
        'dice_num': request.form.get('dice_num'),
        'output_num': request.form.get('output_num'),
    }
    coin_flip.update_one(
        {'_id': ObjectId(dice_id)},
        {'$set': updated_dice})
    return redirect(url_for('playlists_show', dice_id=dice_id))

@app.route('/dice/<dice_id>/remove', methods=['POST'])
def dice_delete(dice_id):
    dice_rolls.delete_one({'_id': ObjectId(dice_id)})
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

@app.route('/rps/<rps_id>')
def rps_show(rps_id):
    rps = rps_games.find_one({'_id': ObjectId(rps_id)})
    return render_template('rps_show.html', rps=rps)

@app.route('/rps/<rps_id>', methods=['POST'])
def rps_update(rps_id):
    updated_rps = {
        'input': request.form.get('input'),
        'output': request.form.get('output'),
    }
    coin_flip.update_one(
        {'_id': ObjectId(rps_id)},
        {'$set': updated_rps})
    return redirect(url_for('playlists_show', rps_id=rps_id))

@app.route('/rps/<rps_id>/remove', methods=['POST'])
def rps_delete(rps_id):
    rps_games.delete_one({'_id': ObjectId(rps_id)})
    flash('Your game record has been deleted!')
    return redirect(url_for('rps_plays'))

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=os.environ.get("PORT", 5500))