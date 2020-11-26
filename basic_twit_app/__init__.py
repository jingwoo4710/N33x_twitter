import os
from flask import Flask
from basic_twit_app.routes import main_routes, tweet_routes
from basic_twit_app.models import db, migrate
from dotenv import load_dotenv

# 환경변수 load
load_dotenv()

# DATAVASE_URI ("sqlite:///twit.sqlite3")
DATABASE_URI = os.getenv('DATABASE_URI')

# Factory pattern
def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main_routes.main_routes)
    app.register_blueprint(tweet_routes.tweet_routes)
    
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
