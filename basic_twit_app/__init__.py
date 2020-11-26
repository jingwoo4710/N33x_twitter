import os
from flask import Flask
from basic_twit_app.routes import main_routes, tweet_routes
from basic_twit_app.models import db, migrate


# DATAVASE_URI ("sqlite:///twit.sqlite3")
DATABASE_URI = "postgres://wjtwnbjlsljupc:a21855bcb707466b630b9995697cc9d16a182eac951f03431d4acb1cf9a3636b@ec2-3-214-46-194.compute-1.amazonaws.com:5432/d57gss8v0p7oiu"
#"postgres://wjtwnbjlsljupc:a21855bcb707466b630b9995697cc9d16a182eac951f03431d4acb1cf9a3636b@ec2-3-214-46-194.compute-1.amazonaws.com:5432/d57gss8v0p7oiu"

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
