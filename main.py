import flask
from flask import request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


Users = []
Courses = []
#ScoreCards = [];

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    handicap = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return "User(email = {email}, username = {username}, handicap = {handicap}, password = {password})"

class CourseModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    par = db.Column(db.Integer, nullable=False)
    h1p = db.Column(db.Integer, nullable=False)
    h2p = db.Column(db.Integer, nullable=False)
    h3p = db.Column(db.Integer, nullable=False)
    h4p = db.Column(db.Integer, nullable=False)
    h5p = db.Column(db.Integer, nullable=False)
    h6p = db.Column(db.Integer, nullable=False)
    h7p = db.Column(db.Integer, nullable=False)
    h8p = db.Column(db.Integer, nullable=False)
    h9p = db.Column(db.Integer, nullable=False)
    h10p = db.Column(db.Integer, nullable=False)
    h11p = db.Column(db.Integer, nullable=False)
    h12p = db.Column(db.Integer, nullable=False)
    h13p = db.Column(db.Integer, nullable=False)
    h14p = db.Column(db.Integer, nullable=False)
    h15p = db.Column(db.Integer, nullable=False)
    h16p = db.Column(db.Integer, nullable=False)
    h17p = db.Column(db.Integer, nullable=False)
    h18p = db.Column(db.Integer, nullable=False)
    h1hc = db.Column(db.Integer, nullable=False)
    h2hc = db.Column(db.Integer, nullable=False)
    h3hc = db.Column(db.Integer, nullable=False)
    h4hc = db.Column(db.Integer, nullable=False)
    h5hc = db.Column(db.Integer, nullable=False)
    h6hc = db.Column(db.Integer, nullable=False)
    h7hc = db.Column(db.Integer, nullable=False)
    h8hc = db.Column(db.Integer, nullable=False)
    h9hc = db.Column(db.Integer, nullable=False)
    h10hc = db.Column(db.Integer, nullable=False)
    h11hc = db.Column(db.Integer, nullable=False)
    h12hc = db.Column(db.Integer, nullable=False)
    h13hc = db.Column(db.Integer, nullable=False)
    h14hc = db.Column(db.Integer, nullable=False)
    h15hc = db.Column(db.Integer, nullable=False)
    h16hc = db.Column(db.Integer, nullable=False)
    h17hc = db.Column(db.Integer, nullable=False)
    h18hc = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return "Course(name = {name}, par = {par}, h1 par = {h1p}, h2 par = {h2p}, h3 par = {h3p}, h4 par = {h4p}, h5 par = {h5p}, h6 par = {h6p}, h7 par = {h7p}, h8 par = {h8p}, h9 par = {h9p}, h10 par = {h10p}, h11 par = {h11p}, h12 par = {h12p}, h13 par = {h13p}, h14 par = {h14p}, h15 par = {h15p}, h16 par = {h16p}, h17 par = {h17p}, h18 par = {h18p}, h1 handicap = {h1hc}, h2 handicap = {h2hc}, h3 handicap = {h3hc}, h4 handicap = {h4hc}, h5 handicap = {h5hc}, h6 handicap = {h6hc}, h7 handicap = {h7hc}, h8 handicap = {h8hc}, h9 handicap = {h9hc}, h10 handicap = {h10hc}, h11 handicap = {h11hc}, h12 handicap = {h12hc}, h13 handicap = {h13hc}, h14 handicap = {h14hc}, h15 handicap = {h15hc}, h16 handicap = {h16hc}, h17 handicap = {h17hc}, h18 handicap = {h18hc}"

