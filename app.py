from flask import Flask
from flask_restful import Api
from security import authenticate, identity
from resources.user import UsersRegistration,User
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from flask_jwt import JWT
from db import db

app = Flask(__name__)
app.secret_key = "Jan-2021"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXPECTATION"]=True
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)

api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UsersRegistration, "/register")
api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")
api.add_resource(User,"/user/<int:user_id>")

if __name__ == "__main__":


    db.init_app(app)
    app.run(port=8082, debug=True)
