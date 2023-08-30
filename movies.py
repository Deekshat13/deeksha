from flask import Flask, jsonify

app = Flask(__name__)

movies = [
    {"id": "1", "title": "Inception: The Beginning", "year": "2015", "genre": "Action", "rating": 8.1},
    {"id": "2", "title": "The ShawShank", "year": "2015", "genre": "Drama", "rating": 8.2},
    {"id": "3", "title": "The Dark Knight", "year": "2018", "genre": "Drama", "rating": 8.5},
    {"id": "4", "title": "Forrest Gump", "year": "2019", "genre": "Sports Drama", "rating": 8.7},
    {"id": "5", "title": "Forrest Gump", "year": "2019", "genre": "Sports Drama", "rating": 8.7},
    {"id": "6", "title": "Forrest Gump", "year": "2019", "genre": "Sports Drama", "rating": 8.7},

]


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
