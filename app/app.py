from flask import Flask, jsonify


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    @app.route('/ping')
    def health_check():
        return jsonify(dict(ok='ok'))

    return app
