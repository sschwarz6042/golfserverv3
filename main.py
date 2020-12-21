import flask
from flask import request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

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
    h1 = db.Column(db.Integer, nullable=False)
    h2 = db.Column(db.Integer, nullable=False)
    h3 = db.Column(db.Integer, nullable=False)
    h4 = db.Column(db.Integer, nullable=False)
    h5 = db.Column(db.Integer, nullable=False)
    h6 = db.Column(db.Integer, nullable=False)
    h7 = db.Column(db.Integer, nullable=False)
    h8 = db.Column(db.Integer, nullable=False)
    h9 = db.Column(db.Integer, nullable=False)
    h10 = db.Column(db.Integer, nullable=False)
    h11 = db.Column(db.Integer, nullable=False)
    h12 = db.Column(db.Integer, nullable=False)
    h13 = db.Column(db.Integer, nullable=False)
    h14 = db.Column(db.Integer, nullable=False)
    h15 = db.Column(db.Integer, nullable=False)
    h16 = db.Column(db.Integer, nullable=False)
    h17 = db.Column(db.Integer, nullable=False)
    h18 = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return "Course(name = {name}, par = {par}, h1 = {h1}, h2 = {h2}, h3 = {h3}, h4 = {h4}, h5 = {h5}, h6 = {h6}, h7 = {h7}, h8 = {h8}, h9 = {h9}, h10 = {h10}, h11 = {h11}, h12 = {h12}, h13 = {h13}, h14 = {h14}, h15 = {h15}, h16 = {h16}, h17 = {h17}, h18 = {h18}"


db.create_all()

course_put_args = reqparse.RequestParser()
course_put_args.add_argument("name", type=str, help="Name of the Golf Course", required=True)
course_put_args.add_argument("par", type=str, help="Par for the Course", required=True)
course_put_args.add_argument("h1", type=int, help="Hole 1 Par", required=True)
course_put_args.add_argument("h2", type=int, help="Hole 2 Par", required=True)
course_put_args.add_argument("h3", type=int, help="Hole 3 Par", required=True)
course_put_args.add_argument("h4", type=int, help="Hole 4 Par", required=True)
course_put_args.add_argument("h5", type=int, help="Hole 5 Par", required=True)
course_put_args.add_argument("h6", type=int, help="Hole 6 Par", required=True)
course_put_args.add_argument("h7", type=int, help="Hole 7 Par", required=True)
course_put_args.add_argument("h8", type=int, help="Hole 8 Par", required=True)
course_put_args.add_argument("h9", type=int, help="Hole 9 Par", required=True)
course_put_args.add_argument("h10", type=int, help="Hole 10 Par", required=False)
course_put_args.add_argument("h11", type=int, help="Hole 11 Par", required=False)
course_put_args.add_argument("h12", type=int, help="Hole 12 Par", required=False)
course_put_args.add_argument("h13", type=int, help="Hole 13 Par", required=False)
course_put_args.add_argument("h14", type=int, help="Hole 14 Par", required=False)
course_put_args.add_argument("h15", type=int, help="Hole 15 Par", required=False)
course_put_args.add_argument("h16", type=int, help="Hole 16 Par", required=False)
course_put_args.add_argument("h17", type=int, help="Hole 17 Par", required=False)
course_put_args.add_argument("h18", type=int, help="Hole 18 Par", required=False)

course_update_args = reqparse.RequestParser()
course_update_args.add_argument("name", type=str, help="Name of the Golf Course")
course_update_args.add_argument("par", type=int, help="Par for the course")
course_update_args.add_argument("h1", type=int, help="Hole 1 par")
course_update_args.add_argument("h2", type=int, help="Hole 2 par")
course_update_args.add_argument("h3", type=int, help="Hole 3 par")
course_update_args.add_argument("h4", type=int, help="Hole 4 par")
course_update_args.add_argument("h5", type=int, help="Hole 5 par")
course_update_args.add_argument("h6", type=int, help="Hole 6 par")
course_update_args.add_argument("h7", type=int, help="Hole 7 par")
course_update_args.add_argument("h8", type=int, help="Hole 8 par")
course_update_args.add_argument("h9", type=int, help="Hole 9 par")
course_update_args.add_argument("h10", type=int, help="Hole 10 par")
course_update_args.add_argument("h11", type=int, help="Hole 11 par")
course_update_args.add_argument("h12", type=int, help="Hole 12 par")
course_update_args.add_argument("h13", type=int, help="Hole 13 par")
course_update_args.add_argument("h14", type=int, help="Hole 14 par")
course_update_args.add_argument("h15", type=int, help="Hole 15 par")
course_update_args.add_argument("h16", type=int, help="Hole 16 par")
course_update_args.add_argument("h17", type=int, help="Hole 17 par")
course_update_args.add_argument("h18", type=int, help="Hole 18 par")

resource_fields_course = {
    'id': fields.Integer,
    'name': fields.String,
    'par': fields.Integer,
    'h1': fields.Integer,
    'h2': fields.Integer,
    'h3': fields.Integer,
    'h4': fields.Integer,
    'h5': fields.Integer,
    'h6': fields.Integer,
    'h7': fields.Integer,
    'h8': fields.Integer,
    'h9': fields.Integer,
    'h10': fields.Integer,
    'h11': fields.Integer,
    'h12': fields.Integer,
    'h13': fields.Integer,
    'h14': fields.Integer,
    'h15': fields.Integer,
    'h16': fields.Integer,
    'h17': fields.Integer,
    'h18': fields.Integer
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
        args = user_put_args.parse_args()
        result = UserModel.query.filter_by(id=uid).first()
        if result:
            abort(409, message="ID TAKEN!")

        user = UserModel(id=uid, email=args['email'], username=args['username'], handicap=args['handicap'],
                         password=args['password'])
        db.session.add(user)
        db.session.commit()
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
        args = course_put_args.parse_args()
        result = CourseModel.query.filter_by(id=cid).first()
        if result:
            abort(409, message="COURSE ID TAKEN!")

        course = CourseModel(id=cid, name=args['name'], par=args['par'],
                             h1=args['h1'],
                             h2=args['h2'],
                             h3=args['h3'],
                             h4=args['h4'],
                             h5=args['h5'],
                             h6=args['h6'],
                             h7=args['h7'],
                             h8=args['h8'],
                             h9=args['h9'],
                             h10=args['h10'],
                             h11=args['h11'],
                             h12=args['h12'],
                             h13=args['h13'],
                             h14=args['h14'],
                             h15=args['h15'],
                             h16=args['h16'],
                             h17=args['h17'],
                             h18=args['h18'])
        db.session.add(course)
        db.session.commit()
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
        if args['h1']:
            result.h1 = args['h1']
        if args['h2']:
            result.h1 = args['h2']
        if args['h3']:
            result.h1 = args['h3']
        if args['h4']:
            result.h1 = args['h4']
        if args['h5']:
            result.h1 = args['h5']
        if args['h6']:
            result.h1 = args['h6']
        if args['h7']:
            result.h1 = args['h7']
        if args['h8']:
            result.h1 = args['h8']
        if args['h9']:
            result.h1 = args['h9']
        if args['h10']:
            result.h1 = args['h10']
        if args['h11']:
            result.h1 = args['h11']
        if args['h12']:
            result.h1 = args['h12']
        if args['h13']:
            result.h1 = args['h13']
        if args['h14']:
            result.h1 = args['h14']
        if args['h15']:
            result.h1 = args['h15']
        if args['h16']:
            result.h1 = args['h16']
        if args['h17']:
            result.h1 = args['h17']
        if args['h18']:
            result.h1 = args['h18']

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