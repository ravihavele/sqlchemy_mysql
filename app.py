from movies import *
from userschema import UserSchema
from loggerfile import LoggerFile
import logging
from functools import wraps
from marshmallow import Schema, fields, ValidationError

#creates Logger instance
LoggerFile.set_logger('app','app.log',logging.DEBUG)
logger = logging.getLogger('app')

# #creates Logger instance
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# f = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
# fh = logging.FileHandler("app.log")
# fh.setFormatter(f)
# logger.addHandler(fh)


# class UserSchema(Schema):
#     title = fields.String(required=True)
#     year = fields.Integer(required=True)
#     genre = fields.String(required=True)

def required_params(schema):
    def decorator(fn):
        # print("I m here")
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                schema.load(request.get_json())
            except ValidationError as err:
                error = {
                    "status": "error",
                    "messages": err.messages
                }
                return jsonify(error), 400
            return fn(*args, **kwargs)

        return wrapper

    return decorator

# @app.route('/')
# def hello():
#     return "welcome to the flask tutorials"

# route to get all Movies
@app.route("/movies", methods=["GET"])
def get_movies():
    '''Function to get all the movies in the database'''
    logger.debug("Getting movie from database by get_movies method..")
    return jsonify({'Movies': Movie.get_all_movies()})

# route to get movie by id
@app.route("/movie/<int:id>",methods=["GET"])
def get_movie_by_id(id):
    logger.debug("Getting movie from database by get_movies_by_id method..")
    return_value = Movie.get_movie(id)
    return jsonify(return_value)

#route to add movie
@app.route("/add_movie", methods=["POST"])
@required_params(UserSchema())
def add_movies():
    '''Function to add new movie to our database'''
    logger.debug("Adding movies to the database...")
    request_data = request.get_json() #getting data from client
    Movie.add_movie(request_data["title"], request_data["year"], request_data["genre"])
    responce = Response("Movie successfully added", status= 201, mimetype="application/json")
    return responce

#route to update movie with PUT Method
@app.route("/update_movie/<int:id>", methods=["PUT"])
@required_params(UserSchema())
def update_movie(id):
    '''Function to edit movie in our database using movie id'''
    logger.debug("Updating movies to the database...")
    request_data = request.get_json() # getting data from client
    Movie.update_movie(id, request_data["title"], request_data["year"], request_data["genre"])
    responce = Response("Movie successfully updated", status=200, mimetype="application/json")
    return responce

# route to delete movie using the DELETE method
@app.route("/delete_movie/<int:id>",methods=["DELETE"])
def delete_movie(id):
    '''Function to delete movie from our database'''
    logger.debug("Deleting movies to the database...")
    Movie.delete_movie(id)
    responce = Response("Movie successfully deleted", status=200, mimetype="application/json")
    return responce

if __name__=="__main__":
    # app.run(port=5000, debug=True)
    app.run(host="0.0.0.0", port=5000)

