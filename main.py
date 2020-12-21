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

db.create_all()

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

resource_fields = {
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
    @marshal_with(resource_fields)
    def get(self, uid):
        # abort_if_id_doesnt_exist(uid)
        # return Users[uid]
        result = UserModel.query.filter_by(id=uid).first()
        if not result:
            abort(404, message="Could Not Find That User")
        return result

    @marshal_with(resource_fields)
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

    @marshal_with(resource_fields)
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


api.add_resource(User, "/user/<int:uid>")

if __name__ == "__main__":
    app.run()