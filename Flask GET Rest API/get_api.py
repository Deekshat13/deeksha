from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load movie data from config.json
with open('config.json', 'r') as json_file:
    movie_data = json.load(json_file)
    movies = movie_data.get('movies', [])


@app.route('/', methods=['GET'])
def get_movies():
    return jsonify(movies)


@app.route('/<year>', methods=['GET'])
def get_movie(year):
    movies_in_same_year = []
    for item in movies:
        if item['year'] == year:
            movies_in_same_year.append(item)
    return movies_in_same_year


if __name__ == '__main__':
    app.run(debug=True)

