import flask
from flask import request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

Users = [];
Courses = [];

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


db.create_all()

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
course_put_args.add_argument("name", type=str, help="Name of the Golf Course")
course_put_args.add_argument("par", type=str, help="Par for the Course")
course_put_args.add_argument("h1p", type=int, help="Hole 1 Par")
course_put_args.add_argument("h2p", type=int, help="Hole 2 Par")
course_put_args.add_argument("h3p", type=int, help="Hole 3 Par")
course_put_args.add_argument("h4p", type=int, help="Hole 4 Par")
course_put_args.add_argument("h5p", type=int, help="Hole 5 Par")
course_put_args.add_argument("h6p", type=int, help="Hole 6 Par")
course_put_args.add_argument("h7p", type=int, help="Hole 7 Par")
course_put_args.add_argument("h8p", type=int, help="Hole 8 Par")
course_put_args.add_argument("h9p", type=int, help="Hole 9 Par")
course_put_args.add_argument("h10p", type=int, help="Hole 10 Par")
course_put_args.add_argument("h11p", type=int, help="Hole 11 Par")
course_put_args.add_argument("h12p", type=int, help="Hole 12 Par")
course_put_args.add_argument("h13p", type=int, help="Hole 13 Par")
course_put_args.add_argument("h14p", type=int, help="Hole 14 Par")
course_put_args.add_argument("h15p", type=int, help="Hole 15 Par")
course_put_args.add_argument("h16p", type=int, help="Hole 16 Par")
course_put_args.add_argument("h17p", type=int, help="Hole 17 Par")
course_put_args.add_argument("h18p", type=int, help="Hole 18 Par")
course_put_args.add_argument("h1hc", type=int, help="Hole 1 Handicap")
course_put_args.add_argument("h2hc", type=int, help="Hole 2 Handicap")
course_put_args.add_argument("h3hc", type=int, help="Hole 3 Handicap")
course_put_args.add_argument("h4hc", type=int, help="Hole 4 Handicap")
course_put_args.add_argument("h5hc", type=int, help="Hole 5 Handicap")
course_put_args.add_argument("h6hc", type=int, help="Hole 6 Handicap")
course_put_args.add_argument("h7hc", type=int, help="Hole 7 Handicap")
course_put_args.add_argument("h8hc", type=int, help="Hole 8 Handicap")
course_put_args.add_argument("h9hc", type=int, help="Hole 9 Handicap")
course_put_args.add_argument("h10hc", type=int, help="Hole 10 Handicap")
course_put_args.add_argument("h11hc", type=int, help="Hole 11 Handicap")
course_put_args.add_argument("h12hc", type=int, help="Hole 12 Handicap")
course_put_args.add_argument("h13hc", type=int, help="Hole 13 Handicap")
course_put_args.add_argument("h14hc", type=int, help="Hole 14 Handicap")
course_put_args.add_argument("h15hc", type=int, help="Hole 15 Handicap")
course_put_args.add_argument("h16hc", type=int, help="Hole 16 Handicap")
course_put_args.add_argument("h17hc", type=int, help="Hole 17 Handicap")
course_put_args.add_argument("h18hc", type=int, help="Hole 18 Handicap")

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
    def put(self, uid):
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

        Users.append(user);
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
    def put(self, cid):
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

        Courses.append(course);
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

api.add_resource(User, "/user/<int:uid>")
api.add_resource(Course, "/course/<int:cid>")

if __name__ == "__main__":
    app.run()