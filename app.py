from flask import Flask, render_template
from flask_migrate import Migrate
from logging.config import dictConfig
from config import DEBUG, Session

from models.User import db
from routes.auth_bp import auth_bp
from routes.user_bp import user_bp

# Logging Configurations
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '%(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

# Setup Flask App
app = Flask(__name__)
app.config.from_object('config')

# Setup Database
db.init_app(app)
migrate = Migrate(app, db)

# Setup Routes
app.register_blueprint(auth_bp, url_prefix='/')
app.register_blueprint(user_bp, url_prefix='/users')


@app.route('/')
# Setup Index page.
def index():
    return render_template('index.html')


@app.errorhandler(404)
# Show Custom Page when route don't found.
def page_not_found(error):
    return render_template('errors/404.html'), 404


@app.teardown_appcontext
# Remove Session when App exit.
def cleanup(resp_or_exc):
    Session.remove()


# Run Flask App
if __name__ == '__main__':
    app.debug = DEBUG
    app.run()
