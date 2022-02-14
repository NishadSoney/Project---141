from flask import Flask,jsonify,request
import csv

all_articles = []
with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_liked_articels = []

app = Flask(__name__)

@app.route("/get-article")
def get_article():
    return jsonify({
        "data": all_articles[0],
        "status": "success"
    })

@app.route("/liked-articles", methods=["POST"])
def liked_movie():
    movie = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(movie)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-articles", methods=["POST"])
def unliked_movie():
    movie = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articels.append(movie)
    return jsonify({
        "status": "success"
    }), 201


if __name__ == "__main__":
  app.run()