#class ScoreCardModel(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    uid = db.Column(db.Integer, nullable=False)
#    #Raw/unadjusted score
#    h1r = db.Column(db.Integer, nullable=False)
#    h2r = db.Column(db.Integer, nullable=False)
#    h3r = db.Column(db.Integer, nullable=False)
#    h4r = db.Column(db.Integer, nullable=False)
#    h5r = db.Column(db.Integer, nullable=False)
#    h6r = db.Column(db.Integer, nullable=False)
#    h7r = db.Column(db.Integer, nullable=False)
#    h8r = db.Column(db.Integer, nullable=False)
#    h9r = db.Column(db.Integer, nullable=False)
#    h10r = db.Column(db.Integer, nullable=False)
#    h11r = db.Column(db.Integer, nullable=False)
#    h12r = db.Column(db.Integer, nullable=False)
#    h13r = db.Column(db.Integer, nullable=False)
#    h14r = db.Column(db.Integer, nullable=False)
#    h15r = db.Column(db.Integer, nullable=False)
#    h16r = db.Column(db.Integer, nullable=False)
#    h17r = db.Column(db.Integer, nullable=False)
#    h18r = db.Column(db.Integer, nullable=False)
#    # - handicap strokes
#    h1hc = db.Column(db.Integer, nullable=False)
#    h2hc = db.Column(db.Integer, nullable=False)
#    h3hc = db.Column(db.Integer, nullable=False)
#    h4hc = db.Column(db.Integer, nullable=False)
#    h5hc = db.Column(db.Integer, nullable=False)
#    h6hc = db.Column(db.Integer, nullable=False)
#    h7hc = db.Column(db.Integer, nullable=False)
#    h8hc = db.Column(db.Integer, nullable=False)
#    h9hc = db.Column(db.Integer, nullable=False)
#    h10hc = db.Column(db.Integer, nullable=False)
#    h11hc = db.Column(db.Integer, nullable=False)
#    h12hc = db.Column(db.Integer, nullable=False)
#    h13hc = db.Column(db.Integer, nullable=False)
#    h14hc = db.Column(db.Integer, nullable=False)
#    h15hc = db.Column(db.Integer, nullable=False)
#    h16hc = db.Column(db.Integer, nullable=False)
#    h17hc = db.Column(db.Integer, nullable=False)
#    h18hc = db.Column(db.Integer, nullable=False)
#    # - beer strokes or other special strokes
#    h1sp = db.Column(db.Integer, nullable=False)
#    h2sp = db.Column(db.Integer, nullable=False)
#    h3sp = db.Column(db.Integer, nullable=False)
#    h4sp = db.Column(db.Integer, nullable=False)
#    h5sp = db.Column(db.Integer, nullable=False)
#    h6sp = db.Column(db.Integer, nullable=False)
#    h7sp = db.Column(db.Integer, nullable=False)
#    h8sp = db.Column(db.Integer, nullable=False)
#    h9sp = db.Column(db.Integer, nullable=False)
#    h10sp = db.Column(db.Integer, nullable=False)
#    h11sp = db.Column(db.Integer, nullable=False)
#    h12sp = db.Column(db.Integer, nullable=False)
#    h13sp = db.Column(db.Integer, nullable=False)
#    h14sp = db.Column(db.Integer, nullable=False)
#    h15sp = db.Column(db.Integer, nullable=False)
#    h16sp = db.Column(db.Integer, nullable=False)
#    h17sp = db.Column(db.Integer, nullable=False)
#    h18sp = db.Column(db.Integer, nullable=False)
#    def __repr__(self):
#        return "ScoreCard(user number = {uid}, h1 raw score = {h1r}, h2 raw score = {h2r}, h3 raw score = {h3r}, h4 raw score = {h4r}, h5 raw score = {h5r}, h6 raw score = {h6r}, h7 raw score = {h7r}, h8 raw score = {h8r}, h9 raw score = {h9r}, h10 raw score = {h10r}, h11 raw score = {h11r}, h12 raw score = {h12r}, h13 raw score = {h13r}, h14 raw score = {h14r}, h15 raw score = {h15r}, h16 raw score = {h16r}, h17 raw score = {h17r}, h18 raw score = {h18r}, h1 special strokes = {h1sp}, h2 special strokes = {h2sp}, h3 special strokes = {h3sp}, h4 special strokes = {h4sp}, h5 special strokes = {h5sp}, h6 special strokes = {h6sp}, h7 special strokes = {h7sp}, h8 special strokes = {h8sp}, h9 special strokes = {h9sp}, h10 special strokes = {h10sp}, h11 special strokes = {h11sp}, h12 special strokes = {h12sp}, h13 special strokes = {h13sp}, h14 special strokes = {h14sp}, h15 special strokes = {h15sp}, h16 special strokes = {h16sp}, h17 special strokes = {h17sp}, h18 special strokes = {h18sp}"
#

db.create_all()
db.session.commit()

course_put_args = reqparse.RequestParser()
course_put_args.add_argument("name", type=str, help="Name of the Golf Course", required=True)
course_put_args.add_argument("par", type=str, help="Par for the Course", required=True)
course_put_args.add_argument("h1p", type=int, help="Hole 1 Par", required=True)
course_put_args.add_argument("h2p", type=int, help="Hole 2 Par", required=True)
course_put_args.add_argument("h3p", type=int, help="Hole 3 Par", required=True)
course_put_args.add_argument("h4p", type=int, help="Hole 4 Par", required=True)
course_put_args.add_argument("h5p", type=int, help="Hole 5 Par", required=True)
course_put_args.add_argument("h6p", type=int, help="Hole 6 Par", required=True)
course_put_args.add_argument("h7p", type=int, help="Hole 7 Par", required=True)
course_put_args.add_argument("h8p", type=int, help="Hole 8 Par", required=True)
course_put_args.add_argument("h9p", type=int, help="Hole 9 Par", required=True)
course_put_args.add_argument("h10p", type=int, help="Hole 10 Par", required=False)
course_put_args.add_argument("h11p", type=int, help="Hole 11 Par", required=False)
course_put_args.add_argument("h12p", type=int, help="Hole 12 Par", required=False)
course_put_args.add_argument("h13p", type=int, help="Hole 13 Par", required=False)
course_put_args.add_argument("h14p", type=int, help="Hole 14 Par", required=False)
course_put_args.add_argument("h15p", type=int, help="Hole 15 Par", required=False)
course_put_args.add_argument("h16p", type=int, help="Hole 16 Par", required=False)
course_put_args.add_argument("h17p", type=int, help="Hole 17 Par", required=False)
course_put_args.add_argument("h18p", type=int, help="Hole 18 Par", required=False)
course_put_args.add_argument("h1hc", type=int, help="Hole 1 Handicap", required=True)
course_put_args.add_argument("h2hc", type=int, help="Hole 2 Handicap", required=True)
course_put_args.add_argument("h3hc", type=int, help="Hole 3 Handicap", required=True)
course_put_args.add_argument("h4hc", type=int, help="Hole 4 Handicap", required=True)
course_put_args.add_argument("h5hc", type=int, help="Hole 5 Handicap", required=True)
course_put_args.add_argument("h6hc", type=int, help="Hole 6 Handicap", required=True)
course_put_args.add_argument("h7hc", type=int, help="Hole 7 Handicap", required=True)
course_put_args.add_argument("h8hc", type=int, help="Hole 8 Handicap", required=True)
course_put_args.add_argument("h9hc", type=int, help="Hole 9 Handicap", required=True)
course_put_args.add_argument("h10hc", type=int, help="Hole 10 Handicap", required=False)
course_put_args.add_argument("h11hc", type=int, help="Hole 11 Handicap", required=False)
course_put_args.add_argument("h12hc", type=int, help="Hole 12 Handicap", required=False)
course_put_args.add_argument("h13hc", type=int, help="Hole 13 Handicap", required=False)
course_put_args.add_argument("h14hc", type=int, help="Hole 14 Handicap", required=False)
course_put_args.add_argument("h15hc", type=int, help="Hole 15 Handicap", required=False)
course_put_args.add_argument("h16hc", type=int, help="Hole 16 Handicap", required=False)
course_put_args.add_argument("h17hc", type=int, help="Hole 17 Handicap", required=False)
course_put_args.add_argument("h18hc", type=int, help="Hole 18 Handicap", required=False)

