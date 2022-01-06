from settings import *
from loggerfile import LoggerFile
import json
import logging

#creates Logger instance
LoggerFile.set_logger('movies','movie.log',logging.DEBUG)
logger = logging.getLogger('movies')

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
#
# f = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
# fh = logging.FileHandler("movies.log")
# fh.setFormatter(f)
#
# logger.addHandler(fh)

#Initializing our database
db = SQLAlchemy(app)

# the class Movie will inherit the db.model of SQLALChemy
class Movie(db.Model):
    __tablename__ = "tbl_movies"  #creating a table name
    id = db.Column(db.Integer, primary_key=True) # This is primary key
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(100), nullable=False)


    def json(self):
        # this method will return output in json
        return {'id': self.id, 'title': self.title, 'year': self.year, 'genre': self.genre}

    def add_movie(_title, _year, _genre):
        ''' function to add movie to database using _title,_year__genre
        as parameters'''
        # creating instance of our movie constructor
        try:
            new_movie = Movie(title=_title, year=_year, genre=_genre)
            db.session.add(new_movie) # add new movie to database session
            db.session.commit() # commit changes to session
            logger.debug("Movie details successfully added to database...")
        except Exception as e:
            logger.critical("Issue with book details addition..." + str(e))
            print(e)


    def get_all_movies():
        '''function to get all movies from databse '''
        return [Movie.json(movie) for movie in Movie.query.all()]

    def get_movie(_id):
        '''function to get movie using the id of movie paramter'''
        return [Movie.json(Movie.query.filter_by(id=_id).first())]
        # Movie.json() coverts our output to the json format defined earlier
        # the filter_by method filters the query by the id
        # since our id is unique we will only get one result
        # the .first() method will get that first value returned

    def update_movie(_id, _title, _year, _genre):
        '''function to update the details of a movie using the id, title,
                year and genre as parameters'''
        try:
            movie_to_update = Movie.query.filter_by(id=_id).first()
            movie_to_update.title = _title
            movie_to_update.year = _year
            movie_to_update.genre = _genre
            db.session.commit()
            logger.debug("Movie details successfully updated to database...")
        except Exception as e:
            logger.critical("Issue with movie details updating..." + str(e))
            print(e)

    def delete_movie(_id):
        '''function to delete a movie from our database using
                   the id of the movie as a parameter'''
        try:
            Movie.query.filter_by(id=_id).delete()
            # filter by id and delete
            db.session.commit() # commiting new changes to our database
            logger.debug("Movie details successfully deleted from database...")
        except Exception as e:
            logger.critical("Issue with movie details deleting..." + str(e))
            print(e)
