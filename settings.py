# importing libraries
from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()



#creating an instance of flask app
app = Flask(__name__)

#configure our database

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+mysqlconnector://' + os.getenv("SQLUSER") + ':' + os.getenv("PASSWORD") \
                                       + '@' + os.getenv("SERVER") +'/'+ os.getenv("DATABASE")
print(app.config['SQLALCHEMY_DATABASE_URI'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')