course_update_args = reqparse.RequestParser()
course_update_args.add_argument("name", type=str, help="Name of the Golf Course")
course_update_args.add_argument("par", type=str, help="Par for the Course")
course_update_args.add_argument("h1p", type=int, help="Hole 1 Par")
course_update_args.add_argument("h2p", type=int, help="Hole 2 Par")
course_update_args.add_argument("h3p", type=int, help="Hole 3 Par")
course_update_args.add_argument("h4p", type=int, help="Hole 4 Par")
course_update_args.add_argument("h5p", type=int, help="Hole 5 Par")
course_update_args.add_argument("h6p", type=int, help="Hole 6 Par")
course_update_args.add_argument("h7p", type=int, help="Hole 7 Par")
course_update_args.add_argument("h8p", type=int, help="Hole 8 Par")
course_update_args.add_argument("h9p", type=int, help="Hole 9 Par")
course_update_args.add_argument("h10p", type=int, help="Hole 10 Par")
course_update_args.add_argument("h11p", type=int, help="Hole 11 Par")
course_update_args.add_argument("h12p", type=int, help="Hole 12 Par")
course_update_args.add_argument("h13p", type=int, help="Hole 13 Par")
course_update_args.add_argument("h14p", type=int, help="Hole 14 Par")
course_update_args.add_argument("h15p", type=int, help="Hole 15 Par")
course_update_args.add_argument("h16p", type=int, help="Hole 16 Par")
course_update_args.add_argument("h17p", type=int, help="Hole 17 Par")
course_update_args.add_argument("h18p", type=int, help="Hole 18 Par")
course_update_args.add_argument("h1hc", type=int, help="Hole 1 Handicap")
course_update_args.add_argument("h2hc", type=int, help="Hole 2 Handicap")
course_update_args.add_argument("h3hc", type=int, help="Hole 3 Handicap")
course_update_args.add_argument("h4hc", type=int, help="Hole 4 Handicap")
course_update_args.add_argument("h5hc", type=int, help="Hole 5 Handicap")
course_update_args.add_argument("h6hc", type=int, help="Hole 6 Handicap")
course_update_args.add_argument("h7hc", type=int, help="Hole 7 Handicap")
course_update_args.add_argument("h8hc", type=int, help="Hole 8 Handicap")
course_update_args.add_argument("h9hc", type=int, help="Hole 9 Handicap")
course_update_args.add_argument("h10hc", type=int, help="Hole 10 Handicap")
course_update_args.add_argument("h11hc", type=int, help="Hole 11 Handicap")
course_update_args.add_argument("h12hc", type=int, help="Hole 12 Handicap")
course_update_args.add_argument("h13hc", type=int, help="Hole 13 Handicap")
course_update_args.add_argument("h14hc", type=int, help="Hole 14 Handicap")
course_update_args.add_argument("h15hc", type=int, help="Hole 15 Handicap")
course_update_args.add_argument("h16hc", type=int, help="Hole 16 Handicap")
course_update_args.add_argument("h17hc", type=int, help="Hole 17 Handicap")
course_update_args.add_argument("h18hc", type=int, help="Hole 18 Handicap")

resource_fields_course = {
    'id': fields.Integer,
    'name': fields.String,
    'par': fields.Integer,
    'h1p': fields.Integer,
    'h2p': fields.Integer,
    'h3p': fields.Integer,
    'h4p': fields.Integer,
    'h5p': fields.Integer,
    'h6p': fields.Integer,
    'h7p': fields.Integer,
    'h8p': fields.Integer,
    'h9p': fields.Integer,
    'h10p': fields.Integer,
    'h11p': fields.Integer,
    'h12p': fields.Integer,
    'h13p': fields.Integer,
    'h14p': fields.Integer,
    'h15p': fields.Integer,
    'h16p': fields.Integer,
    'h17p': fields.Integer,
    'h18p': fields.Integer,
    'h1hc': fields.Integer,
    'h2hc': fields.Integer,
    'h3hc': fields.Integer,
    'h4hc': fields.Integer,
    'h5hc': fields.Integer,
    'h6hc': fields.Integer,
    'h7hc': fields.Integer,
    'h8hc': fields.Integer,
    'h9hc': fields.Integer,
    'h10hc': fields.Integer,
    'h11hc': fields.Integer,
    'h12hc': fields.Integer,
    'h13hc': fields.Integer,
    'h14hc': fields.Integer,
    'h15hc': fields.Integer,
    'h16hc': fields.Integer,
    'h17hc': fields.Integer,
    'h18hc': fields.Integer
}

