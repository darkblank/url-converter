from flask import Flask, jsonify, request

from app.apis import api


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(api, url_prefix='/api')

    @app.route('/ping')
    def health_check():
        return jsonify(dict(ok='ok'))

    @app.teardown_request
    def teardown_sessions(exception):
        ctx = request._get_current_object()
        if hasattr(ctx, '_current_session'):
            if exception:
                ctx._current_session.rollback()
            ctx._current_session.close()

    return app
