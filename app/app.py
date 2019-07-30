from flask import Flask, jsonify

from app.apis import api


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(api, url_prefix='/api')

    @app.route('/ping')
    def health_check():
        return jsonify(dict(ok='ok'))

    return app