#scorecard_put_args = reqparse.RequestParser()
#scorecard_put_args.add_argument("uid", type=int, help="User Number", required=True)
#scorecard_put_args.add_argument("h1r", type=int, help="Hole 1 Raw Score", required=True)
#scorecard_put_args.add_argument("h2r", type=int, help="Hole 2 Raw Score", required=True)
#scorecard_put_args.add_argument("h3r", type=int, help="Hole 3 Raw Score", required=True)
#scorecard_put_args.add_argument("h4r", type=int, help="Hole 4 Raw Score", required=True)
#scorecard_put_args.add_argument("h5r", type=int, help="Hole 5 Raw Score", required=True)
#scorecard_put_args.add_argument("h6r", type=int, help="Hole 6 Raw Score", required=True)
#scorecard_put_args.add_argument("h7r", type=int, help="Hole 7 Raw Score", required=True)
#scorecard_put_args.add_argument("h8r", type=int, help="Hole 8 Raw Score", required=True)
#scorecard_put_args.add_argument("h9r", type=int, help="Hole 9 Raw Score", required=True)
#scorecard_put_args.add_argument("h10r", type=int, help="Hole 10 Raw Score", required=False)
#scorecard_put_args.add_argument("h11r", type=int, help="Hole 11 Raw Score", required=False)
#scorecard_put_args.add_argument("h12r", type=int, help="Hole 12 Raw Score", required=False)
#scorecard_put_args.add_argument("h13r", type=int, help="Hole 13 Raw Score", required=False)
#scorecard_put_args.add_argument("h14r", type=int, help="Hole 14 Raw Score", required=False)
#scorecard_put_args.add_argument("h15r", type=int, help="Hole 15 Raw Score", required=False)
#scorecard_put_args.add_argument("h16r", type=int, help="Hole 16 Raw Score", required=False)
#scorecard_put_args.add_argument("h17r", type=int, help="Hole 17 Raw Score", required=False)
#scorecard_put_args.add_argument("h18r", type=int, help="Hole 18 Raw Score", required=False)
#scorecard_put_args.add_argument("h1hc", type=int, help="Hole 1 Handicap", required=True)
#scorecard_put_args.add_argument("h2hc", type=int, help="Hole 2 Handicap", required=True)
#scorecard_put_args.add_argument("h3hc", type=int, help="Hole 3 Handicap", required=True)
#scorecard_put_args.add_argument("h4hc", type=int, help="Hole 4 Handicap", required=True)
#scorecard_put_args.add_argument("h5hc", type=int, help="Hole 5 Handicap", required=True)
#scorecard_put_args.add_argument("h6hc", type=int, help="Hole 6 Handicap", required=True)
#scorecard_put_args.add_argument("h7hc", type=int, help="Hole 7 Handicap", required=True)
#scorecard_put_args.add_argument("h8hc", type=int, help="Hole 8 Handicap", required=True)
#scorecard_put_args.add_argument("h9hc", type=int, help="Hole 9 Handicap", required=True)
#scorecard_put_args.add_argument("h10hc", type=int, help="Hole 10 Handicap", required=False)
#scorecard_put_args.add_argument("h11hc", type=int, help="Hole 11 Handicap", required=False)
#scorecard_put_args.add_argument("h12hc", type=int, help="Hole 12 Handicap", required=False)
#scorecard_put_args.add_argument("h13hc", type=int, help="Hole 13 Handicap", required=False)
#scorecard_put_args.add_argument("h14hc", type=int, help="Hole 14 Handicap", required=False)
#scorecard_put_args.add_argument("h15hc", type=int, help="Hole 15 Handicap", required=False)
#scorecard_put_args.add_argument("h16hc", type=int, help="Hole 16 Handicap", required=False)
#scorecard_put_args.add_argument("h17hc", type=int, help="Hole 17 Handicap", required=False)
#scorecard_put_args.add_argument("h18hc", type=int, help="Hole 18 Handicap", required=False)
#scorecard_put_args.add_argument("h1sp", type=int, help="Hole 1 Extra Strokes", required=True)
#scorecard_put_args.add_argument("h2sp", type=int, help="Hole 2 Extra Strokes", required=True)
#scorecard_put_args.add_argument("h3sp", type=int, help="Hole 3 Extra Strokes", required=True)
#scorecard_put_args.add_argument("h4sp", type=int, help="Hole 4 Extra Strokes", required=True)
#scorecard_put_args.add_argument("h5sp", type=int, help="Hole 5 Extra Strokes", required=True)
#scorecard_put_args.add_argument("h6sp", type=int, help="Hole 6 Extra Strokes", required=True)
#scorecard_put_args.add_argument("h7sp", type=int, help="Hole 7 Extra Strokes", required=True)
#scorecard_put_args.add_argument("h8sp", type=int, help="Hole 8 Extra Strokes", required=True)
#scorecard_put_args.add_argument("h9sp", type=int, help="Hole 9 Extra Strokes", required=True)
#scorecard_put_args.add_argument("h10sp", type=int, help="Hole 10 Extra Strokes", required=False)
#scorecard_put_args.add_argument("h11sp", type=int, help="Hole 11 Extra Strokes", required=False)
#scorecard_put_args.add_argument("h12sp", type=int, help="Hole 12 Extra Strokes", required=False)
#scorecard_put_args.add_argument("h13sp", type=int, help="Hole 13 Extra Strokes", required=False)
#scorecard_put_args.add_argument("h14sp", type=int, help="Hole 14 Extra Strokes", required=False)
#scorecard_put_args.add_argument("h15sp", type=int, help="Hole 15 Extra Strokes", required=False)
#scorecard_put_args.add_argument("h16sp", type=int, help="Hole 16 Extra Strokes", required=False)
#scorecard_put_args.add_argument("h17sp", type=int, help="Hole 17 Extra Strokes", required=False)
#scorecard_put_args.add_argument("h18sp", type=int, help="Hole 18 Extra Strokes", required=False)

