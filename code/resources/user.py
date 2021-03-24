import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UsersRegistration(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username",
                        type=str,
                        required=True,
                        help="This field cannot be left blank"
                        )
    parser.add_argument("password",
                        type=str,
                        required=True,
                        help="This field cannot be left blank"
                        )

    def post(self):
        data = UsersRegistration.parser.parse_args()

        if UserModel.find_by_username(data["username"]):
            return {"message": "Username already registered"}, 400
        user = UserModel(**data)
        user.save_to_db()
        return {"message": "User created successfully!!"}, 201
