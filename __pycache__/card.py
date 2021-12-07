from flask import render_template, request, redirect, url_for
import pymongo
from bson.objectid import ObjectId
from flask import Blueprint

from database import *
from flask import Blueprint

card_draws = Blueprint ('card_draws', __name__)

@card_draws.route("/")
def index():
    return render_template("index.html")

@card_draws.route("/card")
def card_draws():
    return render_template("card_draws.html")

@card_draws.route("/card/new")
def card_draw():
    return render_template("card_draw.html")