#scorecard_patch_args = reqparse.RequestParser()
#scorecard_patch_args.add_argument("uid", type=int, help="User Number")
#scorecard_patch_args.add_argument("h1r", type=int, help="Hole 1 Raw Score")
#scorecard_patch_args.add_argument("h2r", type=int, help="Hole 2 Raw Score")
#scorecard_patch_args.add_argument("h3r", type=int, help="Hole 3 Raw Score")
#scorecard_patch_args.add_argument("h4r", type=int, help="Hole 4 Raw Score")
#scorecard_patch_args.add_argument("h5r", type=int, help="Hole 5 Raw Score")
#scorecard_patch_args.add_argument("h6r", type=int, help="Hole 6 Raw Score")
#scorecard_patch_args.add_argument("h7r", type=int, help="Hole 7 Raw Score")
#scorecard_patch_args.add_argument("h8r", type=int, help="Hole 8 Raw Score")
#scorecard_patch_args.add_argument("h9r", type=int, help="Hole 9 Raw Score")
#scorecard_patch_args.add_argument("h10r", type=int, help="Hole 10 Raw Score")
#scorecard_patch_args.add_argument("h11r", type=int, help="Hole 11 Raw Score")
#scorecard_patch_args.add_argument("h12r", type=int, help="Hole 12 Raw Score")
#scorecard_patch_args.add_argument("h13r", type=int, help="Hole 13 Raw Score")
#scorecard_patch_args.add_argument("h14r", type=int, help="Hole 14 Raw Score")
#scorecard_patch_args.add_argument("h15r", type=int, help="Hole 15 Raw Score")
#scorecard_patch_args.add_argument("h16r", type=int, help="Hole 16 Raw Score")
#scorecard_patch_args.add_argument("h17r", type=int, help="Hole 17 Raw Score")
#scorecard_patch_args.add_argument("h18r", type=int, help="Hole 18 Raw Score")
#scorecard_patch_args.add_argument("h1hc", type=int, help="Hole 1 Handicap")
#scorecard_patch_args.add_argument("h2hc", type=int, help="Hole 2 Handicap")
#scorecard_patch_args.add_argument("h3hc", type=int, help="Hole 3 Handicap")
#scorecard_patch_args.add_argument("h4hc", type=int, help="Hole 4 Handicap")
#scorecard_patch_args.add_argument("h5hc", type=int, help="Hole 5 Handicap")
#scorecard_patch_args.add_argument("h6hc", type=int, help="Hole 6 Handicap")
#scorecard_patch_args.add_argument("h7hc", type=int, help="Hole 7 Handicap")
#scorecard_patch_args.add_argument("h8hc", type=int, help="Hole 8 Handicap")
#scorecard_patch_args.add_argument("h9hc", type=int, help="Hole 9 Handicap")
#scorecard_patch_args.add_argument("h10hc", type=int, help="Hole 10 Handicap")
#scorecard_patch_args.add_argument("h11hc", type=int, help="Hole 11 Handicap")
#scorecard_patch_args.add_argument("h12hc", type=int, help="Hole 12 Handicap")
#scorecard_patch_args.add_argument("h13hc", type=int, help="Hole 13 Handicap")
#scorecard_patch_args.add_argument("h14hc", type=int, help="Hole 14 Handicap")
#scorecard_patch_args.add_argument("h15hc", type=int, help="Hole 15 Handicap")
#scorecard_patch_args.add_argument("h16hc", type=int, help="Hole 16 Handicap")
#scorecard_patch_args.add_argument("h17hc", type=int, help="Hole 17 Handicap")
#scorecard_patch_args.add_argument("h18hc", type=int, help="Hole 18 Handicap")
#scorecard_patch_args.add_argument("h1sp", type=int, help="Hole 1 Extra Strokes")
#scorecard_patch_args.add_argument("h2sp", type=int, help="Hole 2 Extra Strokes")
#scorecard_patch_args.add_argument("h3sp", type=int, help="Hole 3 Extra Strokes")
#scorecard_patch_args.add_argument("h4sp", type=int, help="Hole 4 Extra Strokes")
#scorecard_patch_args.add_argument("h5sp", type=int, help="Hole 5 Extra Strokes")
#scorecard_patch_args.add_argument("h6sp", type=int, help="Hole 6 Extra Strokes")
#scorecard_patch_args.add_argument("h7sp", type=int, help="Hole 7 Extra Strokes")
#scorecard_patch_args.add_argument("h8sp", type=int, help="Hole 8 Extra Strokes")
#scorecard_patch_args.add_argument("h9sp", type=int, help="Hole 9 Extra Strokes")
#scorecard_patch_args.add_argument("h10sp", type=int, help="Hole 10 Extra Strokes")
#scorecard_patch_args.add_argument("h11sp", type=int, help="Hole 11 Extra Strokes")
#scorecard_patch_args.add_argument("h12sp", type=int, help="Hole 12 Extra Strokes")
#scorecard_patch_args.add_argument("h13sp", type=int, help="Hole 13 Extra Strokes")
#scorecard_patch_args.add_argument("h14sp", type=int, help="Hole 14 Extra Strokes")
#scorecard_patch_args.add_argument("h15sp", type=int, help="Hole 15 Extra Strokes")
#scorecard_patch_args.add_argument("h16sp", type=int, help="Hole 16 Extra Strokes")
#scorecard_patch_args.add_argument("h17sp", type=int, help="Hole 17 Extra Strokes")
#scorecard_patch_args.add_argument("h18sp", type=int, help="Hole 18 Extra Strokes")


