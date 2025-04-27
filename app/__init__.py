import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()
API_KEY = 'SECRET123'

def create_app():
    # Enable instance-relative config so instance_path points to ../instance
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # ensure instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)
    # use absolute path for the SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        'sqlite:///' + os.path.join(app.instance_path, 'health.db')
    )

    db.init_app(app)
    ma.init_app(app)

    # register blueprints
    from app.routes.clients    import clients_bp
    from app.routes.programs   import programs_bp
    from app.routes.enrollments import enrollments_bp

    app.register_blueprint(clients_bp)
    app.register_blueprint(programs_bp)
    app.register_blueprint(enrollments_bp)

    # simple API key check
    @app.before_request
    def require_api_key():
        if request.endpoint != 'home':
            auth = request.headers.get('Authorization')
            if auth != f'Bearer {API_KEY}':
                return jsonify({'error':'Unauthorized'}), 401

    @app.route('/')
    def home():
        return 'Welcome to Health Info System secured API!'

    # create tables
    with app.app_context():
        from app import models
        db.create_all()

    return app
