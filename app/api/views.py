'''API module'''
import logging

from flask import Blueprint, jsonify


from app.dao.app_dao import AppDAO


api_blueprint = Blueprint('api_blueprint', __name__)
app_dao = AppDAO()


@api_blueprint.route('/', methods=['GET'])
def api_root() -> str:
    '''Root method of api'''
    return "All works well. You can send your requests..."


@api_blueprint.route("/api/movie/<title>", methods=['GET'])
def movie_title(title: str):
    '''Return json. Filter movie by title'''
    logging.info('Запрос: /api/movie/%s', title)
    data = app_dao.search_movie_by_title(title)
    return jsonify(data)


@api_blueprint.route("/api/movie/<int:year_from>/to/<int:year_to>", methods=['GET'])
def movie_year_to_year(year_from: int, year_to: int):
    '''Return json. Filter movie year to year'''
    logging.info('Запрос: /api/movie/year/%s/to/%s', year_from, year_to)
    data = app_dao.search_movies_by_release_year(year_from, year_to)
    return jsonify(data)


@api_blueprint.route("/api/rating/children", methods=['GET'])
def movie_for_children():
    '''Return json. Filter movie by rating'''
    logging.info('Запрос: /api/rating/children')
    data = app_dao.search_movies_by_rating(tuple(["G"]))
    return jsonify(data)


@api_blueprint.route("/api/rating/family", methods=['GET'])
def movie_for_family():
    '''Return json. Filter movie by rating'''
    logging.info('Запрос: /api/rating/children')
    data = app_dao.search_movies_by_rating(tuple(['G', 'PG', 'PG-13']))
    return jsonify(data)


@api_blueprint.route("/api/rating/adult", methods=['GET'])
def movie_for_adult():
    '''Return json. Filter movie by rating'''
    logging.info('Запрос: /api/rating/children')
    data = app_dao.search_movies_by_rating(tuple(['R', 'NC-17']))
    return jsonify(data)


@api_blueprint.route("/api/genre/<str:genre>", methods=['GET'])
def movie_by_genre(genre: str):
    '''Return json. Filter movie bt genre'''
    logging.info('Запрос: /api/genre/%s', genre)
    data = app_dao.search_movies_by_genre(genre)
    return jsonify(data)