#resource_fields_scorecard = {
#    'id': fields.Integer,
#    'uid': fields.Integer,
#    'h1r': fields.Integer,
#    'h2r': fields.Integer,
#    'h3r': fields.Integer,
#    'h4r': fields.Integer,
#    'h5r': fields.Integer,
#    'h6r': fields.Integer,
#    'h7r': fields.Integer,
#    'h8r': fields.Integer,
#    'h9r': fields.Integer,
#    'h10r': fields.Integer,
#    'h11r': fields.Integer,
#    'h12r': fields.Integer,
#    'h13r': fields.Integer,
#    'h14r': fields.Integer,
#    'h15r': fields.Integer,
#    'h16r': fields.Integer,
#    'h17r': fields.Integer,
#    'h18r': fields.Integer,
#    'h1hc': fields.Integer,
#    'h2hc': fields.Integer,
#    'h3hc': fields.Integer,
#    'h4hc': fields.Integer,
#    'h5hc': fields.Integer,
#    'h6hc': fields.Integer,
#    'h7hc': fields.Integer,
#    'h8hc': fields.Integer,
#    'h9hc': fields.Integer,
#    'h10hc': fields.Integer,
#    'h11hc': fields.Integer,
#    'h12hc': fields.Integer,
#    'h13hc': fields.Integer,
#    'h14hc': fields.Integer,
#    'h15hc': fields.Integer,
#    'h16hc': fields.Integer,
#    'h17hc': fields.Integer,
#    'h18hc': fields.Integer,
#    'h1sp': fields.Integer,
#    'h2sp': fields.Integer,
#    'h3sp': fields.Integer,
#    'h4sp': fields.Integer,
#    'h5sp': fields.Integer,
#    'h6sp': fields.Integer,
#    'h7sp': fields.Integer,
#    'h8sp': fields.Integer,
#    'h9sp': fields.Integer,
#    'h10sp': fields.Integer,
#    'h11sp': fields.Integer,
#    'h12sp': fields.Integer,
#    'h13sp': fields.Integer,
#    'h14sp': fields.Integer,
#    'h15sp': fields.Integer,
#    'h16sp': fields.Integer,
#    'h17sp': fields.Integer,
#    'h18sp': fields.Integer
#}

user_put_args = reqparse.RequestParser()
user_put_args.add_argument("email", type=str, help="Email", required=True)
user_put_args.add_argument("username", type=str, help="Username", required=True)
user_put_args.add_argument("handicap", type=int, help="Handicap", required=True)
user_put_args.add_argument("password", type=str, help="Password", required=True)

user_update_args = reqparse.RequestParser()
user_update_args.add_argument("email", type=str, help="Email")
user_update_args.add_argument("username", type=str, help="Username")
user_update_args.add_argument("handicap", type=int, help="Handicap")
user_update_args.add_argument("password", type=str, help="Password")

resource_fields_user = {
    'id': fields.Integer,
    'email': fields.String,
    'username': fields.String,
    'handicap': fields.Integer,
    'password': fields.String
}


@app.route('/', methods=['GET'])
def home():
    return "Hello World"


class User(Resource):
    @marshal_with(resource_fields_user)
    def get(self, uid):
        # abort_if_id_doesnt_exist(uid)
        # return Users[uid]
        result = UserModel.query.filter_by(id=uid).first()
        if not result:
            abort(404, message="Could Not Find That User")
        return result

    @marshal_with(resource_fields_user)
    def put(self):
        # abort_if_id_exists(uid)
        # args = user_put_args.parse_args()
        # Users[uid] = args
        # return Users[uid], 201
        uid = len(Users);

        args = user_put_args.parse_args()
        result = UserModel.query.filter_by(id=uid).first()
        if result:
            abort(409, message="ID TAKEN!")

        user = UserModel(id=uid, email=args['email'], username=args['username'], handicap=args['handicap'],
                         password=args['password'])
        db.session.add(user)
        db.session.commit()

        Users[uid] = user;
        return user, 201

    @marshal_with(resource_fields_user)
    def patch(self, uid):
        args = user_update_args.parse_args()
        result = UserModel.query.filter_by(id=uid).first()
        if not result:
            abort(404, message="ID NOT FOUND!")
        if args['email']:
            result.email = args['email']
        if args['username']:
            result.username = args['username']
        if args['handicap']:
            result.handicap = args['handicap']
        if args['password']:
            result.password = args['password']

        db.session.commit()
        return result

    def delete(self, uid):
        # abort_if_id_doesnt_exist(uid)
        # del Users[uid]
        result = UserModel.query.filter_by(id=uid).first()
        if not result:
            abort(404, message="ID NOT FOUND!")

        db.session.delete(result)
        db.session.commit()

        return '', 204

class Course(Resource):
    @marshal_with(resource_fields_course)
    def get(self, cid):
        result = CourseModel.query.filter_by(id=cid).first()
        if not result:
            abort(404, message="Could Not Find That Course")
        return result

    @marshal_with(resource_fields_course)
    def put(self):
        cid = len(Courses);
        args = course_put_args.parse_args()
        result = CourseModel.query.filter_by(id=cid).first()
        if result:
            abort(409, message="COURSE ID TAKEN!")

        course = CourseModel(id=cid, name=args['name'], par=args['par'],
                             h1p=args['h1p'],
                             h2p=args['h2p'],
                             h3p=args['h3p'],
                             h4p=args['h4p'],
                             h5p=args['h5p'],
                             h6p=args['h6p'],
                             h7p=args['h7p'],
                             h8p=args['h8p'],
                             h9p=args['h9p'],
                             h10p=args['h10p'],
                             h11p=args['h11p'],
                             h12p=args['h12p'],
                             h13p=args['h13p'],
                             h14p=args['h14p'],
                             h15p=args['h15p'],
                             h16p=args['h16p'],
                             h17p=args['h17p'],
                             h18p=args['h18p'],
                             h1hc=args['h1hc'],
                             h2hc=args['h2hc'],
                             h3hc=args['h3hc'],
                             h4hc=args['h4hc'],
                             h5hc=args['h5hc'],
                             h6hc=args['h6hc'],
                             h7hc=args['h7hc'],
                             h8hc=args['h8hc'],
                             h9hc=args['h9hc'],
                             h10hc=args['h10hc'],
                             h11hc=args['h11hc'],
                             h12hc=args['h12hc'],
                             h13hc=args['h13hc'],
                             h14hc=args['h14hc'],
                             h15hc=args['h15hc'],
                             h16hc=args['h16hc'],
                             h17hc=args['h17hc'],
                             h18hc=args['h18hc'])
        db.session.add(course)
        db.session.commit()

        Courses[cid] = course;

        return course, 201

    @marshal_with(resource_fields_course)
    def patch(self, cid):
        args = course_update_args.parse_args()
        result = UserModel.query.filter_by(id=cid).first()
        if not result:
            abort(404, message="ID NOT FOUND!")
        if args['name']:
            result.name = args['name']
        if args['par']:
            result.par = args['par']
        if args['h1p']:
            result.h1p = args['h1p']
        if args['h2p']:
            result.h2p = args['h2p']
        if args['h3p']:
            result.h3p = args['h3p']
        if args['h4p']:
            result.h4p = args['h4p']
        if args['h5p']:
            result.h5p = args['h5p']
        if args['h6p']:
            result.h6p = args['h6p']
        if args['h7p']:
            result.h7p = args['h7p']
        if args['h8p']:
            result.h8p = args['h8p']
        if args['h9p']:
            result.h9p = args['h9p']
        if args['h10p']:
            result.h10p = args['h10p']
        if args['h11p']:
            result.h11p = args['h11p']
        if args['h12p']:
            result.h12p = args['h12p']
        if args['h13p']:
            result.h13p = args['h13p']
        if args['h14p']:
            result.h14p = args['h14p']
        if args['h15p']:
            result.h15p = args['h15p']
        if args['h16p']:
            result.h16p = args['h16p']
        if args['h17p']:
            result.h17p = args['h17p']
        if args['h18p']:
            result.h18p = args['h18p']
        if args['h1hc']:
            result.h1hc = args['h1hc']
        if args['h2hc']:
            result.h2hc = args['h2hc']
        if args['h3hc']:
            result.h3hc = args['h3hc']
        if args['h4hc']:
            result.h4hc = args['h4hc']
        if args['h5hc']:
            result.h5hc = args['h5hc']
        if args['h6hc']:
            result.h6hc = args['h6hc']
        if args['h7hc']:
            result.h7hc = args['h7hc']
        if args['h8hc']:
            result.h8hc = args['h8hc']
        if args['h9hc']:
            result.h9hc = args['h9hc']
        if args['h10hc']:
            result.h10hc = args['h10hc']
        if args['h11hc']:
            result.h11hc = args['h11hc']
        if args['h12hc']:
            result.h12hc = args['h12hc']
        if args['h13hc']:
            result.h13hc = args['h13hc']
        if args['h14hc']:
            result.h14hc = args['h14hc']
        if args['h15hc']:
            result.h15hc = args['h15hc']
        if args['h16hc']:
            result.h16hc = args['h16hc']
        if args['h17hc']:
            result.h17hc = args['h17hc']
        if args['h18hc']:
            result.h18hc = args['h18hc']

        db.session.commit()
        return result

    def delete(self, cid):
        result = CourseModel.query.filter_by(id=cid).first()
        if not result:
            abort(404, message="ID NOT FOUND!")

        db.session.delete(result)
        db.session.commit()

        return '', 204

#class ScoreCard(Resource):
#    @marshal_with(resource_fields_scorecard)
#    def get(self, sid):
#        result = ScoreCardModel.query.filter_by(id=sid).first()
#        if not result:
#            abort(404, message="Could Not Find That ScoreCard")
#        return result
#
#    @marshal_with(resource_fields_course)
#    def put(self, sid):
#        sid = len(ScoreCards);
#        args = scorecard_put_args.parse_args()
#        result = ScoreCardModel.query.filter_by(id=sid).first()
#        if result:
#            abort(409, message="COURSE ID TAKEN!")
#
#        scorecard = CourseModel(id=sid, uid=args['uid'],
#                             h1r=args['h1r'],
#                             h2r=args['h2r'],
#                             h3r=args['h3r'],
#                             h4r=args['h4r'],
#                             h5r=args['h5r'],
#                             h6r=args['h6r'],
#                             h7r=args['h7r'],
#                             h8r=args['h8r'],
#                             h9r=args['h9r'],
#                             h10r=args['h10r'],
#                             h11r=args['h11r'],
#                             h12r=args['h12r'],
#                             h13r=args['h13r'],
#                             h14r=args['h14r'],
#                             h15r=args['h15r'],
#                             h16r=args['h16r'],
#                             h17r=args['h17r'],
#                             h18r=args['h18r'],
#                             h1hc=args['h1hc'],
#                             h2hc=args['h2hc'],
#                             h3hc=args['h3hc'],
#                             h4hc=args['h4hc'],
#                             h5hc=args['h5hc'],
#                             h6hc=args['h6hc'],
#                             h7hc=args['h7hc'],
#                             h8hc=args['h8hc'],
#                             h9hc=args['h9hc'],
#                             h10hc=args['h10hc'],
#                             h11hc=args['h11hc'],
#                             h12hc=args['h12hc'],
#                             h13hc=args['h13hc'],
#                             h14hc=args['h14hc'],
#                             h15hc=args['h15hc'],
#                             h16hc=args['h16hc'],
#                             h17hc=args['h17hc'],
#                             h18hc=args['h18hc'],
#                             h1sp=args['h1sp'],
#                             h2sp=args['h2sp'],
#                             h3sp=args['h3sp'],
#                             h4sp=args['h4sp'],
#                             h5sp=args['h5sp'],
#                             h6sp=args['h6sp'],
#                             h7sp=args['h7sp'],
#                             h8sp=args['h8sp'],
#                             h9sp=args['h9sp'],
#                             h10sp=args['h10sp'],
#                             h11sp=args['h11sp'],
#                             h12sp=args['h12sp'],
#                             h13sp=args['h13sp'],
#                             h14sp=args['h14sp'],
#                             h15sp=args['h15sp'],
#                             h16sp=args['h16sp'],
#                             h17sp=args['h17sp'],
#                             h18sp=args['h18sp'])
#
#        db.session.add(scorecard)
#        db.session.commit()
#
 #       ScoreCards.append(scorecard);
  #      return scorecard, 201
#
#    @marshal_with(resource_fields_scorecard)
#    def patch(self, sid):
#        args = scorecard_patch_args.parse_args()
#        result = ScoreCardModel.query.filter_by(id=sid).first()
#        if not result:
#            abort(404, message="ID NOT FOUND!")
#        if args['uid']:
#            result.uid = args['uid']
#        if args['h1r']:
#            result.h1r = args['h1r']
#        if args['h2r']:
#            result.h2r = args['h2r']
#        if args['h3r']:
#            result.h3r = args['h3r']
#        if args['h4r']:
#            result.h4r = args['h4r']
#        if args['h5r']:
#            result.h5r = args['h5r']
#        if args['h6r']:
#            result.h6r = args['h6r']
#        if args['h7r']:
#            result.h7r = args['h7r']
#        if args['h8r']:
#            result.h8r = args['h8r']
#        if args['h9r']:
#            result.h9r = args['h9r']
#        if args['h10r']:
#            result.h10r = args['h10r']
#        if args['h11r']:
#            result.h11r = args['h11r']
#        if args['h12r']:
#            result.h12r = args['h12r']
#        if args['h13r']:
#            result.h13r = args['h13r']
#        if args['h14r']:
#            result.h14r = args['h14r']
#        if args['h15r']:
#            result.h15r = args['h15r']
#        if args['h16r']:
#            result.h16r = args['h16r']
#        if args['h17r']:
#            result.h17r = args['h17r']
#        if args['h18r']:
#            result.h18r = args['h18r']
#        if args['h1hc']:
#            result.h1hc = args['h1hc']
#        if args['h2hc']:
#            result.h2hc = args['h2hc']
#        if args['h3hc']:
#            result.h3hc = args['h3hc']
#        if args['h4hc']:
#            result.h4hc = args['h4hc']
#        if args['h5hc']:
#            result.h5hc = args['h5hc']
#        if args['h6hc']:
#            result.h6hc = args['h6hc']
#        if args['h7hc']:
#            result.h7hc = args['h7hc']
#        if args['h8hc']:
#            result.h8hc = args['h8hc']
#        if args['h9hc']:
#            result.h9hc = args['h9hc']
#        if args['h10hc']:
#            result.h10hc = args['h10hc']
#        if args['h11hc']:
#            result.h11hc = args['h11hc']
#        if args['h12hc']:
#            result.h12hc = args['h12hc']
#        if args['h13hc']:
#            result.h13hc = args['h13hc']
#        if args['h14hc']:
#            result.h14hc = args['h14hc']
#        if args['h15hc']:
#            result.h15hc = args['h15hc']
#        if args['h16hc']:
#            result.h16hc = args['h16hc']
#        if args['h17hc']:
#            result.h17hc = args['h17hc']
#        if args['h18hc']:
#            result.h18hc = args['h18hc']
#        if args['h1sp']:
#            result.h1sp = args['h1sp']
#        if args['h2sp']:
#            result.h2sp = args['h2sp']
#        if args['h3sp']:
#            result.h3sp = args['h3sp']
#        if args['h4sp']:
#            result.h4sp = args['h4sp']
#        if args['h5sp']:
#            result.h5sp = args['h5sp']
#        if args['h6sp']:
#            result.h6sp = args['h6sp']
#        if args['h7sp']:
#            result.h7sp = args['h7sp']
#        if args['h8sp']:
#            result.h8sp = args['h8sp']
#        if args['h9sp']:
#            result.h9sp = args['h9sp']
#        if args['h10sp']:
#            result.h10sp = args['h10sp']
#        if args['h11sp']:
#            result.h11sp = args['h11sp']
#        if args['h12sp']:
#            result.h12sp = args['h12sp']
#        if args['h13sp']:
#            result.h13sp = args['h13sp']
#        if args['h14sp']:
#            result.h14sp = args['h14sp']
#        if args['h15sp']:
#            result.h15sp = args['h15sp']
#        if args['h16sp']:
#            result.h16sp = args['h16sp']
#        if args['h17sp']:
#            result.h17sp = args['h17sp']
#        if args['h18sp']:
#            result.h18sp = args['h18sp']
#
#
 #       db.session.commit()
  #      return result

#    def delete(self, sid):
#        result = ScoreCardModel.query.filter_by(id=sid).first()
#        if not result:
#            abort(404, message="ID NOT FOUND!")
#
#        db.session.delete(result)
 #       db.session.commit()
#
#        return '', 204


api.add_resource(User, "/user/<int:uid>")
api.add_resource(Course, "/course/<int:cid>")
#api.add_resource(ScoreCard, "/scorecard/<int:sid>")

if __name__ == "__main__":
    app.run()